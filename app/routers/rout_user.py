from fastapi import Depends, HTTPException, Request, status, APIRouter
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

from .. import models, utils
from app.database import get_db
from ..schemas import UserCreate, UserOut
from util.templates import get_templates

router = APIRouter(
    prefix="/users",
    tags=["Users"],  # Adds headers to documentation http://127.0.0.1:8000/redoc
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user: models.User = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get("/", response_class=HTMLResponse)
def display_create_user_form(request: Request):
    return get_templates().TemplateResponse("create_user.html", {"request": request})


@router.get("/{id}", response_class=HTMLResponse)
def get_user_info(request: Request, id: int, db: Session = Depends(get_db)):
    user: models.User = db.query(models.User).filter(models.User.id == id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return get_templates().TemplateResponse("user_info.html", {"request": request, "user": user})

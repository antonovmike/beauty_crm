from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from . import models
from .database import engine
from .routers import rout_appointment, rout_user


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(rout_user.router)
app.include_router(rout_appointment.router)

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root(request: Request):
    message = "Beauty CRM"
    return templates.TemplateResponse("index.html", {"request": request, "message": message})

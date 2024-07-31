from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from . import models
from .database import engine
from .routers import rout_appointment, rout_user
from util.templates import get_templates


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(rout_user.router)
app.include_router(rout_appointment.router)


@app.get("/", response_class=HTMLResponse)
async def read_main(request: Request, templates: Jinja2Templates = Depends(get_templates)):
    message = "Beauty CRM"
    return templates.TemplateResponse("index.html", {"request": request, "message": message})

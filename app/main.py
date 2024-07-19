from fastapi import FastAPI
from pydantic import BaseModel

from . import models
from .database import engine
from .routers import rout_user


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(rout_user.router)


@app.get("/")
async def root():
    return {"message": "Beauty CRM"}

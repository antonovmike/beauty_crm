from fastapi import FastAPI
from pydantic import BaseModel

from . import models
from .database import engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Beauty CRM"}

from fastapi import FastAPI
from .database import engine
from . import models
from .routes import form
from dotenv import load_dotenv

load_dotenv()

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(form.router)

@app.get("/")
def root():
    return {"message": "KPA API is running!"}

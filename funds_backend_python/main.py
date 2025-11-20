from fastapi import FastAPI
from .database import engine
from . import models
from funds_backend_python.routers import customers

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(customers.router, prefix="/customers", tags=["customers"])

@app.get("/health")
def health_check():
    return {"status": "ok"}

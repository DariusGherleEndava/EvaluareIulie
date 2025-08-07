from fastapi import FastAPI
from app.api import math_api
from app.db.database import Base, engine
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# Create database tables at startup
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
    Instrumentator().instrument(app).expose(app)

app.include_router(math_api.router)

@app.get("/")
def read_root():
    return {"message": "Math Service API is running"}

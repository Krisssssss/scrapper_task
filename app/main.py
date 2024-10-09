from fastapi import FastAPI
from app.routers.suspect_router import suspect_router
from app.config import init_db

app = FastAPI()

init_db()

app.include_router(suspect_router, prefix="/suspects", tags=["Suspects"])


@app.get("/")
def read_root():
    return {"message": "Welcome!"}

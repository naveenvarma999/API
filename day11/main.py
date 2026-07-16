from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import sessionlocal

app = FastAPI()

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "Database connection API is running"}


@app.get("/test-db")
def test_database_connection(db: Session = Depends(get_db)):
    return {"message": "Database connected successfully"}


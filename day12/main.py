from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import SessionLocal, engine, Base
import models

app = FastAPI()

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "SQLAlchemy model and table created successfully"}


@app.get("/test-db")
def test_database_connection(db: Session = Depends(get_db)):
    return {"message": "Database connected successfully"}
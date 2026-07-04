from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel, Field


app = FastAPI()

class student(BaseModel):
    name: str = Field(min_length= 2, max_length = 100)
    course : str
    age : int = Field(gt= 0, le = 100)
    email : Optional[str] = None
    is_active: bool = True


@app.get("/")
def Home():
    return {"message": "API is running successfully with validation"}


@app.post("/students")
def create_students(student: student):
    return {"message": "Student created successfully", "student": student}      




from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class student(BaseModel):
    name : str
    course: str
    age : int

@app.get("/")
def home():
    return {"message": "API is running successfully"}   

@app.post("/students")
def create_student(student: student):
    return {
        "message": "Student created successfully",
        "student": student
    }
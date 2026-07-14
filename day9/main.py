from fastapi import FastAPI, Request
from pydantic import BaseModel, Field
import time

app = FastAPI()


class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    age: int = Field(gt=0, le=100)
    course: str


students = []


@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()

    print("Request method:", request.method)
    print("Request URL:", request.url)

    response = await call_next(request)

    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)

    print("Response status code:", response.status_code)
    print("Process time:", process_time)

    return response


@app.get("/")
def home():
    return {"message": "Middleware API is running"}


@app.post("/students")
def create_student(student: StudentCreate):
    new_student = {
        "id": len(students) + 1,
        "name": student.name,
        "age": student.age,
        "course": student.course
    }

    students.append(new_student)

    return {
        "message": "Student created successfully",
        "student": new_student
    }


@app.get("/students")
def get_all_students():
    return {
        "total_students": len(students),
        "students": students
    }


@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student

    return {"message": "Student not found"}
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()


class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    age: int = Field(gt=0, le=100)
    course: str


students = []


def common_message():
    return "This message came from Depends function"


def check_admin(role: str):
    if role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Only admin can access this API"
        )
    return role


@app.get("/")
def home():
    return {"message": "Depends API is running"}


@app.get("/info")
def get_info(message: str = Depends(common_message)):
    return {
        "message": message
    }


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


@app.delete("/admin/students/{student_id}")
def delete_student_by_admin(
    student_id: int,
    role: str = Depends(check_admin)
):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return {
                "message": "Student deleted successfully by admin"
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )
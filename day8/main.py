from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()


class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    age: int = Field(gt=0, le=100)
    course: str


students = []


@app.get("/")
def home():
    return {"message": "Exception handling API is running"}


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
    if len(students) == 0:
        raise HTTPException(
            status_code=404,
            detail="No students found"
        )

    return {
        "total_students": len(students),
        "students": students
    }


@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id <= 0:
        raise HTTPException(
            status_code=400,
            detail="Student ID must be greater than 0"
        )

    for student in students:
        if student["id"] == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: StudentCreate):
    if student_id <= 0:
        raise HTTPException(
            status_code=400,
            detail="Student ID must be greater than 0"
        )

    for student in students:
        if student["id"] == student_id:
            student["name"] = updated_student.name
            student["age"] = updated_student.age
            student["course"] = updated_student.course

            return {
                "message": "Student updated successfully",
                "student": student
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id <= 0:
        raise HTTPException(
            status_code=400,
            detail="Student ID must be greater than 0"
        )

    for student in students:
        if student["id"] == student_id:
            students.remove(student)

            return {
                "message": "Student deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )
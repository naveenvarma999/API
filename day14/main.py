from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal, engine, Base
from models import Student
from schema import StudentCreate

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
    return {"message": "Student database API is running"}


@app.post("/students")
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    new_student = Student(
        name=student.name,
        age=student.age,
        course=student.course
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return {
        "message": "Student inserted into database successfully",
        "student": {
            "id": new_student.id,
            "name": new_student.name,
            "age": new_student.age,
            "course": new_student.course
        }
    }


@app.get("/students")
def get_all_students(db: Session = Depends(get_db)):
    students = db.query(Student).all()

    return {
        "total_students": len(students),
        "students": students
    }


@app.get("/students/{student_id}")
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student
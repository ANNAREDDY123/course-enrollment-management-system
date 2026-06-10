from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from models.models import Student
from schemas.schemas import StudentCreate

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("")
def create_student(
        student: StudentCreate,
        db: Session = Depends(get_db)
):

    existing = db.query(Student).filter(
        Student.email == student.email
    ).first()

    if existing:
        raise HTTPException(
            400,
            "Email already exists"
        )

    db_student = Student(
        name=student.name,
        email=student.email,
        phone=student.phone,
        department=student.department
    )

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student


@router.get("")
def get_students(
        db: Session = Depends(get_db)
):
    return db.query(Student).all()


@router.get("/{student_id}")
def get_student(
        student_id: int,
        db: Session = Depends(get_db)
):

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        raise HTTPException(
            404,
            "Student not found"
        )

    return student


@router.put("/{student_id}")
def update_student(
        student_id: int,
        student: StudentCreate,
        db: Session = Depends(get_db)
):

    db_student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not db_student:
        raise HTTPException(
            404,
            "Student not found"
        )

    db_student.name = student.name
    db_student.email = student.email
    db_student.phone = student.phone
    db_student.department = student.department

    db.commit()

    return {"message": "Student updated"}


@router.delete("/{student_id}")
def delete_student(
        student_id: int,
        db: Session = Depends(get_db)
):

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        raise HTTPException(
            404,
            "Student not found"
        )

    db.delete(student)
    db.commit()

    return {"message": "Student deleted"}

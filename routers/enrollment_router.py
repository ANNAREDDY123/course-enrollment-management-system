from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from models.models import Student, Course
from schemas.schemas import EnrollmentCreate

router = APIRouter(
    prefix="/enrollments",
    tags=["Enrollments"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("")
def enroll_student(
        enrollment: EnrollmentCreate,
        db: Session = Depends(get_db)
):

    student = db.query(Student).filter(
        Student.id == enrollment.student_id
    ).first()

    course = db.query(Course).filter(
        Course.id == enrollment.course_id
    ).first()

    if not student:
        raise HTTPException(
            404,
            "Student not found"
        )

    if not course:
        raise HTTPException(
            404,
            "Course not found"
        )

    if course in student.courses:
        raise HTTPException(
            400,
            "Duplicate enrollment not allowed"
        )

    student.courses.append(course)

    db.commit()

    return {"message": "Enrollment successful"}


@router.get("/students/{student_id}/courses")
def student_courses(
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

    return student.courses


@router.get("/courses/{course_id}/students")
def course_students(
        course_id: int,
        db: Session = Depends(get_db)
):

    course = db.query(Course).filter(
        Course.id == course_id
    ).first()

    if not course:
        raise HTTPException(
            404,
            "Course not found"
        )

    return course.students

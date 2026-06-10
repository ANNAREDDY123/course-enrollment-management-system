from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from models.models import Course
from schemas.schemas import CourseCreate

router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("")
def create_course(
        course: CourseCreate,
        db: Session = Depends(get_db)
):

    existing = db.query(Course).filter(
        Course.course_code == course.course_code
    ).first()

    if existing:
        raise HTTPException(
            400,
            "Course code already exists"
        )

    db_course = Course(**course.model_dump())

    db.add(db_course)
    db.commit()
    db.refresh(db_course)

    return db_course


@router.get("")
def get_courses(
        db: Session = Depends(get_db)
):
    return db.query(Course).all()


@router.get("/{course_id}")
def get_course(
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

    return course


@router.put("/{course_id}")
def update_course(
        course_id: int,
        course: CourseCreate,
        db: Session = Depends(get_db)
):

    db_course = db.query(Course).filter(
        Course.id == course_id
    ).first()

    if not db_course:
        raise HTTPException(
            404,
            "Course not found"
        )

    db_course.course_name = course.course_name
    db_course.course_code = course.course_code
    db_course.instructor = course.instructor
    db_course.duration = course.duration
    db_course.is_active = course.is_active

    db.commit()

    return {"message": "Course updated"}


@router.delete("/{course_id}")
def delete_course(
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

    db.delete(course)
    db.commit()

    return {"message": "Course deleted"}

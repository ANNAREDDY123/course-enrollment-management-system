from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    Table
)

from sqlalchemy.orm import relationship

from database import Base


# -----------------------------------
# Many To Many Association Table
# -----------------------------------

enrollments = Table(
    "enrollments",
    Base.metadata,

    Column(
        "student_id",
        Integer,
        ForeignKey("students.id")
    ),

    Column(
        "course_id",
        Integer,
        ForeignKey("courses.id")
    )
)


# -----------------------------------
# USER TABLE
# -----------------------------------

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    username = Column(String, unique=True)

    password = Column(String)

    role = Column(String)


# -----------------------------------
# COURSE TABLE
# -----------------------------------

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)

    course_name = Column(String)

    course_code = Column(
        String,
        unique=True
    )

    instructor = Column(String)

    duration = Column(String)

    is_active = Column(
        Boolean,
        default=True
    )

    students = relationship(
        "Student",
        secondary=enrollments,
        back_populates="courses"
    )


# -----------------------------------
# STUDENT TABLE
# -----------------------------------

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)

    name = Column(String)

    email = Column(
        String,
        unique=True
    )

    phone = Column(String)

    department = Column(String)

    courses = relationship(
        "Course",
        secondary=enrollments,
        back_populates="students"
    )

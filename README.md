# course-enrollment-management-system
FastAPI backend application for managing courses, students, enrollments, authentication, and role-based access control using JWT, SQLAlchemy, and SQLite.
# Course Enrollment Management System

## Tech Stack

- FastAPI
- SQLAlchemy
- Pydantic
- SQLite
- JWT Authentication

## Features

### Authentication

- Register User
- Login User
- JWT Token Generation

### Course Management

- Create Course
- View Courses
- Update Course
- Delete Course

### Student Management

- Create Student
- View Students
- Update Student
- Delete Student

### Enrollment Management

- Enroll Student
- View Student Courses
- View Course Students

## Validations

- Unique Email
- Unique Course Code
- Prevent Duplicate Enrollment

## Run Project

pip install -r requirements.txt
py -m uvicorn main:app --reload

Swagger:

http://127.0.0.1:8000/docs

course-enrollment-management-system/

README.md
requirements.txt
database.py
main.py
schema.sql
queries.sql

auth/
    auth_handler.py

models/
    models.py

schemas/
    schemas.py

routers/
    auth_router.py
    course_router.py
    student_router.py
    enrollment_router.py



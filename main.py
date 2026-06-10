from fastapi import FastAPI

from database import engine, Base

from routers.auth_router import router as auth_router
from routers.course_router import router as course_router
from routers.student_router import router as student_router
from routers.enrollment_router import router as enrollment_router

app = FastAPI(
    title="Course Enrollment Management System"
)

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(course_router)
app.include_router(student_router)
app.include_router(enrollment_router)


@app.get("/")
def home():
    return {
        "message":
        "Course Enrollment Management System Running"
    }

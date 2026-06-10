from pydantic import BaseModel, EmailStr



# AUTH


class UserRegister(BaseModel):
    username: str
    password: str
    role: str


class UserLogin(BaseModel):
    username: str
    password: str



# COURSE


class CourseCreate(BaseModel):
    course_name: str
    course_code: str
    instructor: str
    duration: str
    is_active: bool



# STUDENT


class StudentCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    department: str



# ENROLLMENT


class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int

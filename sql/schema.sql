CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    role VARCHAR(20)
);

CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    department VARCHAR(100)
);

CREATE TABLE courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name VARCHAR(100),
    course_code VARCHAR(50) UNIQUE,
    instructor VARCHAR(100),
    duration VARCHAR(50),
    is_active BOOLEAN
);

CREATE TABLE enrollments (
    student_id INTEGER,
    course_id INTEGER,
    FOREIGN KEY(student_id)
        REFERENCES students(id),
    FOREIGN KEY(course_id)
        REFERENCES courses(id)
);

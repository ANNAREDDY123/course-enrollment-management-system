-- Students enrolled in each course

SELECT
    c.course_name,
    COUNT(e.student_id) AS total_students
FROM courses c
LEFT JOIN enrollments e
ON c.id = e.course_id
GROUP BY c.id;


-- Courses per student

SELECT
    s.name,
    COUNT(e.course_id) AS total_courses
FROM students s
LEFT JOIN enrollments e
ON s.id = e.student_id
GROUP BY s.id;


-- Top enrolled courses

SELECT
    c.course_name,
    COUNT(e.student_id) AS enrollments
FROM courses c
JOIN enrollments e
ON c.id = e.course_id
GROUP BY c.id
ORDER BY enrollments DESC;


-- Active courses

SELECT *
FROM courses
WHERE is_active = 1;


-- Student Ranking

SELECT
    student_name,
    total_courses,
    RANK() OVER(
        ORDER BY total_courses DESC
    ) AS rank_no
FROM
(
    SELECT
        s.name AS student_name,
        COUNT(e.course_id) AS total_courses
    FROM students s
    LEFT JOIN enrollments e
    ON s.id=e.student_id
    GROUP BY s.id
) ranked_students;

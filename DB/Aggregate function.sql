-- Write an SQL query to calculate the total payments made by a specific student. You will need to join the "Payments" table with the "Students" table based on the student's ID.
SELECT *
FROM [students];

SELECT *
FROM [payments]


SELECT p.student_id, SUM(p.amount), s.first_name
FROM [students] s INNER JOIN [payments] p
ON  s.student_id = p.student_id
GROUP BY p.student_id, s.first_name
HAVING p.student_id = 'S0001'

-- Write an SQL query to retrieve a list of courses along with the count of students enrolled in each course. Use a JOIN operation between the "Courses" table and the "Enrollments" table

SELECT * 
FROM [course] c;

SELECT *
FROM [enrollments];

SELECT c.course_id, c.course_name, COUNT(e.enrollment_id) AS No_of_Enrollments
FROM [course] c  INNER JOIN [enrollments] e
ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name

-- Write an SQL query to find the names of students who have not enrolled in any course. Use a LEFT JOIN between the "Students" table and the "Enrollments" table to identify students without enrollments.

SELECT *
FROM [enrollments];

SELECT *
FROM [students];

SELECT CONCAT(s.first_name,' ',s.last_name) AS Non_Enrollers
FROM [students] s LEFT JOIN [enrollments] e
ON s.student_id = e.student_id
WHERE e.enrollment_id IS NULL

--Write an SQL query to retrieve the first name, last name of students, and the names of the courses they are enrolled in. Use JOIN operations between the "Students" table and the "Enrollments" and "Courses" tables.

SELECT s.first_name, s.last_name, c.course_name
FROM [course] c INNER JOIN (
							SELECT s.student_id,s.first_name,s.last_name,e.course_id
							FROM [students] s INNER JOIN [enrollments] e
							ON s.student_id = e.student_id
)AS s
ON s.course_id = c.course_id;

-- Create a query to list the names of teachers and the courses they are assigned to. Join the "Teacher" table with the "Courses" table.


SELECT CONCAT(t.first_name,' ',t.last_name) AS teacher_name, c.course_name
FROM [teacher] t LEFT JOIN [course] c
ON t.teacher_id = c.teacher_id

-- Retrieve a list of students and their enrollment dates for a specific course. You'll need to join the "Students" table with the "Enrollments" and "Courses" tables

SELECT *
FROM [students]

SELECT *
FROM [course]

SELECT *
FROM [enrollments]

SELECT se.student_id, se.first_name, se.last_name,c.course_id, c.course_name, se.enrollment_date
FROM [course] c INNER JOIN (
							SELECT s.student_id, s.first_name, s.last_name, e.course_id, e.enrollment_date
							FROM [students] s INNER  JOIN [enrollments] e
							ON s.student_id = e.student_id
)AS se
ON c.course_id = se.course_id

--Find the names of students who have not made any payments. Use a LEFT JOIN between the "Students" table and the "Payments" table and filter for students with NULL payment records.

SELECT CONCAT(s.first_name,' ',s.last_name) AS name
FROM [students] s LEFT JOIN [payments] p
ON s.student_id = p.student_id
WHERE p.payment_id IS NULL

--Write a query to identify courses that have no enrollments. You'll need to use a LEFT JOIN between the "Courses" table and the "Enrollments" table and filter for courses with NULL enrollment records

SELECT *
FROM [course] c LEFT JOIN [enrollments] e
ON c.course_id = e.course_id
WHERE e.enrollment_id IS NULL

--Identify students who are enrolled in more than one course. Use a self-join on the "Enrollments" table to find students with multiple enrollment records

SELECT s.student_id, COUNT(course_id) AS courses_enrolled
FROM [students] s INNER JOIN  [enrollments] e
ON s.student_id = e.student_id
GROUP BY s.student_id
HAVING COUNT(course_id) > 1

SELECT a.student_id
FROM [enrollments] a JOIN [enrollments] b
ON a.student_id = b.student_id
GROUP by a.student_id
HAVING COUNT(a.enrollment_id) > 1

--Find teachers who are not assigned to any courses. Use a LEFT JOIN between the "Teacher" table and the "Courses" table and filter for teachers with NULL course assignments.

SELECT * 
FROM [teacher] t LEFT JOIN [course] c
ON t.teacher_id = c.teacher_id
WHERE c.course_id IS NULL

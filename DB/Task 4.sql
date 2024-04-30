USE [SISDB]
GO
--1. Write an SQL query to calculate the average number of students enrolled in each course. Use aggregate functions and subqueries to achieve this.

SELECT	e.course_id, 
		c.course_name, 
		AVG(e.No_of_enrollers) AS Avg_Enrollment
FROM	[course] c 
		INNER JOIN (
		SELECT 	[course_id], 
				COUNT([student_id]) AS No_of_enrollers
		FROM 	[enrollments]
		GROUP BY [course_id]
	) AS e
ON			e.course_id = c.course_id
GROUP BY	e.course_id, c.course_name, e.No_of_enrollers

--2. Identify the student(s) who made the highest payment. Use a subquery to find the maximum payment amount and then retrieve the student(s) associated with that amount.

SELECT *
FROM	[students] a
WHERE	[student_id] IN (
		SELECT	[student_id]
		FROM	[payments] b
		WHERE	amount = (
			SELECT	MAX([amount])
			FROM	[payments] c
)
);
--3. Retrieve a list of courses with the highest number of enrollments. Use subqueries to find the course(s) with the maximum enrollment count

SELECT  c.*, 
		e.student_count
FROM	[course] c INNER JOIN (
	SELECT course_id, 
			COUNT(student_id) AS student_count
	FROM	[enrollments] i
	GROUP BY [course_id]
) e
ON			c.course_id = e.course_id
ORDER BY	[student_count] DESC
OFFSET 0 ROWS
FETCH NEXT 1 ROWS ONLY;



--4. Calculate the total payments made to courses taught by each teacher. Use subqueries to sum payments for each teacher's courses

SELECT	*
FROM	[teacher] t 
		INNER JOIN(
				SELECT	c.course_id, 
						c.teacher_id, 
						SUM(e.amount) AS earnings_made
				FROM	[course] c 
						INNER JOIN(
							SELECT	s.student_id,
									e.course_id,
									s.amount
							FROM	[enrollments] e 
									INNER JOIN (
											SELECT	s.student_id,	
													p.amount
											FROM	[students] s 
													INNER JOIN [payments] p
											ON		s.student_id = p.student_id
											) s
							ON		e.student_id = s.student_id
							) e
				ON		c.course_id = e.course_id
				GROUP BY c.course_id,c.teacher_id
				) p
ON		t.teacher_id = p.teacher_id
ORDER BY p.earnings_made DESC
OFFSET 0 ROWS
FETCH NEXT 1 ROWS ONLY;


--5.  Identify students who are enrolled in all available courses. Use subqueries to compare a student's enrollments with the total number of courses

SELECT	* 
FROM	[students]
WHERE	[student_id] IN (
						SELECT	student_id
						FROM	[enrollments]
						GROUP BY student_id
						HAVING	COUNT(course_id) = (
												SELECT	COUNT(course_id)
												FROM	[course]
						)
)

--6. Retrieve the names of teachers who have not been assigned to any courses. Use subqueries to find teachers with no course assignments

SELECT	*
FROM	[teacher] 
WHERE	[teacher_id] 
		NOT IN(
			SELECT	[teacher_id]
			FROM	[course]
)


--7. Calculate the average age of all students. Use subqueries to calculate the age of each student based on their date of birth.


SELECT	AVG(DATEDIFF(YEAR, date_of_birth, GETDATE())) AS Average_Age
FROM	[students]


--8. Identify courses with no enrollments. Use subqueries to find courses without enrollment records.

SELECT *
FROM	[course]
WHERE	[course_id] 
		NOT IN (
			SELECT	DISTINCT[course_id]
			FROM	[enrollments]
)

--9. Calculate the total payments made by each student for each course they are enrolled in. Use subqueries and aggregate functions to sum payments

SELECT	s.student_id,
		s.first_name,
		s.last_name,
		e.course_id,
		e.course_name,
		e.Total_payment
FROM	[students] s 
		INNER JOIN (
		SELECT	c.course_id, 
				c.course_name,
				e.student_id,
				e.Total_payment
		FROM	[course] c 
				INNER JOIN (
				SELECT	e.student_id,
						e.course_id,
						SUM(p.amount) AS Total_payment
				FROM	[enrollments] e 
						INNER JOIN [payments] p
				ON		e.student_id = p.student_id
				GROUP BY e.student_id,e.course_id
				) e
		ON		c.course_id = e.course_id
		) e
ON		e.student_id = s.student_id

--10. Identify students who have made more than one payment. Use subqueries and aggregate functions to count payments per student and filter for those with counts greater than one.

SELECT	*
FROM	[students]
WHERE	[student_id] 
		IN (
			SELECT	[student_id]
			FROM	[payments]
			GROUP BY [student_id]
			HAVING	COUNT([payment_id]) > 1
)


--11. Write an SQL query to calculate the total payments made by each student. Join the "Students" table with the "Payments" table and use GROUP BY to calculate the sum of payments for each student.

SELECT	p.student_id, 
		s.first_name, 
		s.last_name, 
		SUM(amount) Total_payments_made
FROM	[students] s 
		INNER JOIN [payments] p
ON		s.student_id = p.student_id
GROUP BY p.student_id, s.first_name, s.last_name

--12. Retrieve a list of course names along with the count of students enrolled in each course. Use JOIN operations between the "Courses" table and the "Enrollments" table and GROUP BY to count enrollments.

SELECT	c.course_id, 
		c.course_name,
		COUNT([student_id]) AS Total_Enrollments
FROM	[course] c 
		INNER JOIN [enrollments] e
ON		c.course_id = e.course_id
GROUP BY c.course_id,c.course_name

--13.  Calculate the average payment amount made by students. Use JOIN operations between the "Students" table and the "Payments" table and GROUP BY to calculate the average.

SELECT	s.student_id, 
		s.first_name,
		s.last_name,
		AVG(p.amount) AS Avg_Payment
FROM	[students] s LEFT JOIN [payments] p
ON		s.student_id = p.student_id
GROUP BY s.student_id,s.first_name,s.last_name
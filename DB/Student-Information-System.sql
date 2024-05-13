--TASK 1
SELECT ('TASK 1: Database Designs') AS [TASK LABEL]
GO
--1. Create the database named "SISDB"
-- Database is created with the name "SISDB"
CREATE DATABASE [SISDB]
GO
USE [SISDB]
GO

--2. Define the schema for the Students, Courses, Enrollments, Teacher, and Payments tables based on the provided schema. Write SQL scripts to create the mentioned tables with appropriate data types, constraints, and relationships. 
--a. Students 
--b. Courses
--c. Enrollments 
--d. Teacher 
--e. Payments
 -- Tables are created with appropriate data types, constraints, and relationships.
CREATE TABLE [students] (
  [student_id] varchar(10) NOT NULL,
  [first_name] varchar(255),
  [last_name] varchar(255),
  [date_of_birth] date,
  [email] varchar(255),
  [phone_number] varchar(10),
  CONSTRAINT student_pk PRIMARY KEY ([student_id])
);

CREATE TABLE [teacher] (
  [teacher_id] varchar(10) NOT NULL,
  [first_name] varchar(255),
  [last_name] varchar(255),
  [email] varchar(255),
  [expertise] varchar(255),
  CONSTRAINT teacher_pk PRIMARY KEY ([teacher_id])
);

CREATE TABLE [course] (
  [course_code] varchar(10) NOT NULL,
  [course_name] varchar(255),
  [credits] int,
  [teacher_id] varchar(10),
  [course_fee] float,
  CONSTRAINT course_pk PRIMARY KEY ([course_id]),
  CONSTRAINT teacher_fk FOREIGN KEY(teacher_id) REFERENCES teacher([teacher_id])
);

CREATE TABLE [payments] (
  [payment_id] int  NOT NULL IDENTITY(100,1),
  [student_id] varchar(10),
  [amount] float,
  [payment_date] date,
  CONSTRAINT payment_pk PRIMARY KEY ([payment_id]),
  CONSTRAINT student_payment_fk FOREIGN KEY(student_id) REFERENCES students([student_id])
);

CREATE TABLE [enrollments] (
  [enrollment_id] int  NOT NULL IDENTITY(200,1),
  [student_id] varchar(10),
  [course_code] varchar(10),
  [enrollment_date] date,
  CONSTRAINT enrollment_pk PRIMARY KEY ([enrollment_id]),
  CONSTRAINT student_fk FOREIGN KEY (student_id) REFERENCES students([student_id]),
  CONSTRAINT course_fk FOREIGN KEY (course_id) REFERENCES course([course_id])
);

--3. Create an ERD (Entity Relationship Diagram) for the database.
-- ERD for the SISDB database is in "SISDB_ERD.png" file in the same folder.

--4. Create appropriate Primary Key and Foreign Key constraints for referential integrity.
-- Primary Key constraints are defined for student_id, teacher_id, course_id, payment_id, and enrollment_id.

--5. Insert at least 10 sample records into each of the following tables.
--i. Students
--ii. Courses
--iii. Enrollments
--iv. Teacher
--v. Payments

-- Sample records for the tables are inserted below:
INSERT INTO [students] 
([student_id],[first_name],[last_name],[date_of_birth],[email],[phone_number])
VALUES ('S0001','Mathesh','Premkumar','2003-01-21','mathesh123@email.com','7788553300'),
	    ('S0002','Mohammed','Asik','2002-10-22','mohammedasik69@smail.com','5566224411'),
	    ('S0003','Manoj','P','2002-10-25','manoj@dev.com','3344556677'),
	    ('S0004','Mathew','Christopher','2002-09-24','mathewhere@email.com','5516223411'),
	    ('S0005','Kogul','K','2003-02-13','kkogul@nothing.com','5516223411'),
	    ('S0006','Sasidharan','M','2002-06-15','sasidharan.ai@dev.com','7576263432'),
	    ('S0007','Raj','Kumar','2002-01-01','rajkumarr@gmail.com','5563923732'),
	    ('S0008','Krishna','Moorthy','2002-08-22','krishmoor@none.com','8834023756'),
	    ('S0009','Nishant','S','2003-01-17','nishant007@xmail.com','6645382299'),
	    ('S0010','Karthick','K','2002-09-24','karthinah@fmail.com','7878964645'),
		('S0011','Ketheesa','K','2003-06-30','keth6211@gmail.com','7734644278');

INSERT INTO [teacher] 
([teacher_id],[first_name],[last_name],[email])
VALUES ('T0001','Ragav','kumar','ragavkumarv@gmail.com'),
	    ('T0002','Nelson','Dilipkumar','nelsondilip@email.com'),
	    ('T0003','Lokesh','kanagaraj','lokeshk@imail.com'),
	    ('T0004','Prithviraj','S','sprithvi@email.com'),
	    ('T0005','Haaris','Jeyaraj','hharrisj@gmail.com'),
	    ('T0006','Joseph','Vijay','cjvijay@email.com'),
	    ('T0007','Ajith','Kumar','ajithkumarak@vmail.com'),
	    ('T0008','Ashok','Selvan','ashokashok@email.com'),
	    ('T0009','Myskin','M','mmyskin@lmail.com'),
	    ('T0010','Vinoth','H','hvinoth@gmail.com'),
		('T0011','Gautham','Menon','gauthamvmenon@gmail.com'),
		('T0012','Fahadh','Fahsil','fahadhfah@fmail.com'),
		('T0013','Tovino','Thomas','tovintom87@gmaul.com'),
		('T0014','Suriya','Sivakumar','suriyamass@gmail.com');

INSERT INTO [course] ([course_id],[course_name],[credits],[teacher_id])
VALUES ('C0001','Problem Solving and Python Programming',3,'T0005'),
		('C0002','Computer Networks',1,'T0003'),
		('C0003','Software Development',3,'T0007'),
		('C0004','Object Oriented Programming with Java',3,'T0002'),
		('C0005','Advanced Java',3,'T0006'),
		('C0006','Data structures and Algorithm',3,'T0008'),
		('C0007','Cloud Computing',1,'T0001'),
		('C0008','Internet and Web Technology',2,'T0009'),
		('C0009','Mobile Application Development',2,'T0004'),
		('C0010','UI/UX Design',1,'T0005'),
		('C0011','Theory of Computation', 3,'T0011'),
		('C0012','Motion Graphics',1,'T0012'),
		('C0013','React Native',2,'T0013');

INSERT INTO [payments]([payment_id],[student_id],[amount],[payment_date])
VALUES ('P0001', 'S0001', 1250.5, '2023-04-01 '),
	('P0002', 'S0002', 800.4, '2023-04-02 '),
	('P0003', 'S0003', 1000.25, '2023-04-07 '),
	('P0004', 'S0004', 800.4, '2023-04-13 '),
	('P0005', 'S0005', 800.4, '2023-04-14 '),
	('P0006', 'S0006', 1600, '2023-04-16 '),
	('P0007', 'S0007', 800.4, '2023-04-21 '),
	('P0008', 'S0008', 800.4, '2023-04-22 '),
	('P0009', 'S0009', 1250.5, '2023-04-23 '),
	('P0010', 'S0010',1600, '2023-04-24 '),
	('P0011', 'S0011', 1250.5, '2023-04-25 ');

INSERT INTO [enrollments]([enrollment_id],[student_id],[course_id],[enrollment_date])
VALUES ('E0001', 'S0001', 'C0004', '2023-04-01 '),
	('E0002', 'S0002', 'C0001', '2023-04-02 '),
	('E0003', 'S0003', 'C0008', '2023-04-07 '),
	('E0004', 'S0004', 'C0001', '2023-04-13 '),
	('E0005', 'S0005', 'C0001', '2023-04-14 '),
	('E0006', 'S0006', 'C0005', '2023-04-16 '),
	('E0007', 'S0007', 'C0001', '2023-04-21 '),
	('E0008', 'S0008', 'C0001', '2023-04-22 '),
	('E0009', 'S0009', 'C0004', '2023-04-23 '),
	('E0010', 'S0010', 'C0005', '2023-04-24 '),
	('E0011', 'S0011', 'C0004', '2023-04-25 ');







--TASK 2
SELECT ('TASK 2: Select, Where, Between, AND, LIKE') AS [TASK LABEL]
GO

USE [SISDB]
GO

--1. Write an SQL query to insert a new student into the "Students" table with the following details:
--a. First Name: John
--b. Last Name: Doe
--c. Date of Birth: 1995-08-15
--d. Email: john.doe@example.com
--e. Phone Number: 1234567890
INSERT INTO	[students] ([student_id],[first_name],[last_name],[email],[date_of_birth],[phone_number])
    VALUES	('S0012','John','Doe','john.doe@example.com','1995-08-15','1234567890');

--2. Write an SQL query to enroll a student in a course. Choose an existing student and course and insert a record into the "Enrollments" table with the enrollment date
INSERT INTO [enrollments]([enrollment_id],[student_id],[course_id],[enrollment_date])
	VALUES	('E0012','S0012','C0008','2024-02-03')

--3. Update the email address of a specific teacher in the "Teacher" table. Choose any teacher and modify their email address.
UPDATE	[teacher]
SET		[email] = 'prithvirajsukumaran21@gmail.com'
WHERE	[teacher_id] = 'T0004'

--4. Write an SQL query to delete a specific enrollment record from the "Enrollments" table. Select an enrollment record based on the student and course.
DELETE 
FROM	[enrollments]
WHERE	[student_id] = 'S0001' AND [course_id] = 'C0005'


--5. Update the "Courses" table to assign a specific teacher to a course. Choose any course and teacher from the respective tables
UPDATE	[course]
SET		[teacher_id] = 'T0013'
WHERE	[course_id] = 'C0010'

--6. Delete a specific student from the "Students" table and remove all their enrollment records from the "Enrollments" table. Be sure to maintain referential integrity.
DELETE
FROM	[enrollments]
WHERE	[student_id] = 'S0012'

DELETE
FROM	[payments]
WHERE	[student_id] = 'S0012'

DELETE
FROM	[students]
WHERE	[student_id] = 'S0012'

--7.Update the payment amount for a specific payment record in the "Payments" table. Choose any payment record and modify the payment amount
UPDATE	[payments]
SET		[amount] = 2250.0
WHERE	[payment_id] = 'P0006'









--TASK 3
SELECT ('TASK 3: Aggregate functions, Having, Order By, GroupBy and Joins') AS [TASK LABEL]
USE [SISDB]
GO

--1. Write an SQL query to calculate the total payments made by a specific student. You will need to join the "Payments" table with the "Students" table based on the student's ID.

SELECT	p.student_id, 
		s.first_name, 
		SUM(p.amount) AS [Total Payments]
FROM	[students] s 
		INNER JOIN [payments] p
ON		s.student_id = p.student_id
GROUP BY p.student_id, s.first_name
HAVING	p.student_id = 'S0001'

--2. Write an SQL query to retrieve a list of courses along with the count of students enrolled in each course. Use a JOIN operation between the "Courses" table and the "Enrollments" table

SELECT	c.course_id, 
		c.course_name, 
		COUNT(e.enrollment_id) AS No_of_Enrollments
FROM	[course] c  INNER JOIN [enrollments] e
ON		c.course_id = e.course_id
GROUP BY c.course_id, c.course_name

--3. Write an SQL query to find the names of students who have not enrolled in any course. Use a LEFT JOIN between the "Students" table and the "Enrollments" table to identify students without enrollments.

SELECT	CONCAT(s.first_name,' ',s.last_name) AS Non_Enrollers
FROM	[students] s 
		LEFT JOIN [enrollments] e
ON		s.student_id = e.student_id
WHERE	e.enrollment_id IS NULL

--4. Write an SQL query to retrieve the first name, last name of students, and the names of the courses they are enrolled in. Use JOIN operations between the "Students" table and the "Enrollments" and "Courses" tables.

SELECT	s.first_name, 
		s.last_name, 
		c.course_name
FROM	[course] c 
		INNER JOIN (
					SELECT	s.student_id,
							s.first_name,
							s.last_name,
							e.course_id
					FROM	[students] s 
							INNER JOIN [enrollments] e
					ON		s.student_id = e.student_id
		)AS	s
ON		s.course_id = c.course_id;

--5. Create a query to list the names of teachers and the courses they are assigned to. Join the "Teacher" table with the "Courses" table.


SELECT	CONCAT(t.first_name,' ',t.last_name) AS teacher_name, 
		c.course_name
FROM	[teacher] t 
		LEFT JOIN [course] c
ON		t.teacher_id = c.teacher_id

--6. Retrieve a list of students and their enrollment dates for a specific course. You'll need to join the "Students" table with the "Enrollments" and "Courses" tables

SELECT	se.student_id, 
		se.first_name, 
		se.last_name,
		c.course_id, 
		c.course_name, 
		se.enrollment_date
FROM	[course] c 
		INNER JOIN (
					SELECT	s.student_id, 
							s.first_name, 
							s.last_name, 
							e.course_id, 
							e.enrollment_date
					FROM	[students] s 
							INNER  JOIN [enrollments] e
					ON		s.student_id = e.student_id
)AS se
ON		c.course_id = se.course_id

--7. Find the names of students who have not made any payments. Use a LEFT JOIN between the "Students" table and the "Payments" table and filter for students with NULL payment records.

SELECT	CONCAT(s.first_name,' ',s.last_name) AS name
FROM	[students] s 
		LEFT JOIN [payments] p
ON		s.student_id = p.student_id
WHERE	p.payment_id IS NULL

--8. Write a query to identify courses that have no enrollments. You'll need to use a LEFT JOIN between the "Courses" table and the "Enrollments" table and filter for courses with NULL enrollment records

SELECT	*
FROM	[course] c 
		LEFT JOIN [enrollments] e
ON		c.course_id = e.course_id
WHERE	e.enrollment_id IS NULL

--9. Identify students who are enrolled in more than one course. Use a self-join on the "Enrollments" table to find students with multiple enrollment records

SELECT	s.student_id,
		s.first_name,
		s.last_name, 
		COUNT(course_id) AS courses_enrolled
FROM	[students] s 
		INNER JOIN  [enrollments] e
ON		s.student_id = e.student_id
GROUP BY GROUPING SETS	((s.student_id,s.first_name,s.last_name))
HAVING	COUNT(course_id) > 1

SELECT	a.student_id
FROM	[enrollments] a 
		JOIN [enrollments] b
ON		a.student_id = b.student_id
GROUP by a.student_id
HAVING	COUNT(a.enrollment_id) > 1

--10. Find teachers who are not assigned to any courses. Use a LEFT JOIN between the "Teacher" table and the "Courses" table and filter for teachers with NULL course assignments.

SELECT	* 
FROM	[teacher] t LEFT JOIN [course] c
ON		t.teacher_id = c.teacher_id
WHERE	c.course_id IS NULL




--TASK 4
SELECT ('TASK 4: Subquery & its types') AS [TASK LABEL]
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

--DROP DATABASE [SISDB]
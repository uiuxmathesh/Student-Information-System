--1.Write an SQL query to insert a new student into the "Students" table 
INSERT INTO [students] ([student_id],[first_name],[last_name],[email],[date_of_birth],[phone_number])
    VALUES ('S0012','John','Doe','john.doe@example.com','1995-08-15','1234567890');

--2. Choose an existing student and course and insert a record into the "Enrollments" table with the enrollment date
INSERT INTO [enrollments]([enrollment_id],[student_id],[course_id],[enrollment_date])
	VALUES ('E0011','S0011','C0008','2024-02-03');

--3. Update the email address of a specific teacher in the "Teacher" table. Choose any teacher and modify their email address
UPDATE [teacher]
SET [email] = 'prithvirajsukumaran21@gmail.com'
WHERE [teacher_id] = 'T0004';

--4. Update the "Courses" table to assign a specific teacher to a course. Choose any course and teacher from the respective tables
UPDATE [course]
SET [teacher_id] = 'T0010'
WHERE [course_id] = 'C0010';

--5. Update the payment amount for a specific payment record in the "Payments" table. Choose any payment record and modify the payment amount
UPDATE [payments]
SET [amount] = 2250.0
WHERE [payment_id] = 'P0006';

--6. Delete a specific enrollment record from the "Enrollments" table. Select an enrollment record based on the student and course.
SELECT *
FROM [enrollments]
WHERE [student_id] ='S0001' AND [course_id] = 'C0005';

DELETE
FROM [enrollments]
WHERE [student_id] ='S0001' AND [course_id] = 'C0005';

--7.Delete a specific student from the "Students" table and remove all their enrollment records from the "Enrollments" table. Be sure to maintain referential integrity
--Method 1:
DELETE
FROM [enrollments]
WHERE [student_id] = 'S0006';

DELETE
FROM [payments]
WHERE [student_id] = 'S0006';

DELETE
FROM [students]
WHERE [student_id] = 'S0006';

--Method 2:
ALTER TABLE [dbo].[enrollments] DROP CONSTRAINT [student_fk]
GO

ALTER TABLE [dbo].[enrollments]  WITH CHECK ADD  CONSTRAINT [student_fk] FOREIGN KEY([student_id])
REFERENCES [dbo].[students] ([student_id]) ON DELETE CASCADE
GO

ALTER TABLE [dbo].[enrollments] CHECK CONSTRAINT [student_fk]
GO

ALTER TABLE [dbo].[payments] DROP CONSTRAINT [student_payment_fk]
GO

ALTER TABLE [dbo].[payments]  WITH CHECK ADD  CONSTRAINT [student_payment_fk] FOREIGN KEY([student_id])
REFERENCES [dbo].[students] ([student_id]) ON DELETE CASCADE
GO

ALTER TABLE [dbo].[payments] CHECK CONSTRAINT [student_payment_fk]
GO

DELETE
FROM [students]
WHERE [student_id] = 'S0006'
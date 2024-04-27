INSERT INTO [students] ([student_id],[first_name],[last_name],[email],[date_of_birth],[phone_number])
    VALUES ('S0012','John','Doe','john.doe@example.com','1995-08-15','1234567890');

INSERT INTO [enrollments]([enrollment_id],[student_id],[course_id],[enrollment_date])
	VALUES ('E0011','S0011','C0008','2024-02-03')

UPDATE [teacher]
SET [email] = 'prithvirajsukumaran21@gmail.com'
WHERE [teacher_id] = 'T0004'

UPDATE [course]
SET [teacher_id] = 'T0010'
WHERE [course_id] = 'C0010'


UPDATE [payments]
SET [amount] = 2250.0
WHERE [payment_id] = 'P0006'
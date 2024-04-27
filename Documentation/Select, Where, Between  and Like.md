# `SELECT`, `WHERE`, `BETWEEN` AND `LIKE`

1. Write an SQL query to insert a new student into the "Students" table with the following details:
    - First Name: John
    - Last Name: Doe
    - Date of Birth: 1995-08-15
    - Email: john.doe@example.com
    - Phone Number: 1234567890

    ```sql
    INSERT INTO [students] ([student_id],[first_name],[last_name],[email],[date_of_birth],[phone_number])
    VALUES ('S0012','John','Doe','john.doe@example.com','1995-08-15','1234567890');
    ```
2. Choose an existing student and course and insert a record into the "Enrollments" table with the enrollment date

    ```sql
    INSERT INTO [enrollments]([enrollment_id],[student_id],[course_id],[enrollment_date])
	VALUES ('E0011','S0011','C0008','2024-02-03')
    ```
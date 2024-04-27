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

3. Update the email address of a specific teacher in the "Teacher" table. Choose any teacher and modify their email address

    Let's say we're updating the email address of a teacher with teacher_id = T0004

    ```sql
    UPDATE [teacher]
    SET [email] = 'prithvirajsukumaran21@gmail.com'
    WHERE [teacher_id] = 'T0004'
    ```
4. Update the "Courses" table to assign a specific teacher to a course. Choose any course and teacher from the respective tables

    Let's say we're updating the course with course_id = 'C0010'. It is assigned to teacher with teacher_id = 'T0008'.
    We're going to update the teeacher_id to 'T0010'

    ```sql
    UPDATE [course]
    SET [teacher_id] = 'T0010'
    WHERE [course_id] = 'C0010'
    ```
5. Update the payment amount for a specific payment record in the "Payments" table. Choose any payment record and modify the payment amount

    Let's say we want to modify the payment record with `payment_id = 'P006'`. We want to update the amount as `amount = 2250.0`
    ```sql
    UPDATE [payments]
    SET [amount] = 2250.0
    WHERE [payment_id] = 'P0006'
    ```
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

6. Delete a specific enrollment record from the "Enrollments" table. Select an enrollment record based on the student and course.
    
    It is said to delete a enrollment record from the 'Enrollments' table.
    Additionally, we need to delete the record based on student and course. 
    This means we should not delete the record by 'enrollment_id' like before.

    Let's say we need to delete the record which have `student_id='S0001'` and `course_id='C0005'`. We can do this by executing the following query.

    Before deleting the record let's first check if we're deleting the right record. We can do this by writing our delete logic for a `SELECT` statement. If the resultant record is what we're intending to delete, then we can proceed further with `DELETE` statement.

    ```sql
    -- Writing a SELECT statement for verification
    SELECT *
    FROM [enrollments]
    WHERE [student_id] ='S0001' AND [course_id] = 'C0005'
    ```

    As the `SELECT` query gives the right record, we can proceed further.

    Now let's move on to deleting that particular record
    ```sql
    DELETE
    FROM [enrollments]
    WHERE [student_id] = 'S0001' AND [course_id] = 'C0005'
    ```
7. Delete a specific student from the "Students" table and remove all their enrollment records from the "Enrollments" table. Be sure to maintain referential integrity

    It is given that we need to delete a record from **'students'** table. While doing so we must also delete the records in the **'enrollments'** table which are associated with the particular `student_id` that gets deleted. Additionally, we need to also delete records from **'payments'** table as that might also be associated with that particular `student-id`. This helps to ensure that the referential integrity remains unaffected.

    Let's say we need to delete a record from student table with `student_id = 'S0006'`
    There are 2 ways by which we can delete the record and maintain the referential integrity

    - Method 1:
    First we need to delete all the associated records of that `student_id` in `enrollments` and `payment` table.

    This is to make sure that no records in both the table can be associated with a non-existing `student_id`

    Let's do that by executing the below query
    ```sql
    DELETE
    FROM [enrollments],
    WHERE [student_id] = 'S0006'

    DELETE
    FROM [payments],
    WHERE [student_id] = 'S0006'

    This query deletes all the associated records of that particular `student_id`
    ```
    Now we can proceed to delete the particular `student-id` from **'students'** table.

    ```sql
    DELETE
    FROM [students],
    WHERE [student_id] = 'S0006'
    ```
    - Method 2:
    We can maintain the referential integrity of data by giving the command `ON DELETE CASCADE` at the time of foreign key creation 
    
    This command helps in this situation by automatically deleting all child records when the parent record gets deleted.

    But to do so, we need to delete our current **foreign key constraint** and make a new **foreign key constraint** with the `ON DELETE CASCADE` command.

    To do so in SQL server, execute the following command
    ```sql
    USE [SISDB]
    GO

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
    ```
    This commands will drop the existing **Foreign key** constraint for the **enrollments'** and **'payments'** table and create a new one with `ON DELETE CASCADE` enabled.

    Now if you proceed to delete the `student_id` no foreign key can stop the deletion from happening.

    Let's delete the `student_id` from our **'student'** table
    ```sql
    DELETE
    FROM [students]
    WHERE [student_id] = 'S0006'
    ```
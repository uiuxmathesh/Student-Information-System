# Subquery and its types

**Task 1: Write an SQL query to calculate the average number of students enrolled in each course. Use aggregate functions and subqueries to achieve this.**
- We need to use `GROUP BY` to *group* the **'enrollments'** table and *count* the occurence of `student_id`

    ```sql
        SELECT [course_id], COUNT([student_id]) AS No_of_enrollers
	    FROM [enrollments]
	    GROUP BY [course_id]
    ```

**Task 2: Identify the student(s) who made the highest payment. Use a subquery to find the maximum payment amount and then retrieve the student(s) associated with that amount.**

- Step 1: Identifying highest payment.
    ```sql
    SELECT MAX([amount])
    FROM [payments];
    ```

- Step 2: Identifying which student_id is associated with that payment.

    ```sql
    SELECT [student_id]
    FROM [payments]
    WHERE amount = (
	    SELECT MAX([amount])
	    FROM [payments]
    );
    ```
- Step 3: Identifying whom does the student id belongs to.
    
    ```sql
    SELECT *
    FROM [students]
    WHERE [student_id] IN (
	    SELECT [student_id]
	    FROM [payments]
	    WHERE amount = (
		    SELECT MAX([amount])
		    FROM [payments]
    )
    );
    ```
**Task 3: Retrieve a list of courses with the highest number of enrollments. Use subqueries to find the course(s) with the maximum enrollment count.**

- Let's start by Identifying number of enrollment for a course by *Grouping* the courses form **'enrollments'** table and *Counting* the `student_id` for each group

    ```sql
    SELECT course_id, COUNT(student_id) AS student_count
	FROM [enrollments]
	GROUP BY [course_id]
    ```

 - Now that we have the `course-id` and No. of Ennrollment on each course as `student_count`, Let's Join this with the **'course'** table using `INNER  JOIN`.

    ```sql
    SELECT c.*, e.student_count
    FROM [course] c INNER JOIN (
	    SELECT course_id, COUNT(student_id) AS student_count
	    FROM [enrollments]
	    GROUP BY [course_id]	
    ) e
    ON c.course_id = e.course_id
    ```
- Now, let's order the table based on `student_count` in decreasing order.

    ```sql
    SELECT c.*, e.student_count
    FROM [course] c INNER JOIN (
	    SELECT course_id, COUNT(student_id) AS student_count
	    FROM [enrollments]
	    GROUP BY [course_id]	
    ) e
    ON c.course_id = e.course_id
    ORDER BY [student_count] DESC;
    ```
-We can, see that the course with most enrollment is now in the top. We can get only that record by limiting the `SELECT` queries output to display only one record on the top.
- In SQL Server, the `LIMIT` Keyword doesn't work. So, we need to make use of `TOP()` keyword to acheive the required output.

    ```sql
    SELECT TOP(1) c.*, e.student_count
    FROM [course] c INNER JOIN (
	    SELECT course_id, COUNT(student_id) AS student_count
	    FROM [enrollments]
	    GROUP BY [course_id]	
    ) e
    ON c.course_id = e.course_id
    ORDER BY [student_count] DESC;
    ```

**`ERROR` Task 4: Calculate the total payments made to courses taught by each teacher. Use subqueries to sum payments for each teacher's courses**

- As from the ERD itself, we can say that the *payments* table is no way related to anyother tables except *student* table 
- Even if we somehow Join the *enrollments*, *payments* and *students*, *courses* table, we can only answer the question,
    - **How much amount is paid by a student?**
- It can never answer the question,
    - **Which course does he/she paid for?**
- If only we know the answer of the above question, then we can calculate the total payments made to courses taught by each teacher
- Hence, it is not possible to write a query for this situation

**Task 5: Identify students who are enrolled in all available courses. Use subqueries to compare a student's enrollments with the total number of courses**

-  Step 1: Identifying Number of Courses in the **'course'** table.

    ```sql
    SELECT COUNT(course_id)
    FROM [course];
    ```
- Step 2: Identifying `student_id`s of students who is enrolled in all the courses
    ```sql
    SELECT student_id
    FROM [enrollments]
    GROUP BY student_id
    HAVING COUNT(course_id) = (
							SELECT COUNT(course_id)
							FROM [course]
    );
    ```
- Step 3: Identiying the records of students in **'students'** table with respect to those `student_id`s from **'enrollment'** table

    ```sql
    SELECT * 
    FROM [students]
    WHERE [student_id] IN (
						SELECT student_id
						FROM [enrollments]
						GROUP BY student_id
						HAVING COUNT(course_id) = (
													SELECT COUNT(course_id)
													FROM [course]
						)
    );
    ```
**Task 6: Retrieve the names of teachers who have not been assigned to any courses. Use subqueries to find teachers with no course assignments**

- Fetching `teacher_id`s of all courses from **'course'** table
    
    ```sql
    SELECT [teacher_id]
	FROM [course];
    ```
    
- Listing all teachers whose `teacher_id`s are not in th previous query

    ```sql
    SELECT *
    FROM [teacher] 
    WHERE [teacher_id] NOT IN(
	    SELECT [teacher_id]
	    FROM [course]
    );

**Task 7: Calculate the average age of all students. Use subqueries to calculate the age of each student based on their date of birth.**
 
- Calculating The Age with `DATEDIFF` method

    ```sql
    SELECT DATEDIFF(YEAR, date_of_birth, GETDATE()) AS Age
    FROM [students]
    ```

- Applying `AVG` aggregation on top of it to calculate Average age

    ```sql
    SELECT AVG(DATEDIFF(YEAR, date_of_birth, GETDATE())) AS Average_Age
    FROM [students]
    ```

**Task 8: Identify courses with no enrollments. Use subqueries to find courses without enrollment records.**

- Fetching all the `course_ide` from **'eenrollments'** table

    ```sql
    SELECT [course_id]
	FROM [enrollments]
    ```
- Fetching courses from **'course'** table whose `course_id` is not listed in the result of previous query

    ```sql
    SELECT *
    FROM [course]
    WHERE [course_id] NOT IN (
    						SELECT [course_id]
    						FROM [enrollments]
    )
    ```
**`ERROR` Task 9: Calculate the total payments made by each student for each course they are enrolled in. Use subqueries and aggregate functions to sum payments**

- As from the ERD itself, we can say that the *payments* table is no way related to anyother tables except *student* table 
- Even if we somehow Join the *enrollments*, *payments* and *students*, *courses* table, we can only answer the question,
    - **How much amount is paid by a student?**
- It can never answer the question,
    - **Which course does he/she paid for?**

**Task 10: Identify students who have made more than one payment. Use subqueries and aggregate functions to count payments per student and filter for those with counts greater than one.**

- Let's first Identity the `student_id`'s of the student who made moree than one payment with `GROUP BY` and `HAVING` clauses from **'payments'* table

    ```sql
    SELECT [student_id]
	FROM [payments]
	GROUP BY [student_id]
	HAVING COUNT([payment_id]) > 1
    ```
- Next, we can select the students with `student_id`s from **'students'** tables which is same as `student_id` fetched from previous query

    ```sql
    SELECT *
    FROM [students]
    WHERE [student_id] IN (
					SELECT [student_id]
					FROM [payments]
					GROUP BY [student_id]
					HAVING COUNT([payment_id]) > 1
    )
    ```

**Task 11: Write an SQL query to calculate the total payments made by each student. Join the "Students" table with the "Payments" table and use GROUP BY to calculate the sum of payments for each student.**

-   ```sql
        SELECT p.student_id, s.first_name, s.last_name, SUM(amount) Total_payments_made
        FROM [students] s INNER JOIN [payments] p
        ON s.student_id = p.student_id
        GROUP BY p.student_id, s.first_name, s.last_name
        ```

**Task 12: Retrieve a list of course names along with the count of students enrolled in each course. Use JOIN operations between the "Courses" table and the "Enrollments" table and GROUP BY to count enrollments.**

-   ```sql
        SELECT e.course_id, COUNT([student_id]) AS Total_Enrollments
        FROM [course] c INNER JOIN [enrollments] e
        ON c.course_id = e.course_id
        GROUP BY e.course_id
    ```

**Task 13: Calculate the average payment amount made by students. Use JOIN operations between the "Students" table and the "Payments" table and GROUP BY to calculate the average.**

-   ```sql
        SELECT s.student_id, AVG(p.amount)
        FROM [students] s LEFT JOIN [payments] p
        ON s.student_id = p.student_id
        GROUP BY s.student_id
    ```

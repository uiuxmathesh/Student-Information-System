# Aggregate Functions, HAVING, ORDER BY, GROUP BY and JOINS

**Task 1: Write an SQL query to calculate the total payments made by a specific student. You will need to join the "Payments" table with the "Students" table based on the student's ID.**

- It is said that we need to calculate the total payments made by a specific student.
Let's assume the `student_id` is `S0001`

- At first, We need to Join the **'payments'** table and **'students'** table

    ```sql
    SELECT  *
    FROM    [students] s 
            INNER JOIN [payments] p
    ON      s.student_id = p.student_id
    ```
- From this Joined table, we need to extract the `student_id`, `first_name`, `last_name` and the sum of total amount made by them using aggregaate function `SUM()` and `GROUP BY` clause

    ```sql
    SELECT  p.student_id,
            s.first_name, 
            SUM(p.amount) AS [Total Payments]
    FROM    [students] s 
            INNER JOIN [payments] p
    ON      s.student_id = p.student_id
    GROUP BY p.student_id, s.first_name
     ```

- Now to get paymment information of a specific children, we need to use `HAVING` clause along with `GROUP BY`clause

    ```sql
    SELECT  p.student_id, 
            s.first_name, 
            SUM(p.amount) AS [Total Payments]
    FROM    [students] s 
            INNER JOIN [payments] p
    ON      s.student_id = p.student_id
    GROUP BY p.student_id, s.first_name
    HAVING  p.student_id = 'S0001'
    ```

**Task 2: Write an SQL query to retrieve a list of courses along with the count of students enrolled in each course. Use a JOIN operation between the "Courses" table and the "Enrollments" table**

- To retrieve a list of courses along with the count of students enrolled in each course we need to join the tables `course` and `enrollments` using `INNER JOIN`

    ```sql
    SELECT  *
    FROM    [course] c  
            INNER JOIN [enrollments] e
    ON      c.course_id = e.course_id
    ```

- Now we just need to apply `GROUP BY` clause to achieve the objective

    ```sql
    SELECT  c.course_id, 
            c.course_name, 
            COUNT(e.enrollment_id) AS No_of_Enrollments
    FROM    [course] c  
            INNER JOIN [enrollments] e
    ON      c.course_id = e.course_id
    GROUP BY c.course_id, c.course_name
    ```

**Task 3: Write an SQL query to find the names of students who have not enrolled in any course. Use a LEFT JOIN between the "Students" table and the "Enrollments" table to identify students without enrollments.**

- We can do this by using `LEFT JOIN` on the tables `sstudents` and `enrollments` so that the resulting table will have `NULL` values for those who have not enrolled in any course.
    ```sql
    SELECT  CONCAT(s.first_name,' ',s.last_name) AS Non_Enrollers
    FROM    [students] s 
            LEFT JOIN [enrollments] e
    ON      s.student_id = e.student_id
    ```
- Now Just apply a `WHERE` clause on top of it to filter the records that has `NULL` in the field of `enrollment_id`

    ```sql
    SELECT  CONCAT(s.first_name,' ',s.last_name) AS Non_Enrollers
    FROM    [students] s 
            LEFT JOIN [enrollments] e
    ON      s.student_id = e.student_id
    WHERE   e.enrollment_id IS NULL
    ```
**Task 4: Write an SQL query to retrieve the first name, last name of students, and the names of the courses they are enrolled in. Use JOIN operations between the "Students" table and the "Enrollments" and "Courses" tables.**

- Since, this operation requires Joining of more than two tables, we need to do them using sub-query


    ```sql
    SELECT  s.student_id, 
            s.first_name, 
            s.last_name, 
            e.course_id, 
	FROM    [students] s 
            INNER  JOIN [enrollments] e
	ON      s.student_id = e.student_id;
    ```
- The above query will join `students` and `enrollments` table based on the `student_id`. 


    ```sql
    SELECT  s.first_name, 
            s.last_name,
            c.course_name, 
    FROM    [course] c 
            INNER JOIN (
						SELECT  s.student_id, 
                                s.first_name, 
                                s.last_name, 
                                e.course_id, 
						FROM    [students] s 
                                INNER  JOIN [enrollments] e
						ON      s.student_id = e.student_id
            )AS s
    ON      s.course_id = c.course_id;
    ```
- This query will nest the previous query and finds the enrollment date for the courses that each students have enrolled

**Task 5: Create a query to list the names of teachers and the courses they are assigned to. Join the "Teacher" table with the "Courses" table.**

    ```sql
    SELECT	CONCAT(t.first_name,' ',t.last_name) AS teacher_name, 
		    c.course_name
    FROM	[teacher] t 
		    LEFT JOIN [course] c
    ON		t.teacher_id = c.teacher_id
    ```
**Task 6: Retrieve a list of students and their enrollment dates for a specific course. You'll need to join the "Students" table with the "Enrollments" and "Courses" tables**

    ```sql
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
    ```

**Task 7: Find the names of students who have not made any payments. Use a LEFT JOIN between the "Students" table and the "Payments" table and filter for students with NULL payment records.**

- First we need to `LEFT JOIN` the tables `payments` and `students` so that the student with no payment history will be listed with `NULL` values. Then we can just filter the required fields with a `WHERE` clause  having `IS NULL` values

    ```sql
    SELECT  CONCAT(s.first_name,' ',s.last_name) AS name
    FROM    [students] s 
            LEFT JOIN [payments] p
    ON      s.student_id = p.student_id
    WHERE   p.payment_id IS NULL
    ```

**Task 8: Write a query to identify courses that have no enrollments. You'll need to use a LEFT JOIN between the "Courses" table and the "Enrollments" table and filter for courses with NULL enrollment records**

- We are going to use the same logic as in the above query with a `LEFT JOIN` between `enrollments ` and `courses` table

    ```sql
    SELECT  *
    FROM    [course] c 
            LEFT JOIN [enrollments] e
    ON      c.course_id = e.course_id
    WHERE   e.enrollment_id IS NULL
    ```

**Task 9: Identify students who are enrolled in more than one course. Use a self-join on the "Enrollments" table to find students with multiple enrollment records**

- We are going to use `INNER JOIN` to join the tables `enrollments` and then just simply find the records with occurence of `enrollment_id` more than once ( With the help of `GROUP BY`)

    ```sql
    SELECT	a.student_id
    FROM	[enrollments] a 
		    JOIN [enrollments] b
    ON		a.student_id = b.student_id
    GROUP by a.student_id
    HAVING	COUNT(a.enrollment_id) > 1
    ```
**Task 10: Find teachers who are not assigned to any courses. Use a LEFT JOIN between the "Teacher" table and the "Courses" table and filter for teachers with NULL course assignments.**

- We can use `LEFT JOIN` on `teacher` table and `course` table and then filter out the records having `NULL` values  for `course_id` field

    ```sql
    SELECT  * 
    FROM    [teacher] t LEFT JOIN [course] c
    ON      t.teacher_id = c.teacher_id
    WHERE   c.course_id IS NULL
    ```


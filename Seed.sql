--Students
INSERT INTO [students] ([student_id], [first_name], [last_name], [date_of_birth], [email], [phone_number])
VALUES
    ('S0001', 'Alice', 'Johnson', '2000-03-15', 'alice.johnson@example.com', '1234567890'),
    ('S0002', 'Bob', 'Smith', '2001-05-20', 'bob.smith@example.com', '2345678901'),
    ('S0003', 'Charlie', 'Brown', '1999-08-10', 'charlie.brown@example.com', '3456789012'),
    ('S0004', 'David', 'Miller', '2002-01-25', 'david.miller@example.com', '4567890123'),
    ('S0005', 'Emma', 'Wilson', '2000-11-05', 'emma.wilson@example.com', '5678901234'),
    ('S0006', 'Frank', 'Taylor', '2003-04-30', 'frank.taylor@example.com', '6789012345'),
    ('S0007', 'Grace', 'Anderson', '2001-09-18', 'grace.anderson@example.com', '7890123456'),
    ('S0008', 'Henry', 'Thomas', '2000-06-12', 'henry.thomas@example.com', '8901234567');


-- Teachers
INSERT INTO [teacher] ([teacher_id], [first_name], [last_name], [email], [expertise])
VALUES
    ('T0001', 'John', 'Doe', 'john.doe@example.com', 'Computer Science'),
    ('T0002', 'Jane', 'Smith', 'jane.smith@example.com', 'Mathematics'),
    ('T0003', 'David', 'Brown', 'david.brown@example.com', 'Electrical Engineering'),
    ('T0004', 'Emily', 'Johnson', 'emily.johnson@example.com', 'English Literature');

-- Courses
INSERT INTO [course] ([course_code], [course_name], [credits], [teacher_id], [course_fee])
VALUES
    ('CS101', 'Introduction to Computer Science', 3, 'T0001', 1500.00),
    ('MA201', 'Calculus I', 4, 'T0002', 1800.00),
    ('EC301', 'Circuit Analysis', 4, 'T0003', 1900.00),
    ('CS201', 'Data Structures and Algorithms', 3, 'T0001', 1600.00),
    ('MA301', 'Linear Algebra', 3, 'T0002', 1700.00),
    ('EC401', 'Electromagnetic Theory', 4, 'T0003', 2000.00),
    ('EN101', 'Introduction to Literature', 3, 'T0004', 1500.00),
    ('CS301', 'Database Management Systems', 3, 'T0001', 1700.00);

-- Payments
INSERT INTO [payments] ([student_id], [amount], [payment_date])
VALUES
    ('S0001', 1500.00, '2024-05-01'),
    ('S0002', 1800.00, '2024-05-03'),
    ('S0003', 1900.00, '2024-05-05'),
    ('S0004', 1600.00, '2024-05-07'),
    ('S0005', 1700.00, '2024-05-10'),
    ('S0006', 2000.00, '2024-05-12'),
    ('S0007', 1500.00, '2024-05-15'),
    ('S0008', 1700.00, '2024-05-17');

-- Enrollments
INSERT INTO [enrollments] ([student_id], [course_code], [enrollment_date])
VALUES
    ('S0001', 'CS101', '2024-05-01'),
    ('S0002', 'MA201', '2024-05-03'),
    ('S0003', 'EC301', '2024-05-05'),
    ('S0004', 'CS201', '2024-05-07'),
    ('S0005', 'MA301', '2024-05-10'),
    ('S0006', 'EC401', '2024-05-12'),
    ('S0007', 'EN101', '2024-05-15'),
    ('S0008', 'CS301', '2024-05-17');


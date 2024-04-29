CREATE DATABASE SISDB
GO

-- For Creating Schemas
USE [SISDB];
GO

CREATE TABLE [students] (
  [student_id] varchar(5),
  [first_name] varchar(255),
  [last_name] varchar(255),
  [date_of_birth] date,
  [email] varchar(255),
  [phone_number] varchar(10),
  CONSTRAINT student_pk PRIMARY KEY ([student_id])
);

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


CREATE TABLE [teacher] (
  [teacher_id] varchar(5),
  [first_name] varchar(255),
  [last_name] varchar(255),
  [email] varchar(255),
  CONSTRAINT teacher_pk PRIMARY KEY ([teacher_id])
);

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
		('T0011','Gautham','Menon','gauthamvmenon@gmail.com');

CREATE TABLE [course] (
  [course_id] varchar(5),
  [course_name] varchar(255),
  [credits] int,
  [teacher_id] varchar(5),
  CONSTRAINT course_pk PRIMARY KEY ([course_id]),
  CONSTRAINT teacher_fk FOREIGN KEY(teacher_id) REFERENCES teacher([teacher_id])
);

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
		('C0010','UI/UX Design',1,'T0005');

CREATE TABLE [payments] (
  [payment_id] varchar(5),
  [student_id] varchar(5),
  [amount] float,
  [payment_date] date,
  CONSTRAINT payment_pk PRIMARY KEY ([payment_id]),
  CONSTRAINT student_payment_fk FOREIGN KEY(student_id) REFERENCES students([student_id])
);

INSERT INTO [payments]([payment_id],[student_id],[amount],[payment_date])
VALUES ('P0001', 'S0001', 1250.5, '2023-04-01 '),
	('P0003', 'S0001', 800.4, '2023-04-02 '),
	('P0004', 'S0003', 1000.25, '2023-04-07 '),
	('P0005', 'S0002', 800.4, '2023-04-13 '),
	('P0006', 'S0005', 800.4, '2023-04-14 '),
	('P0007', 'S0003', 1600, '2023-04-16 '),
	('P0008', 'S0003', 800.4, '2023-04-21 '),
	('P0009', 'S0007', 800.4, '2023-04-22 '),
	('P0010', 'S0005', 1250.5, '2023-04-23 '),
	('P0011', 'S0005',1600, '2023-04-24 '),
	('P0012', 'S0009', 1250.5, '2023-04-25 '),
	('P0013', 'S0010', 2050, '2023-04-26 '),
	('P0014', 'S0010', 1725, '2023-04-29 '),
	('P0015', 'S0010', 1350, '2023-05-04 '),
	('P0016', 'S0004', 1250.5, '2023-05-09 '),
	('P0017', 'S0001', 1600, '2023-05-11 '),
	('P0018', 'S0011', 1000.25, '2023-05-15 '),
	('P0019', 'S0011', 750, '2023-05-19 '),
	('P0020', 'S0011', 1725, '2024-04-04 '),
	('P0021', 'S0010', 880.4, '2024-04-07 '),
	('P0022', 'S0010', 1250.5, '2024-04-10 '),
	('P0023', 'S0010', 1600, '2024-04-18 '),
	('P0024', 'S0010', 1450, '2024-04-22 '),
	('P0025', 'S0010', 1250.5, '2024-04-29 '),
	('P0026', 'S0010', 1000.25, '2024-04-30 '),
	('P0027', 'S0010', 750, '2024-05-02 ');

CREATE TABLE [enrollments] (
  [enrollment_id] varchar(5),
  [student_id] varchar(5),
  [course_id] varchar(5),
  [enrollment_date] date,
  CONSTRAINT enrollment_pk PRIMARY KEY ([enrollment_id]),
  CONSTRAINT student_fk FOREIGN KEY (student_id) REFERENCES students([student_id]),
  CONSTRAINT course_fk FOREIGN KEY (course_id) REFERENCES course([course_id])
);

INSERT INTO [enrollments]([enrollment_id],[student_id],[course_id],[enrollment_date])
VALUES ('E0001', 'S0001', 'C0004', '2023-04-01 '),
	('E0002', 'S0001', 'C0001', '2023-04-02 '),
	('E0004', 'S0003', 'C0008', '2023-04-07 '),
	('E0005', 'S0002', 'C0001', '2023-04-13 '),
	('E0007', 'S0005', 'C0001', '2023-04-14 '),
	('E0008', 'S0003', 'C0005', '2023-04-16 '),
	('E0011', 'S0003', 'C0001', '2023-04-21 '),
	('E0012', 'S0007', 'C0001', '2023-04-22 '),
	('E0013', 'S0005', 'C0004', '2023-04-23 '),
	('E0014', 'S0005', 'C0005', '2023-04-24 '),
	('E0015', 'S0009', 'C0004', '2023-04-25 '),
	('E0016', 'S0010', 'C0002', '2023-04-26 '),
	('E0017', 'S0010', 'C0010', '2023-04-29 '),
	('E0018', 'S0010', 'C0003', '2023-05-04 '),
	('E0019', 'S0004', 'C0007', '2023-05-09 '),
	('E0020', 'S0001', 'C0005', '2023-05-11 '),
	('E0021', 'S0011', 'C0008', '2023-05-15 '),
	('E0022', 'S0011', 'C0009', '2023-05-19 '),
	('E0023', 'S0011', 'C0010', '2024-04-04 '),
	('E0024', 'S0010', 'C0001', '2024-04-07 '),
	('E0025', 'S0010', 'C0004', '2024-04-10 '),
	('E0026', 'S0010', 'C0005', '2024-04-18 '),
	('E0027', 'S0010', 'C0006', '2024-04-22 '),
	('E0028', 'S0010', 'C0007', '2024-04-29 '),
	('E0029', 'S0010', 'C0008', '2024-04-30 '),
	('E0030', 'S0010', 'C0009', '2024-05-02 ');
CREATE DATABASE SISDB;

-- For Creating Schemas
USE [SISDB];

CREATE TABLE [students] (
  [student_id] varchar(5),
  [first_name] varchar(255),
  [last_name] varchar(255),
  [date_of_birth] date,
  [email] varchar(255),
  [phone_number] varchar(10),
  CONSTRAINT student_pk PRIMARY KEY ([student_id])
);

CREATE TABLE [teacher] (
  [teacher_id] varchar(5),
  [first_name] varchar(255),
  [last_name] varchar(255),
  [email] varchar(255),
  CONSTRAINT teacher_pk PRIMARY KEY ([teacher_id])
);

CREATE TABLE [course] (
  [course_id] varchar(5),
  [course_name] varchar(255),
  [credits] int,
  [teacher_id] varchar(5),
  CONSTRAINT course_pk PRIMARY KEY ([course_id]),
  CONSTRAINT teacher_fk FOREIGN KEY(teacher_id) REFERENCES teacher([teacher_id])
);

CREATE TABLE [enrollments] (
  [enrollment_id] varchar(5),
  [student_id] varchar(5),
  [course_id] varchar(5),
  [enrollment_date] date,
  CONSTRAINT enrollment_pk PRIMARY KEY ([enrollment_id]),
  CONSTRAINT student_fk FOREIGN KEY (student_id) REFERENCES students([student_id]),
  CONSTRAINT course_fk FOREIGN KEY (course_id) REFERENCES course([course_id])
);

CREATE TABLE [payments] (
  [payment_id] varchar(5),
  [student_id] varchar(5),
  [amount] float,
  [payment_date] date,
  CONSTRAINT payment_pk PRIMARY KEY ([payment_id]),
  CONSTRAINT student_payment_fk FOREIGN KEY(student_id) REFERENCES students([student_id])
);


INSERT INTO [enrollments]([enrollment_id],[student_id],[course_id],[enrollment_date])
VALUES ('E0001','S0002','C0004','2023-10-04'),
		('E0002','S0004','C0003','2024-01-14'),
		('E0003','S0001','C0005','2023-06-22'),
		('E0004','S0007','C0007','2024-04-01'),
		('E0005','S0010','C0002','2023-11-09'),
		('E0006','S0006','C0008','2023-07-15'),
		('E0007','S0009','C0009','2024-02-14'),
		('E0008','S0009','C0002','2024-02-16'),
		('E0009','S0006','C0004','2023-04-25'),
		('E0010','S0006','C0003','2023-09-10');


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
		('S0011','Ketheesa','K','keth6211@gmail.com','2003-06-30','7734644278');

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

INSERT INTO [payments]([payment_id],[student_id],[amount],[payment_date])
VALUES ('P0001','S0003',1350.25,'2023-12-12'),
		('P0002','S0006',900.00,'2023-10-04'),
		('P0003','S0008',1200.72,'2024-01-11'),
		('P0004','S0001',1125.00,'2023-11-05'),
		('P0005','S0005',1350.25,'2023-01-03'),
		('P0006','S0009',1900.15,'2024-03-06'),
		('P0007','S0003',1350.00,'2024-02-21'),
		('P0008','S0007',950.05,'2024-01-28'),
		('P0009','S0008',3050.00,'2023-07-06'),
		('P0010','S0002',1350.14,'2024-03-08')
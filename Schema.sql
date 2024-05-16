IF NOT EXISTS(SELECT * FROM sys.databases WHERE [name]='CarRentalSystem')
	BEGIN
		CREATE DATABASE [CarRentalSystem]
	END
	GO
USE	[CarRentalSystem]
GO

IF OBJECT_ID(N'students') IS NULL
CREATE TABLE [students] (
  [student_id] varchar(10) NOT NULL,
  [first_name] varchar(255),
  [last_name] varchar(255),
  [date_of_birth] date,
  [email] varchar(255),
  [phone_number] varchar(10),
  CONSTRAINT student_pk PRIMARY KEY ([student_id])
);

IF OBJECT_ID(N'teacher') IS NULL
CREATE TABLE [teacher] (
  [teacher_id] varchar(10) NOT NULL,
  [first_name] varchar(255),
  [last_name] varchar(255),
  [email] varchar(255),
  [expertise] varchar(255),
  CONSTRAINT teacher_pk PRIMARY KEY ([teacher_id])
);

IF OBJECT_ID(N'course') IS NULL
CREATE TABLE [course] (
  [course_code] varchar(10) NOT NULL,
  [course_name] varchar(255),
  [credits] int,
  [teacher_id] varchar(10),
  [course_fee] float,
  CONSTRAINT course_pk PRIMARY KEY ([course_code]),
  CONSTRAINT teacher_fk FOREIGN KEY(teacher_id) REFERENCES teacher([teacher_id])
);

IF OBJECT_ID(N'payments') IS NULL
CREATE TABLE [payments] (
  [payment_id] int  NOT NULL IDENTITY(100,1),
  [student_id] varchar(10),
  [amount] float,
  [payment_date] date,
  CONSTRAINT payment_pk PRIMARY KEY ([payment_id]),
  CONSTRAINT student_payment_fk FOREIGN KEY(student_id) REFERENCES students([student_id])
);

IF OBJECT_ID(N'enrollments') IS NULL
CREATE TABLE [enrollments] (
  [enrollment_id] int  NOT NULL IDENTITY(200,1),
  [student_id] varchar(10),
  [course_code] varchar(10),
  [enrollment_date] date,
  CONSTRAINT enrollment_pk PRIMARY KEY ([enrollment_id]),
  CONSTRAINT enrollment_uk UNIQUE([student_id]),
  CONSTRAINT student_fk FOREIGN KEY (student_id) REFERENCES students([student_id]),
  CONSTRAINT course_fk FOREIGN KEY (course_code) REFERENCES course([course_code])
);

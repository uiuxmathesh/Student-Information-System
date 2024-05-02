
--1. Provide a SQL script that initializes the database for the Job Board scenario “CareerHub”
CREATE DATABASE	[CareerHub]
GO
USE	[CareerHub]
GO

--2. . Create tables for Companies, Jobs, Applicants and Applications. 
CREATE TABLE [Companies](
	[CompanyID] int NOT NULL IDENTITY(1,1),
	[CompanyName] varchar(255),
	[Location] varchar(255),
	CONSTRAINT companies_pk PRIMARY KEY ([CompanyID])
);

CREATE TABLE [Jobs](
	[JobID]	int NOT NULL IDENTITY(1,1),
	[CompanyID] int,
	[JobTitle] varchar(255),
	[JobDescription] text,
	[JobLocation] varchar(255),
	[Salary] decimal,
	[JobType] varchar(255),
	[PostedDate] datetime,
	CONSTRAINT job_pk PRIMARY KEY ([JobID]),
	CONSTRAINT job_company_fk FOREIGN KEY ([CompanyID]) REFERENCES Companies([CompanyID])
);

CREATE TABLE [Applicants](
	[ApplicantID] int NOT NULL IDENTITY(1,1),
	[FirstName] varchar(255),
	[LastName] varchar(255),
	[Email] varchar(255),
	[Phone] varchar(255),
	[Resume] text,
	[City] varchar(255),
	[State] varchar(255),
	CONSTRAINT applicants_pk PRIMARY KEY([ApplicantID])
);

CREATE TABLE [Applications](
	[ApplicationID] int NOT NULL IDENTITY(1,1),
	[JobID] int,
	[ApplicantID] int,
	[ApplicationDate] datetime,
	[CoverLetter] text,
	CONSTRAINT applications_pk PRIMARY KEY([ApplicationID]),
	CONSTRAINT application_job_fk FOREIGN KEY ([JobID]) REFERENCES Jobs([JobID]),
	CONSTRAINT application_applicant_fk FOREIGN KEY ([ApplicantID]) REFERENCES Applicants([ApplicantID])

)

--3. Define appropriate primary keys, foreign keys, and constraints.
--All the tables are created with necessary primary keys, foreign keys and constraints

--4. Ensure the script handles potential errors, such as if the database or tables already exist.
--To ensure error handling in such cases we can check the OBJECT_IDs of the tables along with the table creation syntax
--Here's the error  handled code.
IF OBJECT_ID(N'Companies', N'U') IS NULL
CREATE TABLE [Companies](
	[CompanyID] int NOT NULL IDENTITY(1,1),
	[CompanyName] varchar(255),
	[Location] varchar(255),
	CONSTRAINT companies_pk PRIMARY KEY ([CompanyID])
);

IF OBJECT_ID(N'Jobs', N'U') IS NULL
CREATE TABLE [Jobs](
	[JobID]	int NOT NULL IDENTITY(1,1),
	[CompanyID] int,
	[JobTitle] varchar(255),
	[JobDescription] text,
	[JobLocation] varchar(255),
	[Salary] decimal,
	[JobType] varchar(255),
	[PostedDate] datetime,
	CONSTRAINT job_pk PRIMARY KEY ([JobID]),
	CONSTRAINT job_company_fk FOREIGN KEY ([CompanyID]) REFERENCES Companies([CompanyID])
);

IF OBJECT_ID(N'Applicants', N'U') IS NULL
CREATE TABLE [Applicants](
	[ApplicantID] int NOT NULL IDENTITY(1,1),
	[FirstName] varchar(255),
	[LastName] varchar(255),
	[Email] varchar(255),
	[Phone] varchar(255),
	[Resume] text,
	[City] varchar(255),
	[State] varchar(255),
	CONSTRAINT applicants_pk PRIMARY KEY([ApplicantID])
);

IF OBJECT_ID(N'Applications', N'U') IS NULL
CREATE TABLE [Applications](
	[ApplicationID] int NOT NULL IDENTITY(1,1),
	[JobID] int,
	[ApplicantID] int,
	[ApplicationDate] datetime,
	[CoverLetter] text,
	CONSTRAINT applications_pk PRIMARY KEY([ApplicationID]),
	CONSTRAINT application_job_fk FOREIGN KEY ([JobID]) REFERENCES Jobs([JobID]),
	CONSTRAINT application_applicant_fk FOREIGN KEY ([ApplicantID]) REFERENCES Applicants([ApplicantID])

)

--Inserting Records
INSERT INTO Companies (CompanyName, Location) VALUES
('Tech Innovations', 'San Francisco'),
('Data Driven Inc', 'New York'),
('GreenTech Solutions', 'Austin'),
('CodeCrafters', 'Boston'),
('HexaWare Technologies', 'Chennai');


INSERT INTO Jobs (CompanyID, JobTitle, JobDescription, JobLocation, Salary, JobType, PostedDate) VALUES
(1, 'Frontend Developer', 'Develop user-facing features', 'San Francisco', 75000, 'Full-time', '2023-01-10'),
(2, 'Data Analyst', 'Interpret data models', 'New York', 68000, 'Full-time', '2023-02-20'),
(3, 'Environmental Engineer', 'Develop environmental solutions', 'Austin', 85000, 'Full-time', '2023-03-15'),
(1, 'Backend Developer', 'Handle server-side logic', 'Remote', 77000, 'Full-time', '2023-04-05'),
(4, 'Software Engineer', 'Develop and test software systems', 'Boston', 90000, 'Full-time', '2023-01-18'),
(5, 'HR Coordinator', 'Manage hiring processes', 'Chennai', 45000, 'Contract', '2023-04-25'),
(2, 'Senior Data Analyst', 'Lead data strategies', 'New York', 95000, 'Full-time', '2023-01-22');


INSERT INTO Applicants (FirstName, LastName, Email, Phone, Resume, City, State) VALUES
('John', 'Doe', 'john.doe@example.com', '123-456-7890', 'Experienced web developer with 5 years of experience.', 'San Francisco', 'California'),
('Jane', 'Smith', 'jane.smith@example.com', '234-567-8901', 'Data enthusiast with 3 years of experience in data analysis.', 'New York', 'USA'),
('Alice', 'Johnson', 'alice.johnson@example.com', '345-678-9012', 'Environmental engineer with 4 years of field experience.', 'Austin', 'Texas'),
('Bob', 'Brown', 'bob.brown@example.com', '456-789-0123', 'Seasoned software engineer with 8 years of experience.','Chennai', 'Tamilnadu');


INSERT INTO Applications (JobID, ApplicantID, ApplicationDate, CoverLetter) VALUES
(1, 1, '2023-04-01', 'I am excited to apply for the Frontend Developer position.'),
(2, 2, '2023-04-02', 'I am interested in the Data Analyst position.'),
(3, 3, '2023-04-03', 'I am eager to bring my expertise to your team as an Environmental Engineer.'),
(4, 4, '2023-04-04', 'I am applying for the Backend Developer role to leverage my skills.'),
(5, 1, '2023-04-05', 'I am also interested in the Software Engineer position at CodeCrafters.');

--5. Write an SQL query to count the number of applications received for each job listing in the "Jobs" table. Display the job title and the corresponding application count. Ensure that it lists all
--jobs, even if they have no applications.

SELECT	j.JobID,j.JobTitle,COUNT(a.ApplicantID) AS [Applications Recieved]
FROM	[Jobs] j
		LEFT JOIN	[Applications] a
ON		j.JobID = a.JobID
GROUP BY j.JobID, j.JobTitle

--6. Develop an SQL query that retrieves job listings from the "Jobs" table within a specified salary range. Allow parameters for the minimum and maximum salary values. 
--Display the job title, company name, location, and salary for each matching job.

-- Parameters for minimum and maximum salary
DECLARE @minimumSalary decimal = 40000;
DECLARE @maximumSalary decimal = 60000;


SELECT	j.JobTitle,
		c.CompanyName,
		c.Location,
		j.Salary
FROM	[Jobs] j
		INNER JOIN [Companies] c
ON		j.CompanyID = c.CompanyID
WHERE	j.Salary BETWEEN @minimumSalary AND @maximumSalary

--7. Write an SQL query that retrieves the job application history for a specific applicant. Allow a parameter for the ApplicantID, and return a result set with the 
--job titles, company names, and application dates for all the jobs the applicant has applied to

DECLARE @ApplicantId int = 1;


SELECT	c.CompanyName,
		a.JobTitle,
		a.ApplicationDate
FROM	[Companies] c
		INNER JOIN (
		SELECT	j.CompanyID,
				j.JobTitle,
				a.ApplicationDate
		FROM	[Jobs] j
				INNER JOIN (
				SELECT	b.JobID,
						b.ApplicationDate
				FROM	[Applicants] a
						INNER JOIN [Applications] b
				ON		a.ApplicantID = b.ApplicantID
				WHERE	a.ApplicantID = @ApplicantId
				) a
		ON j.JobID = a.JobID
		) a
ON		c.CompanyID = a.CompanyID

--8. Create an SQL query that calculates and displays the average salary offered by all companies for
--job listings in the "Jobs" table. Ensure that the query filters out jobs with a salary of zero

SELECT	c.CompanyID,
		c.CompanyName,
		AVG(j.Salary) AS [Average Salary Offered]
FROM	[Companies] c 
		INNER JOIN [Jobs] j
ON		c.CompanyID = j.CompanyID
GROUP BY c.CompanyID,c.CompanyName

--9. Write an SQL query to identify the company that has posted the most job listings. Display the
--company name along with the count of job listings they have posted. Handle ties if multiple
--companies have the same maximum count

SELECT	c.CompanyName,
		j.Job_Count
FROM	[Companies] c 
		INNER JOIN(
			SELECT	CompanyID,
					COUNT(JobID) AS Job_Count
			FROM	[Jobs] a
			GROUP BY [CompanyID]
			ORDER BY [Job_Count] DESC
			OFFSET 0 ROWS
			FETCH NEXT 1 ROWS ONLY
		) j
ON		c.CompanyID = j.CompanyID

--10. Find the applicants who have applied for positions in companies located in 'CityX' and have at least 3 years of experience.
DECLARE @city varchar(255) = 'New York'

SELECT a.ApplicantID,
		a.FirstName,
		a.LastName,
		b.CompanyName,
		b.CompanyName,
		b.Location
FROM [Applicants] a
		INNER JOIN(
		SELECT	a.ApplicantID,
				a.JobID,
				c.JobTitle,
				c.JobDescription,
				c.CompanyName,
				c.location
		FROM	[Applications] a 
		INNER JOIN(
				SELECT	c.CompanyID,
						c.CompanyName,
						c.Location,
						j.JobID,
						j.JobTitle,
						j.JobDescription
				FROM	[jobs] j 
						INNER JOIN(
							SELECT	[CompanyID],
									[CompanyName],
									[Location]
							FROM	[Companies]
							WHERE	[Location] = @city
						) c
				ON		j.CompanyID = c.CompanyID
		) c
		ON		a.JobID = c.JobID		
		) b
ON		a.ApplicantID = b.ApplicantID;

-- 11. Retrieve a list of distinct job titles with salaries between $60,000 and $80,000.

SELECT DISTINCT [JobTitle]
FROM [Jobs]
WHERE [Salary] BETWEEN 60000 AND 80000

--12. Find the jobs that have not received any applications.

SELECT	* 
FROM	[JOBS]
WHERE	[JobID] 
		NOT IN (
			SELECT	[JobID]
			FROM	[Applications]
)

--13. . Retrieve a list of job applicants along with the companies they have applied to and the positions they have applied for.


SELECT	j.ApplicantID,
		j.FirstName,
		j.LastName,
		j.JobTitle,
		c.CompanyName
FROM	[Companies] c
		INNER JOIN(
		SELECT	a.*,
				j.JobTitle,
				j.CompanyID
		FROM	[Jobs] j
				INNER JOIN(
				SELECT	a.JobID,
						a.ApplicantID,
						b.FirstName,
						b.LastName
				FROM	[Applications] a
						INNER JOIN [Applicants] b
				ON		a.ApplicantID = b.ApplicantID
						)a
		ON		a.JobID = j.JobID
		)  j
ON		c.CompanyID = j.CompanyID

--  14. Retrieve a list of companies along with the count of jobs they have posted, even if they have not received any applications.

SELECT	*
FROM	[Companies] c 
		INNER JOIN(
			SELECT	j.CompanyID, 
					COUNT(j.JobID) AS Job_Count
			FROM	[Jobs] j 
					LEFT JOIN [Applications] a
			ON		j.JobID = a.JobID
			WHERE	a.ApplicantID IS NULL
			GROUP BY j.CompanyID
) j
ON		c.CompanyID = j.CompanyID

--15. List all applicants along with the companies and positions they have applied for, including those who have not applied.
--For Checking
INSERT INTO [Applicants] ( FirstName, LastName, Email, Phone, Resume, City, State)
VALUES ('Mathesh','Premkumar','matheshpremkumar@gmail.com','9922299222','Experienced web developer with 5 years of experience.','Chennai','Tamilnadu')

--Actual Query
SELECT	j.ApplicantID,
		j.FirstName,
		j.LastName,
		j.JobTitle,
		c.CompanyName
FROM	[Companies] c
		RIGHT JOIN(
		SELECT	a.*,
				j.JobTitle,
				j.CompanyID
		FROM	[Jobs] j
				RIGHT JOIN(
				SELECT	a.JobID,
						a.ApplicantID,
						b.FirstName,
						b.LastName
				FROM	[Applications] a
						RIGHT JOIN [Applicants] b
				ON		a.ApplicantID = b.ApplicantID
						)a
		ON		a.JobID = j.JobID
		)  j
ON		c.CompanyID = j.CompanyID;



--16. Find companies that have posted jobs with a salary higher than the average salary of all jobs.


SELECT	*
FROM	[Companies] c 
		INNER JOIN [Jobs] j
ON		c.CompanyID = j.CompanyID
WHERE	j.Salary > (
					SELECT	AVG(j.Salary) AS [Average Salary Offered]
					FROM	[Companies] c 
							INNER JOIN [Jobs] j
					ON		c.CompanyID = j.CompanyID
					);

--17. Display a list of applicants with their names and a concatenated string of their city and state.
SELECT	[FirstName],
		[LastName],
		CONCAT(city,' ',state) AS [Location]
FROM	[Applicants];

--18. Retrieve a list of jobs with titles containing either 'Developer' or 'Engineer'

SELECT	*
FROM	[Jobs]
WHERE	[JobTitle] IN('%Developer%') OR [JobTitle] LIKE('%Engineer%');

--19. Retrieve a list of applicants and the jobs they have applied for, including those who have not applied and jobs without applicants.

SELECT	a.ApplicantID,
		a.FirstName,
		a.LastName,
		c.JobID
FROM	[Applicants] a
		LEFT JOIN (
		SELECT	a.*,
				b.ApplicantID
		FROM	[Jobs] a
				LEFT JOIN [Applications] b
		ON		a.JobID = b.JobID
		) c
ON		a.ApplicantID = c.ApplicantID
UNION
SELECT	a.ApplicantID,
		a.FirstName,
		a.LastName,
		b.JobID
FROM	[Jobs] b
		LEFT JOIN(
		SELECT a.ApplicantID,
			   a.Firstname,
			   a.LastName,
			   b.JobID
		FROM	[Applicants] a
				LEFT JOIN[Applications] b
		ON		a.ApplicantID = b.ApplicantID
		)a
ON		a.JobID = b.JobID

--20. List all combinations of applicants and companies where the company is in a specific city and the applicant has more than 2 years of experience. For example: city=Chennai



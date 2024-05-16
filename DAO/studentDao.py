from datetime import datetime
from Exceptions.custom_exceptions import *
import pyodbc
from Util import DBConnUtil

class StudentDao(DBConnUtil):

    def addStudent(self,student): # WORKING GOOD AS EXPECTED
        query = "INSERT INTO students ([student_id], [first_name], [last_name], [date_of_birth], [email], [phone_number]) VALUES (?, ?, ?, ?, ?, ?)"
        values = (student.studentId, student.fname, student.lname, student.dob, student.email, student.phone)
        try:
            self.cursor.execute(query, values)
        except pyodbc.IntegrityError as e:
            self.cursor.commit()
            print(f"Student ID {student.studentId} already exists. Please enter a different Student ID.")
        else:
            self.cursor.commit()
            print("Student added successfully")

    def enrollInCourse(self,student, course): # WORKING GOOD AS EXPECTED

        # Preparing the query and values
        query = "INSERT INTO enrollments ([student_id], [course_code], [enrollment_date]) VALUES (?, ?, ?)"
        values = (student.studentId, course.code, str(datetime.now().date().strftime('%Y-%m-%d')))

        try:
            self.cursor.execute(query, values)

        # Handling the exception if the student is already enrolled in the course
        except pyodbc.IntegrityError as e:
            self.cursor.commit()
            raise DuplicateEnrollmentException(f"Student {student.studentId} is already enrolled in course {course.code}.")
        
        # If the enrollment is successful, fetching the enrollment ID
        else:
            print("Student enrolled successfully")
            query = "SELECT IDENT_CURRENT('enrollments') AS ['id']"
            self.cursor.execute(query)
            enrollmentId = int(self.cursor.fetchone()[0])
            self.cursor.commit()
            return enrollmentId
            
            

    def updateStudentInfo(self,student): # WORKING GOOD AS EXPECTED
        if self.displayStudentInfo(student) == []:
            raise InvalidStudentDataException(f"Invalid Student ID {student.studentId}. Please enter a valid Student ID.")
        query ="UPDATE students SET [first_name] = ?, [last_name] = ?, [date_of_birth] = ?, [email] = ?, [phone_number] = ? WHERE [student_id] = ?"
        values = (student.fname, student.lname, student.dob, student.email, student.phone, student.studentId)
        self.cursor.execute(query, values)
        self.cursor.commit()
        print("Student information updated successfully")

    def makePayment(self,studentId,amount:float, paymentDate:str): # WORKING GOOD AS EXPECTED

        # Preparing the query and values
        
        query = "INSERT INTO payments ([student_id], [amount], [payment_date]) VALUES (?, ?, ?)"
        values = (studentId, amount, paymentDate)

        # Executing the query
        try:
            self.cursor.execute(query, values)

        # Handling the exception if the student ID is invalid
        except pyodbc.IntegrityError as e:
            self.cursor.commit()
            raise StudentNotFoundException(f"Invalid Student ID {studentId}. Please enter a valid Student ID.") 
        
        # If the payment is successful, fetching the payment ID
        else:
            print("Payment made successfully")
            query = "SELECT IDENT_CURRENT('payments') AS ['id']"
            self.cursor.execute(query)  
            paymentId = int(self.cursor.fetchone()[0])
            self.cursor.commit()
            return paymentId
            

    def displayStudentInfo(self,student): # WORKING GOOD AS EXPECTED
        query = "SELECT * FROM students WHERE [student_id] = ?"
        values = (student.studentId)
        self.cursor.execute(query, values)
        studentInfo = self.cursor.fetchone()
        if studentInfo == None:
            raise StudentNotFoundException(f"Student ID {student.studentId} not found. Please enter a valid Student ID.")
        header = self.cursor.description
        header = tuple(column[0] for column in header)
        studentInfo = [header, studentInfo]
        return studentInfo

    def getEnrolledCourses(self,student): # WORKING GOOD AS EXPECTED
        query = """
                SELECT	students.student_id AS enrollment_id,
                        CONCAT(students.first_name,' ',students.last_name) AS students_name,
                        course.course_code,
                        course.course_name,
                        course.course_fee,
                        course.credits,
                        teacher.teacher_id,
                        CONCAT(teacher.first_name,' ',teacher.last_name) AS teacher_name
                FROM	[course]
                        INNER JOIN [enrollments] ON course.course_code = enrollments.course_code
                        INNER JOIN [students] ON students.student_id = enrollments.student_id
                        INNER JOIN [teacher] ON teacher.teacher_id = course.teacher_id
                WHERE	students.student_id = ?
                """
        values = student.studentId
        self.cursor.execute(query, values)
        enrolledCourses = self.cursor.fetchall()
        headers =  self.cursor.description
        headers = tuple(header[0] for header in headers)
        enrolledCourses = [headers, *enrolledCourses]
        return enrolledCourses

    def getPaymentHistory(self,student):  # WORKING GOOD AS EXPECTED
        query = "SELECT * FROM payments WHERE [student_id] = ?"
        values = (student.studentId)
        self.cursor.execute(query, values)
        payments = self.cursor.fetchall()
        headers =  self.cursor.description
        headers = tuple(header[0] for header in headers)
        payments = [headers, *payments]
        return payments



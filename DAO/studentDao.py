from datetime import datetime
from Model import *
from Exceptions.custom_exceptions import *
import pyodbc
from .courseDao import CourseDao
from Util import DBConnUtil

class StudentDao:

    def enrollInCourse(self,student:Student, course:Course): # WORKING GOOD AS EXPECTED

        # Preparing the query and values
        query = "INSERT INTO enrollments ([student_id], [course_code], [enrollment_date]) VALUES (?, ?, ?)"
        values = (student.studentId, course.code, str(datetime.now().date().strftime('%Y-%m-%d')))

        # Initializing the enrollment object and courseDao object
        enrollment = None
        courseDao = CourseDao()

        # Checking if the student and course exist in the database
        if self.displayStudentInfo(student) == []:
            raise InvalidStudentDataException(f"Invalid Student ID {student.studentId}. Please enter a valid Student ID.")
        elif courseDao.displayCourseInfo(course) == []:
            raise InvalidCourseDataException(f"Invalid Course Code {course.code}. Please enter a valid Course Code.")
        
        # If exists Inserting the enrollment into the database
        try:
            self.connection = DBConnUtil.getConnection()
            self.cursor = self.connection.cursor()
            self.cursor.execute(query, values)

        # Handling the exception if the student is already enrolled in the course
        except pyodbc.IntegrityError as e:
            self.cursor.commit()
            self.cursor.close()
            raise DuplicateEnrollmentException(f"Student {student.studentId} is already enrolled in course {course.code}.")
        
        # If the enrollment is successful, fetching the enrollment ID
        else:
            print("Student enrolled successfully")
            query = "SELECT IDENT_CURRENT('enrollments') AS ['id']"
            self.cursor.execute(query)
            enrollmentId = int(self.cursor.fetchone()[0])
            enrollment = Enrollment()
            enrollment.enrollmentId = enrollmentId
            enrollment.studentId = student.studentId
            enrollment.courseId = course.code
            self.cursor.commit()
            self.cursor.close()
            self.connection =  DBConnUtil.closeConnection()#After Implementing the method, close the connection
            return enrollment
        # Committing the changes and closing the cursor
            
            

    def updateStudentInfo(self,student): # WORKING GOOD AS EXPECTED
        if self.displayStudentInfo(student) == []:
            raise InvalidStudentDataException(f"Invalid Student ID {student.studentId}. Please enter a valid Student ID.")
        self.connection = DBConnUtil.getConnection()
        self.cursor = self.connection.cursor()
        query ="UPDATE students SET [first_name] = ?, [last_name] = ?, [date_of_birth] = ?, [email] = ?, [phone_number] = ? WHERE [student_id] = ?"
        values = (student.fname, student.lname, student.dob, student.email, student.phone, student.studentId)
        self.cursor.execute(query, values)
        self.cursor.commit()
        self.cursor.close()
        self.connection = DBConnUtil.closeConnection()   #After Implementing the method, close the connection        

    def makePayment(self,studentId,amount:float, paymentDate:str): # WORKING GOOD AS EXPECTED

        # Preparing the query and values
        query = "INSERT INTO payments ([student_id], [amount], [payment_date]) VALUES (?, ?, ?)"
        values = (studentId, amount, paymentDate)

        # Initializing the payment object
        payment = None

        # Executing the query
        try:
            self.connection = DBConnUtil.getConnection()
            self.cursor = self.connection.cursor()
            self.cursor.execute(query, values)

        # Handling the exception if the student ID is invalid
        except pyodbc.IntegrityError as e:
            self.cursor.commit()
            self.cursor.close()
            raise InvalidStudentDataException(f"Invalid Student ID {studentId}. Please enter a valid Student ID.") 
        
        # If the payment is successful, fetching the payment ID
        else:
            print("Payment made successfully")
            query = "SELECT IDENT_CURRENT('payments') AS ['id']"
            self.cursor.execute(query)  
            paymentId = int(self.cursor.fetchone()[0])
            self.cursor.commit()
            self.cursor.close() 
            self.connection = DBConnUtil.closeConnection()
            payment = Payment()
            payment.paymentId = paymentId
            payment.studentId = studentId
            payment.amount = amount
            payment.paymentDate = paymentDate
            return payment
            

    def displayStudentInfo(self,student): # WORKING GOOD AS EXPECTED
        self.connection = DBConnUtil.getConnection()
        self.cursor = self.connection.cursor()
        query = "SELECT * FROM students WHERE [student_id] = ?"
        values = (student.studentId)
        self.cursor.execute(query, values)
        studentInfo = self.cursor.fetchall()
        self.cursor.close()
        self.connection = DBConnUtil.closeConnection()
        return studentInfo

    def getEnrolledCourses(self,student): # WORKING GOOD AS EXPECTED
        self.connection = DBConnUtil.getConnection()
        self.cursor = self.connection.cursor()
        query = "SELECT * FROM enrollments WHERE [student_id] = ?"
        values = (student.studentId)
        self.cursor.execute(query, values)
        enrolledCourses = self.cursor.fetchall()
        self.cursor.close()
        self.connection = DBConnUtil.closeConnection()
        return enrolledCourses

    def getPayments(self,student):  # WORKING GOOD AS EXPECTED
        self.connection = DBConnUtil.getConnection()
        self.cursor = self.connection.cursor()
        query = "SELECT * FROM payments WHERE [student_id] = ?"
        values = (student.studentId)
        self.cursor.execute(query, values)
        payments = self.cursor.fetchall()
        self.cursor.close()
        self.connection = DBConnUtil.closeConnection()
        return payments



from datetime import datetime
from Exceptions.custom_exceptions import *
import pyodbc
from Util import DBConnUtil

class StudentDao(DBConnUtil):

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
        return studentInfo

    def getEnrolledCourses(self,student): # WORKING GOOD AS EXPECTED
        query = "SELECT * FROM enrollments WHERE [student_id] = ?"
        values = (student.studentId)
        self.cursor.execute(query, values)
        enrolledCourses = self.cursor.fetchall()
        return enrolledCourses

    def getPayments(self,student):  # WORKING GOOD AS EXPECTED
        query = "SELECT * FROM payments WHERE [student_id] = ?"
        values = (student.studentId)
        self.cursor.execute(query, values)
        payments = self.cursor.fetchall()
        return payments



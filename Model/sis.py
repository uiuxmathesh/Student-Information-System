from .course import Course
from .student import Student
from .enrollment import Enrollment
from .payment import Payment
from .teacher import Teacher
from DAO import *
from datetime import datetime
from Exceptions.custom_exceptions import *

class SIS:

    def __init__(self):
        self.students = Student()
        self.courses = Course()
        self.teachers = Teacher()
        self.enrollments = Enrollment()
        self.payments = Payment()

    def enrollStudentInCourse(self, student:Student, course:Course):
        service = StudentDao()
        try:
            enrollment = service.enrollInCourse(student, course)
        except Exception as e:
            print(e)
        else:
            Student.enrollments(enrollment)
            Course.enrollments(enrollment)
              # Implementing class-level data structure to store enrollments

    def assignTeacherToCourse(self, teacher:Teacher, course:Course):
        service = CourseDao()
        try:
            service.assignTeacher(teacher, course)
        except Exception as e:
            print(e)
        else:
            pass # Implementing class-level data structure to store teacher assignments

    def recordPayment(self, studentId:str, amount:float, paymentDate:str):
        service = StudentDao()
        try:
            if amount <= 0:
                raise PaymentValidationException("Payment amount must be greater than 0.")
            elif paymentDate > str(datetime.now().date()):
                raise PaymentValidationException("Payment date cannot be in the future.")
            payment = service.makePayment(studentId, amount, paymentDate)
        except Exception as e:
            print(e)
        else:
            pass # Implementing class-level data structure to store payments    
        

    def getEnrollmentReport(self, student:Student):
        pass

    def getPaymentReport(self, student:Student):
        pass

    def calculateCourseStatistics(self, course:Course):
        pass
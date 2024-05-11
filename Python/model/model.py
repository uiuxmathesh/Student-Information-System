from datetime import datetime
from pprint import pprint as print
from exceptions import custom_exceptions as e


#1 
class Teacher:

    def __init__(self, teacherId:int, fname:str, lname:str, email:str):
        self.teacherId = teacherId
        self.fname = fname
        self.lname = lname
        self.email = email
        self.course = None

    # def update_teacher_info(self, teacherId:int, fname:str, lname:str, email:str):
    #     self.teacherId = teacherId
    #     self.fname = fname
    #     self.lname = lname
    #     self.email = email

    # def display_teacher_info(self):
    #     print(f'Teacher Id: {self.teacherId}, First name: {self.fname}, Last name: {self.lname}, Email: {self.email}')

    # def set_assigned_course(self, course):
    #     self.course = course
    
    # def get_assigned_course(self):
    #     return self.course

#2
class Course:

    def __init__(self, courseId:int, name:str, code:str, instructor_name:str):
        self.courseId = courseId
        self.name = name
        self.code = code
        self.instructor_name = instructor_name
        self.enrollments = None
    
    
    # def assign_teacher(self, teacher:Teacher):
    #     self.teacher = teacher
    
    # def update_course_info(self,courseCode:str, courseName:str, instructorName:str):
    #     self.code = courseCode
    #     self.name = courseName
    #     self.instructor_name = instructorName

    # def display_course_info(self):
    #     print(f'Course ID: { self.courseId}, Course Name: { self.name}, Course Code: {self.code}, Instructor Name: {self.instructor_name}')

    # def set_enrollments(self,enrollment):
    #     self.enrollments.add(enrollment)

    # def get_enrollments(self):
    #     return self.enrollments

    # def get_Teacher(self):
    #     self.teacher.display_teacher_info()
    


# 3
class Student:
    
    
    def __init__(self, studentId:int, fname:str, lname:str, dob:datetime, email:str, phone:str):
        self.studentId = studentId
        self.fname = fname
        self.lname = lname
        self.dob = datetime.strptime(dob, '%d-%m-%Y').date()
        self.email = email
        self.phone = phone
        self.payment_history = []
        self.enrollments = set()

    def enroll_in_course(self,course:Course):
        if course in self.enrollments:
            raise e.DuplicateEnrollmentException(f"Already enrolled in the {course} course.")
        try:
            self.enrollments.add(course)
        except e.DuplicateEnrollmentException as err:
            print(f"Invalid Enrollment: {err}")
        

    # def update_student_info(self, studentId:int, fname:str, lname:str, dob:datetime, email:str, phone:str):
    #     self.studentId = studentId
    #     self.fname = fname
    #     self.lname = lname
    #     self.dob = dob
    #     self.email = email
    #     self.phone = phone

    # def make_payment(self, amount:int, paymentDate:datetime):
    #     self.payment_history.append({"amount":amount, "paymentDate":paymentDate})
    
    # def display_student_info(self):
    #     print(f"First name:{self.fname}, Last name:{self.lname}, Date of birth:{self.dob}, Email:{self.email}, Phone Number:{self.phone}")

    # def get_enrolled_courses(self):
    #     try:
    #         return self.enrollments
    #     except NameError as e:
    #         print(f'No courses enrolled. {e}')
    #     else:
    #         print('----------------')
    #     finally:
    #         return
        
    # def get_payment_history(self):
        try:
            return self.payment_history
        except NameError as e:
            print(f'No payment has been made. {e}')
        else:
            print('----------------')
        finally:
            return
        


#4
class Payment:
    def __init__(self, paymentId:int, studentId:int, amount:int, paymentDate:datetime):
        self.paymentId = paymentId
        self.studentId = studentId
        self.amount = amount
        self.paymentDate = datetime.strptime(paymentDate, "%d-%m-%Y").date()

    # def set_student(self, student:Student):
    #     self.student = Student

    # def get_student(self):
    #     return self.student
    
    # def get_payment_amount(self):
    #     return self.amount
    
    # def get_payment_date(self):
    #     return self.paymentDate
    
#5
class Enrollment:

    def __init__(self, enrollmentId:int, studentId:int, courseId:int, enrollmentDate:datetime):
        self.enrollmentId = enrollmentId
        self.studentId = studentId
        self.courseId = courseId
        self.enrollmentDate = datetime.strptime(enrollmentDate, "%d-%m-%Y").date()

    # def set_student(self, student:Student):
    #     self.student = student

    # def get_student(self):
    #     return self.student
    
    # def set_course(self,course:Course):
    #     self.course = course
    
    # def get_course(self):
    #     return self.course
    
    # def display_enrollment(self):
    #     print(f'Enrollment ID: {self.enrollmentId}, Student ID: {self.studentId}, Course ID: {self.courseId}, Date Enrolled: {self.enrollmentDate}')


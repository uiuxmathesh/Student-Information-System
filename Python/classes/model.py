from datetime import datetime
from pprint import pprint as print


#1 
class Teacher:

    def __init__(self, teacherId:int, fname:str, lname:str, email:str):
        self.__teacherId = teacherId
        self.__fname = fname
        self.__lname = lname
        self.__email = email

    def update_teacher_info(self, teacherId:int, fname:str, lname:str, email:str):
        self.__teacherId = teacherId
        self.__fname = fname
        self.__lname = lname
        self.__email = email

    def display_teacher_info(self):
        print(f'Teacher Id: {self.__teacherId}, First name: {self.__fname}, Last name: {self.__lname}, Email: {self.__email}')

#2
class Course:

    def __init__(self, courseId:int, name:str, code:str, instructor_name:str):
        self.__courseId = courseId
        self.__name = name
        self.__code = code
        self.__instructor_name = instructor_name
        self.__enrollments = []
    
    def assign_teacher(self, teacher:Teacher):
        self._teacher = teacher
    
    def update_course_info(self,courseCode:str, courseName:str, instructorName:str):
        self.__code = courseCode
        self.__name = courseName
        self.__instructor_name = instructorName

    def display_course_info(self):
        print(f'Course ID: { self.__courseId}, Course Name: { self.__name}, Course Code: {self.__code}, Instructor Name: {self.__instructor_name}')

    def get_enrollments(self):
        return self.__enrollments

    def get_Teacher(self):
        self._teacher.display_teacher_info()
    


# 3
class Student:

    def __init__(self, studentId:int, fname:str, lname:str, dob:datetime, email:str, phone:str):
        self.__studentId = studentId
        self.__fname = fname
        self.__lname = lname
        self.__dob = datetime.strptime(dob, '%d-%m-%Y').date()
        self.__email = email
        self.__phone = phone
        self.__payment_history = []

    def enroll_in_course(self,course:Course):
        self.__enrolled_courses.append(course)
        course.__enrollments.append(self)

    def update_student_info(self, studentId:int, fname:str, lname:str, dob:datetime, email:str, phone:str):
        self.__studentId = studentId
        self.__fname = fname
        self.__lname = lname
        self.__dob = dob
        self.__email = email
        self.__phone = phone

    def make_payment(self, amount:int, paymentDate:datetime):
        self.__payment_history.append({"amount":amount, "paymentDate":paymentDate})
    
    def display_student_info(self):
        print(f"First name:{self.__fname}, Last name:{self.__lname}, Date of birth:{self.__dob}, Email:{self.__email}, Phone Number:{self.__phone}")

    def get_enrolled_courses(self):
        try:
            return self.__enrolled_courses
        except NameError as e:
            print(f'No courses enrolled. {e}')
        else:
            print('----------------')
        finally:
            return
        
    def get_payment_history(self):
        try:
            return self.__payment_history
        except NameError as e:
            print(f'No payment has been made. {e}')
        else:
            print('----------------')
        finally:
            return
        


#4
class Payment:
    def __init__(self, paymentId:int, studentId:int, amount:int, paymentDate:datetime):
        self.__paymentId = paymentId
        self.__studentId = studentId
        self.__amount = amount
        self.__paymentDate = datetime.strptime(paymentDate, "%d-%m-%Y").date()

    def get_student(self):
        return self.__studentId
    
    def get_payment_amount(self):
        return self.__amount
    
    def get_payment_date(self):
        return self.__paymentDate
    
#5
class Enrollment:

    def __init__(self, enrollmentId:int, studentId:int, courseId:int, enrollmentDate:datetime):
        self.__enrollmentId = enrollmentId
        self.__studentId = studentId
        self.__courseId = courseId
        self.__enrollmentDate = datetime.strptime(enrollmentDate, "%d-%m-%Y").date()

    def get_student(self):
        return self.__studentId
    
    def get_course(self):
        return self.__courseId
    
    def display_enrollment(self):
        print(f'Enrollment ID: {self.__enrollmentId}, Student ID: {self.__studentId}, Course ID: {self.__courseId}, Date Enrolled: {self.__enrollmentDate}')


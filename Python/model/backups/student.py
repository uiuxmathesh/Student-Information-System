from datetime import datetime
from pprint import pprint as print
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
        
s1 = Student(1,"Mathesh","P","21-01-2003","mathesh078@gmail.com","7789511247")

s1.display_student_info()

s1.get_enrolled_courses()
s1.get_payment_history()

s1.make_payment(2000, datetime.now().date())
payments_history = s1.get_payment_history()


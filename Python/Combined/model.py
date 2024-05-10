from datetime import datetime

# from pprint import pprint as print
from StudentServices import *

# from exceptions import custom_exceptions as e


# 1
class Teacher:

    def __init__(
        self, teacherId: int, fname: str = None, lname: str = None, email: str = None
    ):
        self.teacherId = teacherId
        self.fname = fname
        self.lname = lname
        self.email = email
        self.course = None

    
    @staticmethod
    def teacherMenu():
        """
        Catalog for Teacher operations
        """
        while True:
            choice = int(
                input(
        """
        *********Teacher Menu*********
        1. Create Teacher Record
        2. Update Teacher Record
        3. Display Teacher Information
        4. Display Assigned courses
        5. Go to Main menu
        *********T********************             
        Please select a option to continue...  """
                )
            )

            if choice == 1:
                print("Kindly provide the Teacher details")
                id = input("Teacher ID: ")
                fname = input("First name: ")
                lname = input("Last name: ")
                email = input("Email: ")
                print("Creating new Teacher Record.....")
                print(" ")
                print(" ")
                teacher = Teacher(id, fname, lname, email)
                teacherService = TeacherService()
                try:
                    teacherService.create_teacher(teacher)
                except Exception as err:
                    print(f"Unable to insert new record: {err}")
                else:
                    print("Successfully Inserted new Record")
                finally:
                    print("Returning to Teacher's menu....")

            elif choice == 2:
                print("Kindly provide the Updated Teacher details")
                id = input("Teacher ID: ")
                fname = input("First name: ")
                lname = input("Last name: ")
                email = input("Email: ")
                print("Updating Teacher Record.....")
                print(" ")
                print(" ")
                teacher = Teacher(id, fname, lname, email)
                teacherService = TeacherService()
                try:
                    teacherService.update_teacher(teacher)
                except Exception as err:
                    print(f"Unable to insert new record: {err}")
                else:
                    print("Successfully Inserted new Record")
                finally:
                    print("Returning to Teacher's menu....")

            elif choice == 3:
                print("Display student Information")
                id = input("Enter Student-ID: ")
                teacher = Teacher(id)
                teacherService = TeacherService()
                teacherService.display_teacher_info(teacher)

            elif choice == 4:
                print("Assigned Course for a Teacher")
                teacherId = input("Teacher ID: ")
                teacher = Teacher(teacherId)
                teacherService = TeacherService()
                teacherService.get_assigned_courses(teacher)

            elif choice == 5:
                print("Returning to Main Menu......")
                break


# 2


class Course:

    def __init__(
        self,
        courseId: str,
        name: str = None,
        credit: int = None,
        teacher_id: str = None,
    ):
        self.courseId = courseId
        self.name = name
        self.credit = credit
        self.teacher_id = teacher_id
        self.enrollments = None

    @staticmethod
    def courseMenu():
        """
        Catalog for Course operations
        """
        while True:
            choice = int(
                input(
        """
        *********Course Menu*********
        1. Assign Teacher
        2. Create Course Record
        3. Update course Record
        4. Display course information
        5. Show enrollment List
        6. Show Assigned Teacher
        7. Go to Main menu
        *****************************      
        Please select a option to continue...   """
                )
            )

            if choice == 1:
                print("Teacher Assignation")
                courseID = input("Course-ID for Assigning teacher: ")
                teacherID = input("Teacher-ID to be Assigned: ")
                course = Course(courseID)
                teacher = Teacher(teacherID)
                courseService = CourseService()
                courseService.assign_teacher(course, teacher)

            elif choice == 2:
                print("Kindly provide the Course details")
                id = input("Course ID: ")
                course_name = input("Course name: ")
                credit = int(input("Credit: "))
                teacher_id = input("Teacher ID: ")
                print("Creating new Course Record.....")
                print(" ")
                print(" ")
                course = Course(id, course_name, credit, teacher_id)
                courseService = CourseService()
                try:
                    courseService.create_course(course)
                except Exception as err:
                    print(f"Unable to insert new record: {err}")
                else:
                    print("Successfully Inserted new Record")
                finally:
                    print("Returning to course menu....")

            elif choice == 3:
                print("Kindly provide the Updated Course details")
                id = input("Course ID: ")
                course_name = input("Course name: ")
                credit = int(input("Credit: "))
                teacher_id = input("Teacher ID: ")
                print("Updating new Course Record.....")
                print(" ")
                print(" ")
                course = Course(id, course_name, credit, teacher_id)
                courseService = CourseService()
                try:
                    courseService.update_course(course)
                except Exception as err:
                    print(f"Unable to update new record: {err}")
                else:
                    print("Successfully updated new Record")
                finally:
                    print("Returning to course menu....")

            elif choice == 4:
                print("Display course Information")
                id = input("Enter course-ID: ")
                course = Course(id)
                courseService = CourseService()
                courseService.display_course_info(course)

            elif choice == 5:
                print("Enrollments List")
                courseId = input("Course ID: ")
                course = Course(courseId)
                courseService = CourseService()
                courseService.get_Enrollments(course)
            elif choice == 6:
                print("Teacher assigned")
                courseId = input("Course-ID: ")
                course = Course(courseId)
                courseService = CourseService()
                courseService.get_Teacher(course)

            elif choice == 7:
                break


# 3
class Student:

    def __init__(
        self,
        studentId: str,
        fname: str = None,
        lname: str = None,
        dob: str = None,
        email: str = None,
        phone: str = None,
    ):
        self.studentId = studentId
        self.fname = fname
        self.lname = lname
        self.dob = (
            datetime.strptime(dob, "%Y-%m-%d").date() if dob is not None else None
        )
        self.email = email
        self.phone = phone

    @staticmethod
    def studentMenu():
        """
        Catalog for student operations
        """
        while True:
            choice = int(
                input(
        """
        *********Student Menu*********
        1. Create Student Record
        2. Update Student Record
        3. Display Student Information
        4. Enroll in a course
        5. Make Payments
        6. List enrolled courses
        7. View Payment History
        8. Go to Main menu
        *******************************
        Please select a option to continue...  """
                )
            )
            print()
            print()

            if choice == 1:
                print("Kindly provide the student details")
                id = input("Student ID: ")
                fname = input("First name: ")
                lname = input("Last name: ")
                dob = input("Date-of-Birth (YYYY-MM-DD): ")
                email = input("Email: ")
                phone = input("Phone: ")
                print("Creating new Student Record.....")
                print(" ")
                print(" ")
                student = Student(id, fname, lname, dob, email, phone)
                studentService = StudentServices()
                try:
                    studentService.create_student(student)
                except Exception as err:
                    print(f"Unable to insert new record: {err}")
                else:
                    print("Successfully Inserted new Record")
                finally:
                    print("Returning to main menu....")

            elif choice == 2:
                print("Kindly provide the updated student details")
                id = input("Student ID: ")
                fname = input("First name: ")
                lname = input("Last name: ")
                dob = input("Date-of-Birth (YYYY-MM-DD): ")
                email = input("Email: ")
                phone = input("Phone: ")
                print(" ")
                print(" ")
                print("updating Student Record.....")
                student = Student(id, fname, lname, dob, email, phone)
                studentService = StudentServices()
                try:
                    studentService.update_student(student)
                except Exception as err:
                    print(f"Unable to update record: {err}")
                else:
                    print("Successfully updated Record")
                finally:
                    print("Returning to main menu....")

            elif choice == 3:
                print("Display student Information")
                id = input("Enter Student-ID: ")
                student = Student(id)
                studentService = StudentServices()
                studentService.display_student_info(student)

            elif choice == 4:
                print("Course Enrollment")
                courseId = input("Enter the Course-ID for Enrollment: ")
                studentId = input("Enter the Student-ID for Enrollment: ")
                enrollment = Enrollment(studentId, courseId)
                studentService = StudentServices()
                studentService.enroll_in_course(enrollment)

            elif choice == 5:
                print("Make Payments")
                studentId = input("Student-ID: ")
                amount = int(input("Amount: "))
                payment = Payment(studentId, amount)
                studentService = StudentServices()
                studentService.make_payment(payment)

            elif choice == 6:
                print("List of enrolled Courses")
                studentId = input("Student-ID: ")
                student =Student(studentId)
                studentService = StudentServices()
                studentService.list_enrolled_courses(student)

            elif choice == 7:
                print("Payment History")
                studentId = input("Student-ID: ")
                student =Student(studentId)
                studentService = StudentServices()
                studentService.list_payment_history(student)

            elif choice == 8:
                break





# 4
class Payment:
    def __init__(self, paymentId:int = None, studentId: int = None, amount: int = None):
        self.paymentId = paymentId
        self.studentId = studentId
        self.amount = amount
        self.paymentDate = str(datetime.now().date())

    @staticmethod
    def paymentMenu():
        """
        Catalog for payment operations
        """
        while True:
            choice = int(
                input(
        """
        *********PAYMENT MENU*********
        1. Get Student details for Payment ID
        2. Get Payment Amount Details for Payment ID
        3. Get Payment Date Details for Payment ID
        4. Go to Main menu
        *******************************
        Please select a option to continue...  """))
            print()
            print()

            if choice == 1:
                print("Student Details for Payment-ID:-")
                paymentId = input("Payment ID: ")
                payment = Payment(paymentId= paymentId)
                paymentService = PaymentService()
                paymentService.get_student_details(payment)


            elif choice == 2:
                print("Payment amount for Payment-ID:-")
                paymentId = input("Payment ID: ")
                payment = Payment(paymentId= paymentId)
                paymentService = PaymentService()
                paymentService.get_payment_amount(payment)

            elif choice == 3:
                print("Payment amount for Payment-ID:-")
                paymentId = input("Payment ID: ")
                payment = Payment(paymentId= paymentId)
                paymentService = PaymentService()
                paymentService.get_payment_date(payment)

            elif choice == 4:
                break
        

    # def set_student(self, student:Student):
    #     self.student = Student

    # def get_student(self):
    #     return self.student

    # def get_payment_amount(self):
    #     return self.amount

    # def get_payment_date(self):
    #     return self.paymentDate


# 5
class Enrollment:

    def __init__(self, studentId: int = None, courseId: int = None, enrollmentId:int = None):
        self.enrollmentId = enrollmentId
        self.studentId = studentId
        self.courseId = courseId
        self.enrollmentDate = date = str(datetime.now().date())

    @staticmethod
    def enrollmentMenu():
        """
        Catalog for payment operations
        """
        while True:
            choice = int(
                input(
        """
        *********ENROLLMENT MENU*********
        1. Get Student details for Enrollment ID
        2. Get Course details for Enrollment ID
        3. Go to Main menu
        **********************************
        Please select a option to continue...  """))
            print()
            print()

            if choice == 1:
                print("Student Details for Enrollment-ID:-")
                enrollmentId = input("Enrollment ID: ")
                enrollment = Enrollment(enrollmentId = enrollmentId)
                enrollmentService = EnrollmentService()
                enrollmentService.get_student_details(enrollment)


            elif choice == 2:
                print("Course Details for Enrollment-ID:-")
                enrollmentId = input("Enrollment ID: ")
                enrollment = Enrollment(enrollmentId = enrollmentId)
                enrollmentService = EnrollmentService()
                enrollmentService.get_course_details(enrollment)

            elif choice == 3:
                break

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

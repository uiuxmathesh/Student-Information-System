from services import *
from datetime import  datetime
from .enrollment import Enrollment
from .payment import Payment

class Student:

    enrollments = None

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
        self.email = email
        self.phone = phone
        self.enrollments = set()
        if dob is not None:
            try:
                self.dob = datetime.strptime(dob, "%Y-%m-%d").date()
                self.dob = str(self.dob)
            except Exception as err:
                raise InvalidStudentDataException(f"ERROR: Please enter a valid date. {err}")
        else:
            self.dob = None

    @classmethod
    def createStudent(cls):
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
        try:
            student = Student(id, fname, lname, dob, email, phone)
        except Exception as e:
            print(e)
            return
        studentService = StudentServices()
        try:
            studentService.create_student(student)
        except Exception as err:
            print(f"Unable to insert new record: {err}")
        else:
            print("Successfully Inserted new Record")
        finally:
            print("Returning to main menu....")
            return

    @classmethod
    def updateStudent(cls):
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
            return

    @classmethod
    def displayStudentInfo(cls):
        print("Display student Information")
        id = input("Enter Student-ID: ")
        student = Student(id)
        studentService = StudentServices()
        studentService.display_student_info(student)
        return

    @classmethod
    def enrollInCourse(cls):
        print("Course Enrollment")
        courseId = input("Enter the Course-ID for Enrollment: ")
        studentId = input("Enter the Student-ID for Enrollment: ")
        enrollment = Enrollment(studentId, courseId)
        studentService = StudentServices()
        return
    
    @classmethod
    def makePayments(cls):
        print("Make Payments")
        studentId = input("Student-ID: ")
        amount = int(input("Amount: "))
        payment = Payment(studentId=studentId, amount=amount)
        studentService = StudentServices()
        studentService.make_payment(payment)
        return

    @classmethod
    def getpaymentHistory(cls):
        print("Payment History")
        studentId = input("Student-ID: ")
        student = Student(studentId)
        studentService = StudentServices()
        studentService.list_payment_history(student)
        return

    @classmethod
    def getEnrollments(cls):
        print("List of enrolled Courses")
        studentId = input("Student-ID: ")
        student = Student(studentId)
        studentService = StudentServices()
        studentService.list_enrolled_courses(student)
        return

    def setEnrollments(cls,enrollments):
        cls.enrollments.add(enrollments)
        
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
                Student.createStudent()

            elif choice == 2:
                Student.updateStudent()

            elif choice == 3:
                Student.displayStudentInfo()

            elif choice == 4:
                Student.enrollInCourse()

            elif choice == 5:
                Student.makePayments()

            elif choice == 6:
                Student.getEnrollments()

            elif choice == 7:
                Student.getpaymentHistory()

            elif choice == 8:
                break


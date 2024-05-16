from DAO import *
from Model import *
from datetime import datetime
import os
from Exceptions.custom_exceptions import *
from tabulate import tabulate

class Main:

    def __init__(self):
        print("Starting services...This may take a few seconds.")
        self.sis = SIS()
        os.system('cls') if os.name == 'nt' else os.system('clear')
        print("""
              
░██████╗████████╗██╗░░░██╗██████╗░███████╗███╗░░██╗████████╗
██╔════╝╚══██╔══╝██║░░░██║██╔══██╗██╔════╝████╗░██║╚══██╔══╝
╚█████╗░░░░██║░░░██║░░░██║██║░░██║█████╗░░██╔██╗██║░░░██║░░░
░╚═══██╗░░░██║░░░██║░░░██║██║░░██║██╔══╝░░██║╚████║░░░██║░░░
██████╔╝░░░██║░░░╚██████╔╝██████╔╝███████╗██║░╚███║░░░██║░░░
╚═════╝░░░░╚═╝░░░░╚═════╝░╚═════╝░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░

██╗███╗░░██╗███████╗░█████╗░██████╗░███╗░░░███╗░█████╗░████████╗██╗░█████╗░███╗░░██╗
██║████╗░██║██╔════╝██╔══██╗██╔══██╗████╗░████║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
██║██╔██╗██║█████╗░░██║░░██║██████╔╝██╔████╔██║███████║░░░██║░░░██║██║░░██║██╔██╗██║
██║██║╚████║██╔══╝░░██║░░██║██╔══██╗██║╚██╔╝██║██╔══██║░░░██║░░░██║██║░░██║██║╚████║
██║██║░╚███║██║░░░░░╚█████╔╝██║░░██║██║░╚═╝░██║██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║
╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝

░██████╗██╗░░░██╗░██████╗████████╗███████╗███╗░░░███╗
██╔════╝╚██╗░██╔╝██╔════╝╚══██╔══╝██╔════╝████╗░████║
╚█████╗░░╚████╔╝░╚█████╗░░░░██║░░░█████╗░░██╔████╔██║
░╚═══██╗░░╚██╔╝░░░╚═══██╗░░░██║░░░██╔══╝░░██║╚██╔╝██║
██████╔╝░░░██║░░░██████╔╝░░░██║░░░███████╗██║░╚═╝░██║
╚═════╝░░░░╚═╝░░░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═╝
              """)

    def main(self):
        while True:
            print("===========MAIN MENU===========")
            print("1. Student Menu")
            print("2. Teacher Menu")
            print("3. Course Menu")
            print("4. Reports")
            print("5. Exit")
            print("===============================")
            choice = input("Please select a option to continue.... ")
            if choice == "1":
                self.studentMenu()
            elif choice == "2":
                self.teacherMenu()
            elif choice == "3":
                self.courseMenu()
            elif choice == "4":
                self.reportsMenu()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again")

    def studentMenu(self):
        while True:
            print("+-+-+-+-+-+-+-STUDENT MENU-+-+-+-+-+-+-+")
            print("1. Add Student")
            print("2. Update Student Info")
            print("3. Make Payment")
            print("4. Enroll in Course")
            print("5. Display Student Info")
            print("6. Get Enrolled Courses")
            print("7. Get Payment History")
            print("8. Go back")
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            choice = input("Please select a option to continue....")
            if choice == "1":
                try:
                    student = Student()
                    student.studentId = int(input("Enter Student ID: "))
                    student.fname = input("Enter First Name: ")
                    student.lname = input("Enter Last Name: ")
                    student.dob = input("Enter Date of Birth (yyyy-mm-dd): ")
                    student.email = input("Enter Email: ")
                    student.phone = input("Enter Phone Number: ")
                    self.sis.studentService.addStudent(student)
                except Exception as e:
                    print(e)
                else:
                    print("Student added successfully")


            elif choice == "2":
                try:
                    student = Student()
                    student.studentId = int(input("Enter Student ID: "))
                    student.fname = input("Enter First Name: ")
                    student.lname = input("Enter Last Name: ")
                    student.dob = input("Enter Date of Birth (yyyy-mm-dd): ")
                    student.email = input("Enter Email: ")
                    student.phone = input("Enter Phone Number: ")
                    self.sis.studentService.updateStudentInfo(student)
                except Exception as e:
                    print(e)

            elif choice == "3":
                try:
                    studentId = int(input("Enter Student ID: "))
                    amount = float(input("Enter Amount: "))
                    paymentDate = str(datetime.now().date())
                    self.sis.recordPayment(studentId=studentId, amount=amount, paymentDate=paymentDate)
                except Exception as e:
                    print(e)

            elif choice == "4":
                try:
                    student = Student()
                    student.studentId = int(input("Enter Student ID: "))
                    course = Course()
                    course.code = input("Enter Course Code: ")
                    self.sis.enrollStudentInCourse(student, course)
                except Exception as e:
                    print(e)
                else:
                    print("Student enrolled in course successfully")
                    
            elif choice == "5":
                try:
                    student = Student()
                    student.studentId = int(input("Enter Student ID: "))
                    result = self.sis.studentService.displayStudentInfo(student)
                except Exception as e:
                    print(e)
                else:
                    print(tabulate(result, headers='firstrow', tablefmt="pretty"))

            elif choice == "6":
                    try:
                        student = Student()
                        student.studentId = int(input("Enter Student ID: "))
                        self.sis.getEnrollmentForStudent(student)
                    except Exception as e:
                        print(e)

            elif choice == "7":
                try:
                    student = Student()
                    student.studentId = int(input("Enter Student ID: "))
                    result = self.sis.studentService.getPaymentHistory(student)
                    if len(result) == 1:
                        raise InvalidPaymentDataException(f"No payment history found for Student ID {student.studentId}.")
                except Exception as e:  
                    print(e)
                else:
                    table = tabulate(result, headers='firstrow', tablefmt="fancy_grid")
                    print(table)
                
            elif choice == "8":
                break
            else:
                print("Invalid choice. Please try again")
    
    def teacherMenu(self):
        while True:
            print("+-+-+-+-+-+-+-TEACHER MENU-+-+-+-+-+-+-+")
            print("1. Add Teacher")
            print("2. Update Teacher Info")
            print("3. Display Teacher Info")
            print("4. Get Assigned Courses")
            print("5. Go back")
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            choice = input("Please select a option to continue....")
            if choice == "1":
                try:
                    teacher = Teacher()
                    teacher.teacherId = int(input("Enter Teacher ID: "))
                    teacher.fname = input("Enter First Name: ")
                    teacher.lname = input("Enter Last Name: ")
                    teacher.email = input("Enter Email: ")
                    teacher.expertise = input("Enter Expertise: ")
                    self.sis.teacherService.addTeacher(teacher)
                except Exception as e:
                    print(e)
                else:
                    print("Teacher added successfully")

            elif choice == "2":
                try:
                    teacher = Teacher()
                    teacher.teacherId = int(input("Enter Teacher ID: "))
                    teacher.fname = input("Enter First Name: ")
                    teacher.lname = input("Enter Last Name: ")
                    teacher.email = input("Enter Email: ")
                    teacher.expertise = input("Enter Expertise: ")
                    self.sis.teacherService.updateTeacherInfo(teacher)
                except ValueError as e:
                    print("Invalid Teacher ID. Please enter a valid Teacher ID.")
                except Exception as e:
                    print(f"Error: {e}")
                else:
                    print("Teacher information updated successfully")

            elif choice == "3":
                try:
                    teacher = Teacher()
                    teacher.teacherId = int(input("Enter Teacher ID: "))
                    result = self.sis.teacherService.displayTeacherInfo(teacher)
                except Exception as e:
                    print(e)
                else:
                    print(tabulate(result, headers='firstrow', tablefmt="fancy_grid"))

            elif choice == "4":
                try:
                    teacher = Teacher()
                    teacher.teacherId = int(input("Enter Teacher ID: "))
                    assignedCoursesList = self.sis.getCoursesForTeacher(teacher)
                except Exception as e:
                    print(e)
                else:
                    table = tabulate(assignedCoursesList, headers="firstrow", tablefmt="fancy_grid")
                    print(table)
                    
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again")

    def courseMenu(self):
        while True:
            print("+-+-+-+-+-+-+-COURSE MENU-+-+-+-+-+-+-+")
            print("1. Update Course Info")
            print("2. Display Course Info")
            print("3. Get Assigned Teacher")
            print("4. Get Enrollments")
            print("5. Assign Teacher to Course")
            print("6. Go back")
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            choice = input("Please select a option to continue....")
            if choice == "1":
                course = Course()
                try:
                    course.code = input("Enter Course Code: ")
                    course.name = input("Enter Course Name: ")
                    course.credit = int(input("Enter Credits: "))
                    course.fee = float(input("Enter Course Fee: "))
                    self.sis.courseService.updateCourseInfo(course)
                except Exception as e:
                    print(e)
                else:
                    print("Course information updated successfully")

            elif choice == "2":
                try:
                    course = Course()
                    course.code = input("Enter Course Code: ")
                    courseDetails = self.sis.courseService.displayCourseInfo(course)
                except Exception as e:
                    print(e)
                else:
                    table = tabulate(courseDetails, headers='firstrow', tablefmt="fancy_grid")
                    print(table)

            elif choice == "3":
                try:
                    course = Course()
                    course.code = input("Enter Course Code: ")
                    assignedTeacher = self.sis.courseService.getTeacher(course)
                except Exception as e:
                    print(e)
                else:
                    table = tabulate(assignedTeacher, headers='firstrow', tablefmt="fancy_grid")
                    print(table)

            elif choice == "4":
                course = Course()
                try:
                    course.code = input("Enter Course Code: ")
                    enrollments = self.sis.courseService.getEnrollments(course)
                except Exception as e:
                    print(e)
                else:
                    table = tabulate(enrollments, headers='firstrow', tablefmt="fancy_grid")
                    print(table)

            elif choice == "5":
                try:
                    course = Course()
                    course.code = input("Enter Course Code: ")
                    teacher = Teacher()
                    teacher.teacherId = int(input("Enter Teacher ID: "))
                    self.sis.assignTeacherToCourse(teacher=teacher, course=course)
                except Exception as e:
                    raise e
                else:
                    print("Teacher assigned to course successfully")
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again")
            
    def reportsMenu(self):
        while True:
            print("+-+-+-+-+-+-+-REPORTS MENU-+-+-+-+-+-+-+")
            print("1. Get Enrolled Courses")
            print("2. Get Payment History")
            print("3. Get Course Statistics")
            print("4. Go back")
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            choice = input("Please select a option to continue....")
            if choice == "1":
                student = Student()
                student.studentId = int(input("Enter Student ID: "))
                self.sis.getEnrollmentReport(student)
            elif choice == "2":
                student = Student()
                student.studentId = int(input("Enter Student ID: "))
                self.sis.getPaymentReport(student)
            elif choice == "3":
                course = Course()
                course.code = input("Enter Course Code: ")
                self.sis.calculateCourseStatistics(course)
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again")

    def close(self):
        print("Closing services...")
        self.sis.closeConnections()
        os.system('cls') if os.name == 'nt' else os.system('clear')
        


if __name__ == "__main__":
    main = Main()
    main.main()
    main.close()
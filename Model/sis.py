from .course import Course
from .student import Student
from .enrollment import Enrollment
from .payment import Payment
from .teacher import Teacher
from DAO import StudentDao, CourseDao, TeacherDao, EnrollmentDao, PaymentDao
from datetime import datetime
from Exceptions.custom_exceptions import *
from Util import ReportGen


class SIS:

    def __init__(self):
        print("Starting services...This may take a few seconds.")
        self.studentService = StudentDao()
        self.courseService = CourseDao()
        self.teacherService = TeacherDao()
        self.enrollmentService = EnrollmentDao()
        self.paymentService = PaymentDao()

    def enrollStudentInCourse(self, student:Student, course:Course):
        # Checking if the student and course exist in the database
        studentDetails = self.studentService.displayStudentInfo(student)
        courseDetails = self.courseService.displayCourseInfo(course)
        if studentDetails == []:
            raise StudentNotFoundException(f"Student ID {student.studentId} not found. Please enter a valid Student ID.")
        elif courseDetails == []:
            raise CourseNotFoundException(f"Course Code {course.code} not found. Please enter a valid Course Code.") 
        try:
            enrollmentID = self.studentService.enrollInCourse(student, course)
        except Exception as e:
            print(e)
        else:

            print(studentDetails)
            print(courseDetails)
            enrollment = Enrollment()
            student = Student()
            course = Course()
            student.create_by_list(studentDetails)
            course.create_by_list(courseDetails)
            enrollment.create_by_list([enrollmentID, student.studentId, course.code, str(datetime.now().date())])
            enrollment.student = student
            enrollment.course = course
            self.addEnrollment(student, course, str(datetime.now().date()))
            # print(student)
            # print(course)
            # print(enrollment)
            # Student.enrollments(enrollment)
            # Course.enrollments(enrollment)

              # Implementing class-level data structure to store enrollments

    def assignTeacherToCourse(self, teacher:Teacher, course:Course):
        courseDetails = self.courseService.displayCourseInfo(course) 
        teacherDetails = self.teacherService.displayTeacherInfo(teacher)
        try:
            if courseDetails == []:
                raise CourseNotFoundException(f"Course Code {course.code} not found. Please enter a valid Course Code.")
            elif teacherDetails == []:
                raise TeacherNotFoundException(f"Teacher ID {teacher.teacherId} not found. Please enter a valid Teacher ID.")
            self.courseService.assignTeacher(teacher, course)
        except Exception as e:
            print(e)
        else:
            course = Course()
            teacher = Teacher()
            course.create_by_list(courseDetails)
            teacher.create_by_list(teacherDetails)
            course.teacherId = teacher.teacherId
            self.assignCourseToTeacher(course, teacher)
            # print(course)
            # Teacher.assignedCourses(course)

    def recordPayment(self, studentId:str, amount:float, paymentDate:str):
        
        student = Student()
        student.studentId = studentId
        studentDetails = self.studentService.displayStudentInfo(student)
        try:
            if amount <= 0:
                raise PaymentValidationException("Payment amount must be greater than 0.")
            
            elif paymentDate > str(datetime.now().date()):
                raise PaymentValidationException("Payment date cannot be in the future.")
            
            elif studentDetails == []:
                raise StudentNotFoundException(f"Student ID {studentId} not found. Please enter a valid Student ID.")
            
            paymentId = self.studentService.makePayment(studentId, amount, paymentDate)

        except Exception as e:
            print(e)
        else:
            payment = Payment()
            student.create_by_list(studentDetails)
            payment.paymentId = paymentId
            payment.studentId = studentId
            payment.amount = amount
            payment.paymentDate = paymentDate 
            payment.student = student
            # Payment.payment.append(payment)   
            # print(payment)   

    def getEnrollmentReport(self, student:Student):
        enrollmentList = self.studentService.getEnrolledCourses(student)
        header = self.studentService.cursor.description
        header = tuple( column[0] for column in header )
        enrollmentList = [header, *enrollmentList ]
        print(enrollmentList)
        report = ReportGen()
        return report.createReport(enrollmentList, "enrollment")

    def getPaymentReport(self, student:Student):
        paymentList = self.studentService.getPayments(student)
        header = self.studentService.cursor.description
        header = tuple( column[0] for column in header )
        paymentList = [header, *paymentList ]
        print(paymentList)
        report = ReportGen()
        return report.createReport(paymentList, "payment")
        # pdf = canvas.Canvas("payment_report.pdf")
        # pdf.setFont("Helvetica-Bold", 16)
        # pdf.drawString(50, 750, "Enrollment Report")
        # pdf.setFont("Helvetica", 12)
        # y = 700
        # for row in paymentList:
        #     pdf.drawString(50, y, f"Enrollment ID: {row[0]}")
        #     pdf.drawString(50, y-20, f"Student ID: {row[1]}")
        #     pdf.drawString(50, y-40, f"Course Code: {row[2]}")
        #     pdf.drawString(50, y-60, f"Enrollment Date: {row[3]}")
        #     y -= 60
        # pdf.save()
        # pass

    def calculateCourseStatistics(self, course:Course):
        pass

    def addEnrollment(self, student, course, enrollmentDate):
        enrollment = Enrollment()
        enrollment.course = course
        enrollment.student = student
        enrollment.enrollmentDate = enrollmentDate
        Student.enrollments(enrollment)
        Course.enrollments(enrollment)

    def assignCourseToTeacher(self, course:Course, teacher:Teacher):
        course.teacherId = teacher.teacherId
        Teacher.assignedCourses(course)

    def addPayment(self, student:Student, amount, paymentDate):
        payment = Payment()
        paymentID = self.paymentService.cursor.execute("SELECT IDENT_CURRENT('payments') AS ['id']")
        payment.paymentId = paymentID
        payment.studentId = student.studentId
        payment.paymentDate = paymentDate
        payment.amount = amount
        payment.student = student
        Payment.payment.append(payment)

    def getEnrollmentForStudent(self, student):
        enrollmentList = self.studentService.getEnrolledCourses(student)

    def getCoursesForTeacher(self, teacher):
        assignedCoursesList = self.teacherService.getAssignedCourses(teacher)
        print(assignedCoursesList)

    def closeConnections(self):
        self.studentService.close()
        self.courseService.close()
        self.teacherService.close()
        self.enrollmentService.close()
        self.paymentService.close()
from .course import Course
from .student import Student
from .enrollment import Enrollment
from .payment import Payment
from .teacher import Teacher
from DAO import StudentDao, CourseDao, TeacherDao, EnrollmentDao, PaymentDao
from datetime import datetime
from Exceptions.custom_exceptions import *
from Util import ReportGen
from tabulate import tabulate


class SIS:

    def __init__(self):
        print("Initializing student services...")
        self.studentService = StudentDao()
        print("Initializing course services...")
        self.courseService = CourseDao()
        print("Initializing teacher services...")
        self.teacherService = TeacherDao()
        print("Initializing enrollment services...")
        self.enrollmentService = EnrollmentDao()
        print("Initializing payment services...")
        self.paymentService = PaymentDao()

    def enrollStudentInCourse(self, student: Student, course: Course):
        # Checking if the student and course exist in the database
        studentDetails = self.studentService.displayStudentInfo(student)
        courseDetails = self.courseService.displayCourseInfo(course)
        if studentDetails == []:
            raise StudentNotFoundException(
                f"Student ID {student.studentId} not found. Please enter a valid Student ID."
            )
        elif courseDetails == []:
            raise CourseNotFoundException(
                f"Course Code {course.code} not found. Please enter a valid Course Code."
            )
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
            enrollment.create_by_list(
                [
                    enrollmentID,
                    student.studentId,
                    course.code,
                    str(datetime.now().date()),
                ]
            )
            enrollment.student = student
            enrollment.course = course
            self.addEnrollment(student, course, str(datetime.now().date()))

    def assignTeacherToCourse(self, teacher: Teacher, course: Course):
        courseDetails = self.courseService.displayCourseInfo(course)
        teacherDetails = self.teacherService.displayTeacherInfo(teacher)
        self.courseService.assignTeacher(teacher, course)
        course = Course()
        teacher = Teacher()
        course.create_by_list(courseDetails[1])
        teacher.create_by_list(teacherDetails[1])
        course.teacherId = teacher.teacherId
        self.assignCourseToTeacher(course, teacher)

    def recordPayment(self, studentId: int, amount: float, paymentDate: str):

        student = Student()
        student.studentId = studentId
        studentDetails = self.studentService.displayStudentInfo(student)
        courseFee = self.studentService.getEnrolledCourses(student)[0][4]
        if amount <= 0:
            raise PaymentValidationException(
                "Payment amount must be greater than 0."
            )
        elif amount < courseFee:
            raise InsufficientFundsException(
                f"Payment amount must be greater than or equal to the course fee of {courseFee}."
            )
        elif paymentDate > str(datetime.now().date()):
            raise PaymentValidationException(
                "Payment date cannot be in the future."
            )
        elif len(studentDetails) == 1:
            raise StudentNotFoundException(
                f"Student ID {studentId} not found. Please enter a valid Student ID."
            )    
        else:
            paymentId = self.studentService.makePayment(studentId, amount, paymentDate)
            print(f"Payment made successfully. Payment ID: {paymentId}")
            payment = Payment()
            studentDetails = studentDetails[1]
            student.create_by_list(studentDetails)
            payment.paymentId = paymentId
            payment.studentId = studentId
            payment.amount = amount
            payment.paymentDate = paymentDate
            payment.student = student

    def getEnrollmentReport(self, student: Student):
        enrollmentList = self.studentService.getEnrolledCourses(student)
        report = ReportGen()
        report.createReport(enrollmentList, "enrollment")

    def getPaymentReport(self, student: Student):
        paymentList = self.studentService.getPaymentHistory(student)
        if len(paymentList) == 1:
            raise InvalidPaymentDataException(
                f"No payment history found for Student ID {student.studentId}."
            )
        report = ReportGen()
        report.createReport(paymentList, "payment")

    def calculateCourseStatistics(self, course: Course):
        query = """
                SELECT	course.course_code,
                        course.course_name,
                        course.course_fee,
                        teacher.teacher_id,
                        CONCAT(teacher.first_name,' ',teacher.last_name) AS teacher_name,
                        COUNT(students.student_id) AS Total_Enrollments,
                        SUM(payments.amount) Total_Fee_Paid
                FROM	[course]
                        INNER JOIN [enrollments] ON course.course_code = enrollments.course_code
                        INNER JOIN [students] ON students.student_id = enrollments.student_id
                        INNER JOIN [payments] ON payments.student_id = enrollments.student_id
                        INNER JOIN [teacher] ON teacher.teacher_id = course.teacher_id
                WHERE	course.course_code = ?
                GROUP BY	course.course_code,
                            course.course_name,
                            course.course_fee,
                            teacher.teacher_id,
                            teacher.first_name,
                            teacher.last_name
                """
        self.courseService.cursor.execute(query, (course.code,))
        result = self.courseService.cursor.fetchall()
        headers = self.courseService.cursor.description
        headers = tuple(header[0] for header in headers)
        table = tabulate(result, headers=headers, tablefmt="fancy_grid")
        print(table)

    def addEnrollment(self, student, course, enrollmentDate):
        enrollment = Enrollment()
        enrollment.course = course
        enrollment.student = student
        enrollment.enrollmentDate = enrollmentDate
        Student.enrollments(enrollment)
        Course.enrollments(enrollment)

    def assignCourseToTeacher(self, course: Course, teacher: Teacher):
        course.teacherId = teacher.teacherId
        Teacher.assignedCourses(course)

    def addPayment(self, student: Student, amount, paymentDate):
        payment = Payment()
        paymentID = self.paymentService.cursor.execute(
            "SELECT IDENT_CURRENT('payments') AS ['id']"
        )
        payment.paymentId = paymentID
        payment.studentId = student.studentId
        payment.paymentDate = paymentDate
        payment.amount = amount
        payment.student = student
        Payment.payment.append(payment)

    def getEnrollmentForStudent(self, student):
        enrollmentList = self.studentService.getEnrolledCourses(student)
        print("from SIS", enrollmentList)
        if len(enrollmentList) == 1:
            raise InvalidEnrollmentDataException(f"No enrollment data found for Student ID {student.studentId}.")
        table = tabulate(enrollmentList, headers='firstrow', tablefmt="fancy_grid")
        print(table)

    def getCoursesForTeacher(self, teacher):
        assignedCoursesList = self.teacherService.getAssignedCourses(teacher)
        return assignedCoursesList

    def closeConnections(self):
        self.studentService.close()
        self.courseService.close()
        self.teacherService.close()
        self.enrollmentService.close()
        self.paymentService.close()

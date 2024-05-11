from services import *
from datetime import datetime

class Enrollment:
    
    student = None
    course = None
    def __init__(
        self, studentId: int = None, courseId: int = None, enrollmentId: int = None
    ):
        self.enrollmentId = enrollmentId
        self.studentId = studentId
        self.courseId = courseId
        self.enrollmentDate = date = str(datetime.now().date())
        

    @classmethod
    def getStudent(cls):
        print("Student Details for Enrollment-ID:-")
        enrollmentId = input("Enrollment ID: ")
        enrollment = Enrollment(enrollmentId=enrollmentId)
        enrollmentService = EnrollmentService()
        enrollmentService.get_student_details(enrollment)
        return

    def setStudent(self, student):
        self.student = student

    @classmethod
    def getCourse(cls):
        print("Course Details for Enrollment-ID:-")
        enrollmentId = input("Enrollment ID: ")
        enrollment = Enrollment(enrollmentId=enrollmentId)
        enrollmentService = EnrollmentService()
        enrollmentService.get_course_details(enrollment)
        return

    def setCourse(self,course):
        self.course = course

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
        Please select a option to continue...  """
                )
            )
            print()
            print()

            if choice == 1:
                Enrollment.getStudent()

            elif choice == 2:
                Enrollment.getCourse()

            elif choice == 3:
                break


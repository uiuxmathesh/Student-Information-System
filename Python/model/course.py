from exceptions import *
from services import *
from .teacher import Teacher

class Course:


    enrollments = None
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
        self.enrollments = set()

    @classmethod
    def assignTeacher(cls):
        print("Teacher Assignation")
        courseID = input("Course-ID for Assigning teacher: ")
        teacherID = input("Teacher-ID to be Assigned: ")
        course = Course(courseID)
        teacher = Teacher(teacherID)
        courseService = CourseService()
        courseService.assign_teacher(course, teacher)
        return

    @classmethod
    def createCourse(cls):
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
            return


    @classmethod
    def updateCourseInfo(cls):
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
            return

    @classmethod
    def displayCourse(cls):
        print("Display course Information")
        id = input("Enter course-ID: ")
        course = Course(id)
        courseService = CourseService()
        courseService.display_course_info(course)
        return

    @classmethod
    def getEnrollments(cls):
        print("Enrollments List")
        courseId = input("Course ID: ")
        course = Course(courseId)
        courseService = CourseService()
        courseService.get_Enrollments(course)
        return
    
    def setEnrollments(self, enrollment):
        self.enrollments.add(enrollment)

    @classmethod
    def getTeacher(cls):
        print("Teacher assigned")
        courseId = input("Course-ID: ")
        course = Course(courseId)
        courseService = CourseService()
        courseService.get_Teacher(course)
        return

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
                Course.assignTeacher()

            elif choice == 2:
                Course.createCourse()

            elif choice == 3:
                Course.updateCourseInfo()
            elif choice == 4:
                Course.displayCourse()

            elif choice == 5:
                Course.getEnrollments()

            elif choice == 6:
                Course.getTeacher()

            elif choice == 7:
                break


from services import *

class Teacher:

    assignedCourse = None
    def __init__(
        self, teacherId: int, fname: str = None, lname: str = None, email: str = None
    ):
        self.teacherId = teacherId
        self.fname = fname
        self.lname = lname
        self.email = email
        self.assignedCourse = set() 
    
    @classmethod
    def createTeacher(cls):
        print("Kindly provide the Teacher details")
        id = input("Teacher ID: ")
        fname = input("First name: ")
        lname = input("Last name: ")
        email = input("Email: ")

        print("Creating new Teacher Record.....")
        print()
        print()
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
        return

    @classmethod
    def updateTeacherInfo(cls):
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
        return

    @classmethod
    def displayTeacherInfo(cls):
        print("Display student Information")
        id = input("Enter Student-ID: ")
        teacher = Teacher(id)
        teacherService = TeacherService()
        teacherService.display_teacher_info(teacher)
        return

    @classmethod
    def getAssignedCourse(cls):
        print("Assigned Course for a Teacher")
        teacherId = input("Teacher ID: ")
        teacher = Teacher(teacherId)
        teacherService = TeacherService()
        teacherService.get_assigned_courses(teacher)
        return

    def setAssignedCourse(self, course):
        self.assignedCourse.add(course)

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
        ******************************             
        Please select a option to continue...  """
                )
            )

            if choice == 1:
                Teacher.createTeacher()

            elif choice == 2:
                Teacher.updateTeacherInfo()

            elif choice == 3:
                Teacher.displayTeacherInfo()

            elif choice == 4:
                Teacher.getAssignedCourse()

            elif choice == 5:
                print("Returning to Main Menu......")
                return
   
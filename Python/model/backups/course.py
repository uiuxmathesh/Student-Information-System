from teacher import Teacher
class Course:

    def __init__(self, courseId:int, name:str, code:str, instructor_name:str):
        self.__courseId = courseId
        self.__name = name
        self.__code = code
        self.__instructor_name = instructor_name
    
    def assign_teacher(self, teacher:Teacher):
        self._teacher = teacher
    
    def update_course_info(self,courseCode:str, courseName:str, instructorName:str):
        self.__code = courseCode
        self.__name = courseName
        self.__instructor_name = instructorName

    def display_course_info(self):
        print(f'Course ID: { self.__courseId}, Course Name: { self.__name}, Course Code: {self.__code}, Instructor Name: {self.__instructor_name}')

    def get_enrollments(self):
        pass

    def get_Teacher(self):
        return self._teacher
    
c1 = Course(1,"Engineering Mathematics","19UMA123","Nandhakumar")

c1.display_course_info()
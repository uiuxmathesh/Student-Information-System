from datetime import datetime
class Enrollment:

    def __init__(self, enrollmentId:int, studentId:int, courseId:int, enrollmentDate:datetime):
        self.__enrollmentId = enrollmentId
        self.__studentId = studentId
        self.__courseId = courseId
        self.__enrollmentDate = datetime.strptime(enrollmentDate, "%d-%m-%Y").date()

    def get_student(self):
        return self.__studentId
    
    def get_course(self):
        return self.__courseId
    
    def display_enrollment(self):
        print(f'Enrollment ID: {self.__enrollmentId}, Student ID: {self.__studentId}, Course ID: {self.__courseId}, Date Enrolled: {self.__enrollmentDate}')


e1 = Enrollment(1,1,1,"08-05-2024")
e1.display_enrollment()
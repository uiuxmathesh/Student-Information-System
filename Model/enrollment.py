from Exceptions.custom_exceptions import InvalidEnrollmentDataException
from datetime import datetime
class Enrollment:
    def __init__(self):
        self.enrollmentId = None
        self.studentId = None
        self.courseId = None
        self.enrollmentDate = None

    @property
    def enrollmentId(self):
        return self.enrollmentId
    
    @enrollmentId.setter
    def enrollmentId(self, enrollmentId):
        if not isinstance(enrollmentId,int):
            raise InvalidEnrollmentDataException("Enrollment ID must be an integer")
        self.enrollmentId = enrollmentId

    @property
    def studentId(self):
        return self.studentId
    
    @studentId.setter
    def studentId(self, studentId):
        if not isinstance(studentId,str):
            raise InvalidEnrollmentDataException("Student ID must be an integer")
        self.studentId = studentId

    @property
    def courseId(self):
        return self.courseId
    
    @courseId.setter
    def courseId(self, courseId):
        if not isinstance(courseId,str):
            raise InvalidEnrollmentDataException("Course ID must be an integer")
        self.courseId = courseId

    @property
    def enrollmentDate(self):
        return self.enrollmentDate
    
    @enrollmentDate.setter
    def enrollmentDate(self, enrollmentDate):
        if enrollmentDate == "":
            raise InvalidEnrollmentDataException("Enrollment Date cannot be empty")
        try:
            self.enrollmentDate = str(datetime.strptime(enrollmentDate, "%Y-%m-%d"))
        except Exception as e:
            raise InvalidEnrollmentDataException("Invalid Enrollment Date format. Please use YYYY-MM-DD format.")
        
    def __str__(self):
        return f"Enrollment ID: {self.enrollmentId}, Student ID: {self.studentId}, Course ID: {self.courseId}, Enrollment Date: {self.enrollmentDate}"
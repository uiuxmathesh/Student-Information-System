from Exceptions.custom_exceptions import InvalidEnrollmentDataException
from datetime import datetime
class Enrollment:
    def __init__(self):
        self._enrollmentId = None
        self._studentId = None
        self._courseCode = None
        self._enrollmentDate = None
        self._student = None
        self._course = None

    @property
    def enrollmentId(self):
        return self._enrollmentId
    
    @enrollmentId.setter
    def enrollmentId(self, enrollmentId):
        if not isinstance(enrollmentId,int):
            raise InvalidEnrollmentDataException("Enrollment ID must be an integer")
        self._enrollmentId = enrollmentId

    @property
    def studentId(self):
        return self._studentId
    
    @studentId.setter
    def studentId(self, studentId):
        if not isinstance(studentId,str):
            raise InvalidEnrollmentDataException("Student ID must be an integer")
        self._studentId = studentId

    @property
    def courseCode(self):
        return self._courseCode
    
    @courseCode.setter
    def courseCode(self, courseCode):
        if not isinstance(courseCode,str):
            raise InvalidEnrollmentDataException("Course ID must be an string")
        self._courseCode = courseCode

    @property
    def enrollmentDate(self):
        return self._enrollmentDate
    
    @enrollmentDate.setter
    def enrollmentDate(self, enrollmentDate):
        if enrollmentDate == "":
            raise InvalidEnrollmentDataException("Enrollment Date cannot be empty")
        try:
            self.enrollmentDate = str(datetime.strptime(enrollmentDate, "%Y-%m-%d"))
        except Exception as e:
            raise InvalidEnrollmentDataException("Invalid Enrollment Date format. Please use YYYY-MM-DD format.")
        
    @property
    def student(self):
        return self._student
    
    @student.setter
    def student(self, student):
        self._student = student
        
    def __str__(self):
        return f"Enrollment ID: {self.enrollmentId}, Student ID: {self.studentId}, Course ID: {self.courseCode}, Enrollment Date: {self.enrollmentDate}"
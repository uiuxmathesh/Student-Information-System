
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
        self.enrollmentId = enrollmentId

    @property
    def studentId(self):
        return self.studentId
    
    @studentId.setter
    def studentId(self, studentId):
        self.studentId = studentId

    @property
    def courseId(self):
        return self.courseId
    
    @courseId.setter
    def courseId(self, courseId):
        self.courseId = courseId

    @property
    def enrollmentDate(self):
        return self.enrollmentDate
    
    @enrollmentDate.setter
    def enrollmentDate(self, enrollmentDate):
        self.enrollmentDate = enrollmentDate

    def __str__(self):
        return f"Enrollment ID: {self.enrollmentId}, Student ID: {self.studentId}, Course ID: {self.courseId}, Enrollment Date: {self.enrollmentDate}"
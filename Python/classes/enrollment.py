class Enrollment:

    def __init__(self, enrollmentId, studentId, courseId, enrollmentDate):
        self.enrollmentId = enrollmentId
        self.studentId = studentId
        self.courseId = courseId
        self.enrollmentDate = enrollmentDate


# Testing class
enrollment1 = Enrollment("E1001", "S1001", "C1001", "2023-04-21")
print(enrollment1.enrollmentDate)

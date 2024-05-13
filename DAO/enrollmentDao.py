
class EnrollmentDao:

    def __init__(self):
        self.connection = None  
        self.cursor = self.connection.cursor()

    def getStudent(self,enrollment):
        query = "SELECT * FROM [students] WHERE [student_id] = (SELECT [student_id] FROM [enrollments] WHERE [enrollment_id] = ?)"
        values = (enrollment.enrollmentId)
        self.cursor.execute(query, values)
        headers = (column[0] for column in self.cursor.description)
        student = self.cursor.fetchall()
        student = [headers] + student
        self.cursor.close()
        self.connection = None
        return student

    def getCourse(self,enrollment):
        query = "SELECT * FROM [courses] WHERE [course_code] = (SELECT [course_code] FROM [enrollments] WHERE [enrollment_id] = ?)"
        values = (enrollment.enrollmentId)
        self.cursor.execute(query, values)
        headers = (column[0] for column in self.cursor.description)
        course = self.cursor.fetchall()
        course = [headers] + course
        self.cursor.close()
        self.connection = None
        return course
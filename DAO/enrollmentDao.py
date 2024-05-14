from Util import DBConnUtil

class EnrollmentDao(DBConnUtil):
        
    def getStudent(self,enrollment): # WORKING GOOD AS EXPECTED
        query = "SELECT * FROM [students] WHERE [student_id] = (SELECT [student_id] FROM [enrollments] WHERE [enrollment_id] = ?)"
        values = (enrollment.enrollmentId)
        self.cursor.execute(query, values)
        headers = tuple(column[0] for column in self.cursor.description)
        student = self.cursor.fetchall()
        return student

    def getCourse(self,enrollment): # WORKING GOOD AS EXPECTED
        query = "SELECT * FROM [course] WHERE [course_code] = (SELECT [course_code] FROM [enrollments] WHERE [enrollment_id] = ?)"
        values = (enrollment.enrollmentId)
        self.cursor.execute(query, values)
        headers = tuple(column[0] for column in self.cursor.description)
        course = self.cursor.fetchall()
        return course
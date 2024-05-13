from Util import DBConnUtil

class EnrollmentDao:
        
    def getStudent(self,enrollment): # WORKING GOOD AS EXPECTED
        self.connection = DBConnUtil.getConnection()  
        self.cursor = self.connection.cursor()
        query = "SELECT * FROM [students] WHERE [student_id] = (SELECT [student_id] FROM [enrollments] WHERE [enrollment_id] = ?)"
        values = (enrollment.enrollmentId)
        self.cursor.execute(query, values)
        headers = tuple(column[0] for column in self.cursor.description)
        student = self.cursor.fetchall()
        # student = [headers] + student
        self.cursor.close()
        self.connection = DBConnUtil.closeConnection()
        return student

    def getCourse(self,enrollment): # WORKING GOOD AS EXPECTED
        self.connection = DBConnUtil.getConnection()  
        self.cursor = self.connection.cursor()
        query = "SELECT * FROM [course] WHERE [course_code] = (SELECT [course_code] FROM [enrollments] WHERE [enrollment_id] = ?)"
        values = (enrollment.enrollmentId)
        self.cursor.execute(query, values)
        headers = tuple(column[0] for column in self.cursor.description)
        course = self.cursor.fetchall()
        # course = [headers] + course
        self.cursor.close()
        self.connection = DBConnUtil.closeConnection()
        return course
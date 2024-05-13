
class courseDAO:

    def __init__(self):
        self.connection = None
        self.cursor = self.connection.cursor()

    def assignTeacher(self, course):
        query = "UPDATE [courses] SET [teacher_id] = ? WHERE [course_code] = ?"
        values = (course.teacher_id, course.courseCode)
        self.cursor.execute(query, values)
        self.cursor.commit()


    def updateCourseInfo(self,course):
        query = "UPDATE [courses] SET [course_name] = ?, [course_credit] = ?, [course_fee] = ?, [teacher_id] = ? WHERE [course_code] = ?"
        values = (course.name, course.credit, course.fee, course.teacherId, course.code)
        self.cursor.execute(query, values)
        self.cursor.commit()
        self.cursor.close()
        self.connection = None


    def displayCourseInfo(self,course):
        query = "SELECT * FROM [courses] WHERE [course_code] = ?"
        values = (course.code)
        self.cursor.execute(query, values)
        courseInfo = self.cursor.fetchall()
        headers = (column[0] for column in self.cursor.description)
        courseInfo = [headers] + courseInfo
        self.cursor.close()
        self.connection = None

    def getTeacher(self,course):
        query = "SELECT * FROM [teacher] WHERE [teacher_id] = (SELECT [teacher_id] FROM [courses] WHERE [course_code] = ?)"
        values = (course.code)
        self.cursor.execute(query, values)
        headers = (column[0] for column in self.cursor.description)
        teacher = self.cursor.fetchall()
        teacher = [headers] + teacher
        self.cursor.close()
        self.connection = None
        return teacher

    def getEnrollments(self,course):
        query = "SELECT * FROM [enrollments] WHERE [course_code] = ?"
        values = (course.code)
        self.cursor.execute(query, values)
        headers = (column[0] for column in self.cursor.description)
        enrollments = self.cursor.fetchall()
        enrollments = [headers] + enrollments
        self.cursor.close()
        self.connection = None
        return enrollments

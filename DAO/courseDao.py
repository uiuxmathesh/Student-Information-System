from Exceptions.custom_exceptions import *
from Util import DBConnUtil
class CourseDao(DBConnUtil):
        

    def assignTeacher(self, teacher, course): # WORKING GOOD AS EXPECTED
        # Prepare the query and values
        query = "UPDATE [course] SET [teacher_id] = ? WHERE [course_code] = ?"
        values = (teacher.teacherId, course.code)

        try:
            self.cursor.execute(query, values)

        # Handle the exception if the teacher is already assigned to the course
        except Exception as e:
            print(e)

        # If the assignment is successful, update the course object
        else:
            self.cursor.commit()
            return
            


    def updateCourseInfo(self,course): # WORKING GOOD AS EXPECTED

        query = "UPDATE [course] SET [course_name] = ?, [credits] = ?, [course_fee] = ?, [teacher_id] = ? WHERE [course_code] = ?"
        values = (course.name, course.credit, course.fee, course.teacherId, course.code)
        self.cursor.execute(query, values)
        self.cursor.commit()


    def displayCourseInfo(self,course): # WORKING GOOD AS EXPECTED
        query = "SELECT * FROM [course] WHERE [course_code] = ?"
        values = (course.code)
        self.cursor.execute(query, values)
        courseInfo = self.cursor.fetchone()
        # headers = tuple(column[0] for column in self.cursor.description)
        # courseInfo = [headers] + courseInfo
        return courseInfo

    def getTeacher(self,course): # WORKING GOOD AS EXPECTED
        query = "SELECT * FROM [teacher] WHERE [teacher_id] = (SELECT [teacher_id] FROM [course] WHERE [course_code] = ?)"
        values = (course.code)
        self.cursor.execute(query, values)
        headers = tuple(column[0] for column in self.cursor.description)
        teacher = self.cursor.fetchall()
        teacher = [headers] + teacher
        return teacher

    def getEnrollments(self,course): # WORKING GOOD AS EXPECTED
        query = "SELECT * FROM [enrollments] WHERE [course_code] = ?"
        values = (course.code)
        self.cursor.execute(query, values)
        headers = tuple(column[0] for column in self.cursor.description)
        enrollments = self.cursor.fetchall()
        enrollments = [headers] + enrollments
        return enrollments

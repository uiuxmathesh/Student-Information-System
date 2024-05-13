from Exceptions.custom_exceptions import *
from .teacherDao import TeacherDao
from Model import *
from Util import DBConnUtil
class CourseDao:
        

    def assignTeacher(self, teacher:Teacher, course:Course): # WORKING GOOD AS EXPECTED
        # Prepare the query and values
        query = "UPDATE [course] SET [teacher_id] = ? WHERE [course_code] = ?"
        values = (teacher.teacherId, course.code)

        # Initialize the teacherDao object
        teacherDao = TeacherDao()

        # Check if the course and teacher exist in the database
        if self.displayCourseInfo(course) == []:
            raise InvalidCourseDataException(f"Invalid Course Code {course.code}. Please enter a valid Course Code.")
        elif teacherDao.displayTeacherInfo(teacher) == []:
            raise TeacherNotFoundException(f"Teacher ID  {teacher.teacherId} not found. Please enter a valid Teacher ID.")

        self.connection = DBConnUtil.getConnection()
        self.cursor = self.connection.cursor()
        # If exists, assign the teacher to the course
        try:
            self.cursor.execute(query, values)

        # Handle the exception if the teacher is already assigned to the course
        except Exception as e:
            print(e)

        # If the assignment is successful, update the course object
        else:
            course.teacherId = teacher.teacherId

        # Commit the changes and close the cursor
        finally:
            self.cursor.commit()
            self.cursor.close()
            self.connection = DBConnUtil.closeConnection()
            return course


    def updateCourseInfo(self,course:Course): # WORKING GOOD AS EXPECTED
        self.connection = DBConnUtil.getConnection()
        self.cursor = self.connection.cursor()

        query = "UPDATE [course] SET [course_name] = ?, [credits] = ?, [course_fee] = ?, [teacher_id] = ? WHERE [course_code] = ?"
        values = (course.name, course.credit, course.fee, course.teacherId, course.code)
        self.cursor.execute(query, values)
        self.cursor.commit()
        self.cursor.close()
        self.connection = DBConnUtil.closeConnection()


    def displayCourseInfo(self,course:Course): # WORKING GOOD AS EXPECTED
        self.connection = DBConnUtil.getConnection()
        self.cursor = self.connection.cursor()
        query = "SELECT * FROM [course] WHERE [course_code] = ?"
        values = (course.code)
        self.cursor.execute(query, values)
        courseInfo = self.cursor.fetchall()
        # headers = tuple(column[0] for column in self.cursor.description)
        # courseInfo = [headers] + courseInfo
        self.cursor.close()
        self.connection = DBConnUtil.closeConnection()
        return courseInfo

    def getTeacher(self,course:Course): # WORKING GOOD AS EXPECTED
        self.connection = DBConnUtil.getConnection()
        self.cursor = self.connection.cursor()
        query = "SELECT * FROM [teacher] WHERE [teacher_id] = (SELECT [teacher_id] FROM [course] WHERE [course_code] = ?)"
        values = (course.code)
        self.cursor.execute(query, values)
        headers = tuple(column[0] for column in self.cursor.description)
        teacher = self.cursor.fetchall()
        teacher = [headers] + teacher
        self.cursor.close()
        self.connection = DBConnUtil.closeConnection()
        return teacher

    def getEnrollments(self,course:Course): # WORKING GOOD AS EXPECTED
        self.connection = DBConnUtil.getConnection()
        self.cursor = self.connection.cursor()
        query = "SELECT * FROM [enrollments] WHERE [course_code] = ?"
        values = (course.code)
        self.cursor.execute(query, values)
        headers = tuple(column[0] for column in self.cursor.description)
        enrollments = self.cursor.fetchall()
        enrollments = [headers] + enrollments
        self.cursor.close()
        self.connection = DBConnUtil.closeConnection()
        return enrollments

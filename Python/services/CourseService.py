from util.DBConnUtil import DBConnUtil
from exceptions.custom_exceptions import *
import pyodbc
from tabulate import tabulate 


class CourseService:

    def assign_teacher(self, course, teacher):
        query1 = "SELECT [teacher_id] FROM [teacher] WHERE [email] = ?"
        query2 = "SELECT [course_id] FROM [course] WHERE [course_code] = ?"
        query = "UPDATE [course] SET [teacher_id] = ? WHERE [course_id] = ?"
        connection = DBConnUtil.getConnection()
        cursor = connection.cursor()
        try:
            if teacher.email == "":
                raise InvalidTeacherDataException(f"Teacher-ID cannot be empty. Try giving a string instead")
            elif course.code == "":
                raise InvalidCourseDataException(f"Course-ID cannot be empty. Try giving a string instead")     
        except Exception as err:
            print(f"ERROR: {err}")
        else:
            try:
                cursor.execute(query1, (teacher.email))
                teacherID = cursor.fetchone()[0]
            except Exception as err:
                try:
                    raise TeacherNotFoundException(f"Teacher Email: {teacher.email} is not in database.")
                except Exception as err:
                    print(err)
            try:
                cursor.execute(query2,(course.code))
                courseID = cursor.fetchone()[0]
            except Exception as err:
                try:
                    raise CourseNotFoundException(f"Course code: {course.code} is not in database.")
                except Exception as err:
                    print(err)
            
        finally:
            connection.commit()
            connection = DBConnUtil.closeConnection()

    def create_course(self, course):
        query = "INSERT INTO [course] ([course_id], [course_name], [credits], [teacher_id]) VALUES (?, ?, ?, ?)"
        connection = DBConnUtil.getConnection()
        cursor = connection.cursor()
        try:
            if course.courseId == "":
                raise InvalidCourseDataException(f"TCourse Code cannot be empty. Try giving a string instead")
            elif course.name == "":
                raise InvalidCourseDataException(f"Course name cannot be empty. Try giving a string instead")
            elif course.credit <= 0:
                raise InvalidCourseDataException(f"Credit cannot be '0' or 'Negative' ")
            elif course.teacher_id == "":
                raise InvalidCourseDataException(f"Teacher-ID cannot be empty. Try giving a string instead")        
        except Exception as err:
            print(f"ERROR: {err}")
        else:
            try:
                cursor.execute(query, (course.courseId, course.name, course.credit, course.teacher_id))
            except pyodbc.IntegrityError as err:
                print(f"ERROR: Either Course-ID: '{course.courseId}' already exists in database or Associated Teacher-ID: '{course.teacher_id}' is Invalid ")
            else:
                cursor.commit()
        finally: 
            connection.commit()
            connection = DBConnUtil.closeConnection()
       
    def update_course(self, course):
        query = "UPDATE [course] SET [course_name] = ? , [credits] = ?, [teacher_id] = ? WHERE [course_id] = ?"
        connection = DBConnUtil.getConnection()
        cursor = connection.cursor()
        try:
            if course.courseId == "":
                raise InvalidCourseDataException(f"TCourse Code cannot be empty. Try giving a string instead")
            elif course.name == "":
                raise InvalidCourseDataException(f"Course name cannot be empty. Try giving a string instead")
            elif course.credit <= 0:
                raise InvalidCourseDataException(f"Credit cannot be '0' or 'Negative' ")
            elif course.teacher_id == "":
                raise InvalidCourseDataException(f"Teacher-ID cannot be empty. Try giving a string instead")        
        except Exception as err:
            print(f"ERROR: {err}")
        else:
            try:
                cursor.execute(query,( course.name, course.credit, course.teacher_id , course.courseId))
            except pyodbc.IntegrityError as err:
                print(f"ERROR: Either Course-ID: '{course.courseId}' already exists in database or Associated Teacher-ID: '{course.teacher_id}' is Invalid ")
            else:
                cursor.commit()
        finally: 
            connection.commit()
            connection = DBConnUtil.closeConnection()
        # query = "SELECT [teacher_id] FROM [teacher] WHERE CONCAT(first_name, ' ', last_name) = ?"
        # connection = DBConnUtil.getConnection()
        # cursor = connection.cursor()
        # cursor.execute(query, (course.instructor_name))
        # id = []
        # for row in cursor:
        #     id = [*row][0]

    def display_course_info(self, course):
        query = "SELECT * FROM [course] WHERE [course_id] = ?"
        connection = DBConnUtil.getConnection()
        cursor = connection.cursor()
        try:
            if course.courseId == "":
                raise InvalidCourseDataException("Enter a valid Course-ID to fetch records")
        except Exception as e:
            print(f"ERROR: Unable to fetch records {e}")
        else:
            cursor.execute(query, (course.courseId))
            heading = [column[0] for column in cursor.description]
            rows = cursor.fetchall()
            rows = [ [*row] for row in rows ]
            table = [heading, *rows]
            print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
        finally:
            connection = DBConnUtil.closeConnection()

    def get_Enrollments(self, course):#MARKED FOR REVIEW
        query = """SELECT	course.course_id,
		                    course.course_name,
		                    students.student_id,
		                    students.first_name,
		                    students.last_name,
		                    enrollments.enrollment_id
                    FROM	[course]
		                    INNER JOIN [enrollments] ON course.course_id = enrollments.course_id
		                    INNER JOIN [students] ON students.student_id = enrollments.student_id
                    WHERE   course.course_id = ? """
        connection = DBConnUtil.getConnection()
        cursor = connection.cursor()
        try:
            if course.courseId == "":
                raise InvalidCourseDataException("Enter a valid Course-ID to fetch records")
        except Exception as e:
            print(f"ERROR: Unable to fetch records {e}")
        else:
            cursor.execute(query, (course.courseId))
            heading = [column[0] for column in cursor.description]
            rows = cursor.fetchall()
            rows = [ [*row] for row in rows ]
            table = [heading, *rows]
            print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
        finally:
            connection = DBConnUtil.closeConnection()

    def get_Teacher(self,course):
        query = """SELECT	[course_name],
		                    teacher.*
                            FROM	course
		                    INNER JOIN teacher ON course.teacher_id = teacher.teacher_id
                            WHERE	course.course_id = ? """
        connection = DBConnUtil.getConnection()
        cursor = connection.cursor()
        try:
            if course.courseId == "":
                raise InvalidCourseDataException("Enter a valid Course-ID to fetch records")
        except Exception as e:
            print(f"ERROR: Unable to fetch records {e}")
        else:
            cursor.execute(query, (course.courseId))
            heading = [column[0] for column in cursor.description]
            rows = cursor.fetchall()
            rows = [ [*row] for row in rows ]
            table = [heading, *rows]
            print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
        finally:
            connection = DBConnUtil.closeConnection()


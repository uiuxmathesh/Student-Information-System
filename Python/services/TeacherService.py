from util.DBConnUtil import DBConnUtil
from exceptions.custom_exceptions import *
from tabulate import tabulate
import pyodbc


class TeacherService:
        
    def create_teacher(self,teacher):
        query = "INSERT INTO [teacher] ([teacher_id], [first_name], [last_name], [email]) VALUES (?, ?, ?, ?)"
        connection = DBConnUtil.getConnection()
        cursor = connection.cursor()
        try:
            if teacher.teacherId == "":
                raise InvalidTeacherDataException(f"Teacher-ID cannot be empty. Try giving a string instead")
            elif teacher.fname == "":
                raise InvalidTeacherDataException(f"First-name cannot be empty. Try giving a string instead")
            elif teacher.lname == "":
                raise InvalidTeacherDataException(f"Last-name cannot be empty. Try giving a string instead")
            elif teacher.email == "":
                raise InvalidTeacherDataException(f"Email cannot be empty. Try giving a string instead")        
        except Exception as err:
            print(f"ERROR: {err}")
        else:
            try:
                cursor.execute(query, (teacher.teacherId, teacher.fname, teacher.lname, teacher.email))
            except pyodbc.IntegrityError as err:
                print(f"Teacher-ID: {teacher.teacherId} already exists in database.")
        finally:
            connection.commit()
            connection = DBConnUtil.closeConnection()
    
    def update_teacher(self,teacher):
        query = "UPDATE [teacher] SET [first_name] = ?, [last_name] = ?, [email] = ? WHERE [teacher_id] = ?"
        connection = DBConnUtil.getConnection()
        cursor = connection.cursor()
        try:
            if teacher.teacherId == "":
                raise InvalidTeacherDataException(f"Teacher-ID cannot be empty. Try giving a string instead")
            elif teacher.fname == "":
                raise InvalidTeacherDataException(f"First-name cannot be empty. Try giving a string instead")
            elif teacher.lname == "":
                raise InvalidTeacherDataException(f"Last-name cannot be empty. Try giving a string instead")
            elif teacher.email == "":
                raise InvalidTeacherDataException(f"Email cannot be empty. Try giving a string instead")        
        except Exception as err:
            print(f"ERROR: {err}")
        else:
            try:
                cursor.execute(query, (teacher.fname, teacher.lname, teacher.email, teacher.teacherId))
            except pyodbc.IntegrityError as err:
                print(f"Teacher-ID: {teacher.teacherId} already exists in database.")
        finally:
            connection.commit()
            connection = DBConnUtil.closeConnection()

    def display_teacher_info(self, teacher):
        connection = DBConnUtil.getConnection()
        cursor = connection.cursor()
        query = "SELECT * FROM [teacher] WHERE [teacher_id] = ?"
        try:
            if teacher.teacherId == "":
                raise InvalidTeacherDataException("Enter a valid Teacher-ID to fetch records")
        except Exception as e:
            print(f"ERROR: Unable to fetch records {e}")
        else:
            cursor.execute(query, (teacher.teacherId))
            heading = [column[0] for column in cursor.description]
            rows = cursor.fetchall()
            rows = [ [*row] for row in rows ]
            table = [heading, *rows]
            print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
        finally:
            connection = DBConnUtil.closeConnection()

    def get_assigned_courses(self, teacher):
        query = """
                SELECT	*
                FROM	[course]
                        INNER JOIN [teacher] ON course.teacher_id = teacher.teacher_id
                WHERE	teacher.teacher_id = ?
                """
        connection = DBConnUtil.getConnection()
        cursor = connection.cursor()
        try:
            if teacher.teacherId == "":
                raise InvalidTeacherDataException("Enter a valid Teacher-ID to fetch records")
        except Exception as e:
            print(f"ERROR: Unable to fetch records {e}")
        else:
            cursor.execute(query, (teacher.teacherId))
            heading = [column[0] for column in cursor.description]
            rows = cursor.fetchall()
            rows = [ [*row] for row in rows ]
            table = [heading, *rows]
            print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
        finally:
            connection = DBConnUtil.closeConnection()
      
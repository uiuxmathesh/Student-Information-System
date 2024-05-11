from util.DBConnUtil import DBConnUtil
from exceptions.custom_exceptions import *
import pyodbc
from tabulate import tabulate

class EnrollmentService:

    def get_student_details(self,enrollment):
        query = """
        SELECT	*
        FROM	[students]
        WHERE	[student_id] = (
                                SELECT	[student_id]
                                FROM	[enrollments]
						        WHERE	[enrollment_id] = ?)"""
        connection = DBConnUtil.getConnection()
        cursor = connection.cursor()
        cursor.execute(query, (enrollment.enrollmentId)).fetchall()
        heading = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        rows = [ [*row] for row in rows ]
        table = [heading, *rows]
        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
        connection = DBConnUtil.closeConnection()

    def get_course_details(self,enrollment):
        query = """
        SELECT	*
        FROM	[course]
        WHERE	[course_id] = (
                                SELECT	[course_id]
                                FROM	[enrollments]
						        WHERE	[enrollment_id] = ?)"""
        connection = DBConnUtil.getConnection()
        cursor = connection.cursor()
        cursor.execute(query, (enrollment.enrollmentId)).fetchall()
        heading = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        rows = [ [*row] for row in rows ]
        table = [heading, *rows]
        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
        connection = DBConnUtil.closeConnection()


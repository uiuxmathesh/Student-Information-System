# from model.model import *
from DBConnUtil import DBConnUtil
from datetime import datetime
# from model import *

class StudentServices:

    def create_student(self, student):
        connection = DBConnUtil.getConnection()
        cursor = connection.cursor()
        query = "INSERT INTO students([student_id],[first_name],[last_name],[date_of_birth],[email],[phone_number]) VALUES (?,?,?,?,?,?)"
        cursor.execute(query, (student.studentId ,student.fname, student.lname, f'{student.dob.year}-{student.dob.month}-{student.dob.day}', student.email, student.phone))
        connection.commit()
        connection = DBConnUtil.closeConnection()
    
    def update_student(self,student):
        query = "UPDATE students SET [first_name] = ?, [last_name] = ?, [date_of_birth] = ?, [email] = ?, [phone_number] = ? WHERE [student_id] = ?"
        connection = DBConnUtil.getConnection()
        cursor = connection.cursor()
        cursor.execute(query, (student.fname, student.lname, f'{student.dob.year}-{student.dob.month}-{student.dob.day}', student.email, student.phone, student.studentId))
        connection.commit()
        connection = DBConnUtil.closeConnection()
    
    def display_student_info(self, student):
        query = "SELECT * FROM [students] WHERE [student_id] = ?"
        connection = DBConnUtil.getConnection()
        cursor = connection.cursor()
        cursor = connection.cursor()
        cursor.execute(query, (student.studentId))
        heading = [column[0] for column in cursor.description]
        rows = cursor.fetchall()[0] 
        result = dict(zip(heading,rows))
        for columnName,value in result.items():
            print(f"{columnName}:  {value}")
        connection = DBConnUtil.closeConnection()

    def enroll_in_course(self, enrollment):
        # date = f"{date.year}-{date.month}-{date.day}"
        query = "INSERT INTO [enrollments]([student_id],[course_id],[enrollment_date]) VALUES (?,?,?)"
        connection = DBConnUtil.getConnection()
        cursor = connection.cursor()
        cursor = connection.cursor()
        cursor.execute(query, (enrollment.studentId, enrollment.courseId, enrollment.enrollmentDate))
        cursor.commit()
        connection.commit()
        connection = DBConnUtil.closeConnection()

    def make_payment(self,payment):
        query ="INSERT INTO [payments] ([student_id],[amount],[payment_date]) VALUES (?,?,?)"
        connection = DBConnUtil.getConnection()
        cursor = connection.cursor()
        cursor = connection.cursor()
        cursor.execute(query, (payment.studentId, payment.amount, payment.paymentDate))
        cursor.commit()
        connection.commit()
        connection = DBConnUtil.closeConnection()

    def list_enrolled_courses(self, student):
        query ="""
                    SELECT	enrollment_id,course.*, enrollment_date
                    FROM	[enrollments]
                    INNER JOIN [course] ON enrollments.course_id = course.course_id
                    WHERE enrollments.student_id = ? """
        connection = DBConnUtil.getConnection()
        cursor = connection.cursor()
        cursor = connection.cursor()
        cursor.execute(query, (student.studentId))
        heading = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        print(heading)
        for row in rows:
            print(row)

    def list_payment_history(self, student):
        query = "SELECT * FROM [payments] WHERE [student_id] = ?"
        connection = DBConnUtil.getConnection()
        cursor = connection.cursor()
        cursor = connection.cursor()
        cursor.execute(query, (student.studentId))
        heading = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        print(heading)
        for row in rows:
            print(row)
        
class TeacherService:
        
    def create_teacher(self,teacher):
        query = "INSERT INTO [teacher] ([teacher_id], [first_name], [last_name], [email]) VALUES (?, ?, ?, ?)"
        connection = DBConnUtil.getConnection()
        cursor = connection.cursor()
        cursor.execute(query, (teacher.teacherId, teacher.fname, teacher.lname, teacher.email))
        connection.commit()
        connection = DBConnUtil.closeConnection()
    
    def update_teacher(self,teacher):
        query = "UPDATE [teacher] SET [first_name] = ?, [last_name] = ?, [email] = ? WHERE [teacher_id] = ?"
        connection = DBConnUtil.getConnection()
        cursor = connection.cursor()
        cursor.execute(query, (teacher.fname, teacher.lname, teacher.email, teacher.teacherId))
        connection.commit()
        connection = DBConnUtil.closeConnection()

    def display_teacher_info(self, teacher):
        query = "SELECT * FROM [teacher] WHERE [teacher_id] = ?"
        connection = DBConnUtil.getConnection()
        cursor = connection.cursor()
        cursor = connection.cursor()
        cursor.execute(query, (teacher.teacherId))
        heading = [column[0] for column in cursor.description]
        rows = cursor.fetchall()[0] 
        result = dict(zip(heading,rows))
        for columnName,value in result.items():
            print(f"{columnName}:  {value}")
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
        cursor = connection.cursor()
        cursor.execute(query, (teacher.teacherId))
        rows = cursor.fetchall()[0]
        heading = [column[0] for column in cursor.description]
        result = dict(zip(heading,rows))
        for columnName,value in result.items():
            print(f"{columnName}:  {value}")
        connection = DBConnUtil.closeConnection()
        
class CourseService:

    def assign_teacher(self, course, teacher):
        query = "UPDATE [course] SET [teacher_id] = ? WHERE [course_id] = ?"
        connection = DBConnUtil.getConnection()
        cursor = connection.cursor()
        cursor.execute(query, (teacher.teacherId,course.courseId))
        cursor.commit()
        connection.commit()
        print("Assigned Successfully")
        connection = DBConnUtil.closeConnection()

    def create_course(self, course):
        query = "INSERT INTO [course] ([course_id], [course_name], [credits], [teacher_id]) VALUES (?, ?, ?, ?)"
        connection = DBConnUtil.getConnection()
        cursor = connection.cursor()
        cursor.execute(query, (course.courseId, course.name, course.credit, course.teacher_id))
        cursor.commit()
        connection.commit()
        connection = DBConnUtil.closeConnection()

    def update_course(self, course):
        query = "UPDATE [course] SET [course_name] = ? , [credits] = ?, [teacher_id] = ? WHERE [course_id] = ?"
        connection = DBConnUtil.getConnection()
        cursor = connection.cursor()
        cursor.execute(query, ( course.name, course.credit, course.teacher_id , course.courseId))
        cursor.commit()
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
        cursor = connection.cursor()
        cursor.execute(query, (course.courseId))
        heading = [column[0] for column in cursor.description]
        rows = cursor.fetchall()[0] 
        result = dict(zip(heading,rows))
        for columnName,value in result.items():
            print(f"{columnName}:  {value}")
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
        cursor.execute(query, (course.courseId))
        result = []
        for column in cursor.execute(query, (course.courseId)).fetchall():
            result.append(column)
        result = [*result]
        heading = [column[0] for column in cursor.description]
        cursor.commit()
        connection.commit()
        connection = DBConnUtil.closeConnection()

    def get_Teacher(self,course):
        query = """SELECT	[course_name],
		                    teacher.*
                            FROM	course
		                    INNER JOIN teacher ON course.teacher_id = teacher.teacher_id
                            WHERE	course.course_id = ? """
        connection = DBConnUtil.getConnection()
        cursor = connection.cursor()
        result = None
        for column in cursor.execute(query, (course.courseId)).fetchall():
            result = column 
        result = [*result]
        heading = [column[0] for column in cursor.description]
        
        result = dict(zip(heading,result))
        for columnName,value in result.items():
            print(f"{columnName}:  {value}")
        connection = DBConnUtil.closeConnection()


class PaymentService:

    def get_student_details(self, payment):
        query = """
        SELECT	*
        FROM	[students]
        WHERE	[student_id] = (
                                SELECT	[student_id]
                                FROM	[payments]
						        WHERE	[payment_id] = ?)"""
        connection = DBConnUtil.getConnection()
        cursor = connection.cursor()
        result = None
        for column in cursor.execute(query, (payment.paymentId)).fetchall():
            result = column 
        result = [*result]
        heading = [column[0] for column in cursor.description]
        
        result = dict(zip(heading,result))
        for columnName,value in result.items():
            print(f"{columnName}:  {value}")
        connection = DBConnUtil.closeConnection()

    def get_payment_amount(self, payment):
        query = """
                SELECT	[amount]
                FROM	[payments]
				WHERE	[payment_id] = ?"""
        connection = DBConnUtil.getConnection()
        cursor = connection.cursor()
        result = None
        for column in cursor.execute(query, (payment.paymentId)).fetchall():
            result = column 
        result = [*result]
        heading = [column[0] for column in cursor.description]
        
        result = dict(zip(heading,result))
        for columnName,value in result.items():
            print(f"{columnName}:  {value}")
        connection = DBConnUtil.closeConnection()

    def get_payment_date(self, payment):
        query = """
                SELECT	[payment_date]
                FROM	[payments]
				WHERE	[payment_id] = ?"""
        connection = DBConnUtil.getConnection()
        cursor = connection.cursor()
        result = None
        for column in cursor.execute(query, (payment.paymentId)).fetchall():
            result = column 
        result = [*result]
        heading = [column[0] for column in cursor.description]
        
        result = dict(zip(heading,result))
        for columnName,value in result.items():
            print(f"{columnName}:  {value}")
        connection = DBConnUtil.closeConnection()


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
        result = None
        for column in cursor.execute(query, (enrollment.enrollmentId)).fetchall():
            result = column 
        result = [*result]
        heading = [column[0] for column in cursor.description]
        
        result = dict(zip(heading,result))
        for columnName,value in result.items():
            print(f"{columnName}:  {value}")
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
        result = None
        for column in cursor.execute(query, (enrollment.enrollmentId)).fetchall():
            result = column 
        result = [*result]
        heading = [column[0] for column in cursor.description]
        
        result = dict(zip(heading,result))
        for columnName,value in result.items():
            print(f"{columnName}:  {value}")
        connection = DBConnUtil.closeConnection()
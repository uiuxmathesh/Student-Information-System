# from model.model import *
from DBConnUtil import DBConnUtil
from datetime import datetime
from custom_exceptions import *
import pyodbc
# from model import *

class StudentServices:

    def create_student(self, student):
        connection = DBConnUtil.getConnection()
        cursor = connection.cursor() 
        try:
            if student.studentId == "":
                raise InvalidStudentDataException("Student-ID cannot be empty")
            elif student.fname == "":
                raise InvalidStudentDataException("First-name cannot be empty")
            elif student.lname == "":
                raise InvalidStudentDataException("Last-name cannot be empty")
            elif student.email == "":
                raise InvalidStudentDataException("Email-ID cannot be empty")
            elif student.phone == "":
                raise InvalidStudentDataException("Phone number cannot be empty")
        except Exception as err:
            print(f"ERROR: {err}")
        else:
            try:
                query = "INSERT INTO students([student_id],[first_name],[last_name],[date_of_birth],[email],[phone_number]) VALUES (?,?,?,?,?,?)"
                cursor.execute(query, (student.studentId ,student.fname, student.lname, student.dob, student.email, student.phone)) 
            except pyodbc.IntegrityError as err:
                print(f"{student.studentId} already exists in Database. Try updating or deleting {student.studentId} from Database")
        finally:
            connection.commit()
            connection = DBConnUtil.closeConnection()           
    
    def update_student(self,student):
        connection = DBConnUtil.getConnection()
        cursor = connection.cursor()
        try:
            if student.studentId == "":
                raise InvalidStudentDataException("Student-ID cannot be empty")
            elif student.fname == "":
                raise InvalidStudentDataException("First-name cannot be empty")
            elif student.lname == "":
                raise InvalidStudentDataException("Last-name cannot be empty")
            elif student.email == "":
                raise InvalidStudentDataException("Email-ID cannot be empty")
            elif student.phone == "":
                raise InvalidStudentDataException("Phone number cannot be empty")
        except Exception as err:
            print(f"ERROR: {err}")
        else:
            try:
                query = "UPDATE students SET [first_name] = ?, [last_name] = ?, [date_of_birth] = ?, [email] = ?, [phone_number] = ? WHERE [student_id] = ?"
                cursor.execute(query, (student.fname, student.lname, student.dob, student.email, student.phone, student.studentId)) 
            except pyodbc.IntegrityError as err:
                print(f"{student.studentId} doesn't exist in Database. Try inserting to Database")
        finally:
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
        successFlag = False
        query = "INSERT INTO [enrollments]([student_id],[course_id],[enrollment_date]) VALUES (?,?,?)"
        connection = DBConnUtil.getConnection()
        cursor = connection.cursor()
        try:
            if enrollment.studentId == "":
                raise InvalidEnrollmentDataException(f"Give a Student-ID to for enrollment")
            elif enrollment.courseId == "":
                raise InvalidEnrollmentDataException(f"Give a Course-ID to for enrollment")    
            
        except Exception as err:

            print(f"ERROR: {err}")

        else:
            try:
                cursor.execute(query, (enrollment.studentId, enrollment.courseId, enrollment.enrollmentDate))
            except pyodbc.Error as e:
                if e.args[0] == '23000':
                    if e.args[1].find('FOREIGN KEY') != -1:
                        try:
                            if e.args[1].find('"student_fk"') != -1:
                                raise StudentNotFoundException(f"Invalid Student-ID {enrollment.studentId}")
                            else:
                                raise CourseNotFoundException(f"Invalid course-ID {enrollment.courseId}")
                            
                        except Exception as e:
                            print(e)

                    else:
                        try:
                            raise DuplicateEnrollmentException("Enrollment Already Exists. Try Checking in Enrollment menu")
                        except Exception as err:
                            print(err)
            else:
                successFlag = True
                        
        finally: 
            connection.commit()
            connection = DBConnUtil.closeConnection()
            return successFlag

    def make_payment(self,payment):
        query ="INSERT INTO [payments] ([student_id],[amount],[payment_date]) VALUES (?,?,?)"
        connection = DBConnUtil.getConnection()
        cursor = connection.cursor()
        try:
            if payment.studentId == "":
                raise InvalidStudentDataException(f"Give a Student-ID to make payment")
            elif payment.amount <= 100:
                raise InsufficientFundsException(f"Payment amounts cannot be less than Rs.100")    
        except Exception as err:
            print(f"ERROR: {err}")
        else:
            
            try:
                cursor.execute(query, (payment.studentId, payment.amount, payment.paymentDate))
            except pyodbc.IntegrityError as err:
                try:
                    sqlState = err.args[0]
                    if(sqlState == '23000'):
                        raise StudentNotFoundException(f"Student-ID {payment.studentId} is Invalid")
                except Exception as e:
                    try:
                        raise PaymentValidationException(f"Failed to Validate payment: {e}")
                    except Exception as e:
                        print(e)
            else:
                cursor.commit()
        finally: 
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
            rows = cursor.fetchall()[0] 
            result = dict(zip(heading,rows))
            for columnName,value in result.items():
                print(f"{columnName}:  {value}")
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
            rows = cursor.fetchall()[0] 
            result = dict(zip(heading,rows))
            for columnName,value in result.items():
                print(f"{columnName}:  {value}")
        finally:
            connection = DBConnUtil.closeConnection()
        
class CourseService:

    def assign_teacher(self, course, teacher):
        query = "UPDATE [course] SET [teacher_id] = ? WHERE [course_id] = ?"
        connection = DBConnUtil.getConnection()
        cursor = connection.cursor()
        try:
            if teacher.teacherId == "":
                raise InvalidTeacherDataException(f"Teacher-ID cannot be empty. Try giving a string instead")
            elif course.courseId == "":
                raise InvalidCourseDataException(f"Course-ID cannot be empty. Try giving a string instead")     
        except Exception as err:
            print(f"ERROR: {err}")
        else:
            try:
                cursor.execute(query, (teacher.teacherId,course.courseId))
            except pyodbc.Error as err:
                try:
                    raise TeacherNotFoundException(f"Teacher-ID: {teacher.teacherId} is not in database.")
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
            rows = cursor.fetchall()[0] 
            result = dict(zip(heading,rows))
            for columnName,value in result.items():
                print(f"{columnName}:  {value}")
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
            rows = cursor.fetchall()[0] 
            result = dict(zip(heading,rows))
            for columnName,value in result.items():
                print(f"{columnName}:  {value}")
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
            rows = cursor.fetchall()[0] 
            result = dict(zip(heading,rows))
            for columnName,value in result.items():
                print(f"{columnName}:  {value}")
        finally:
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
        try:
            if payment.paymentId == "":
                raise InvalidPaymentDataException("Enter a valid payment-ID to fetch records")
        except Exception as e:
            print(f"ERROR: Unable to fetch records {e}")
        else:
            cursor.execute(query, (payment.paymentId))
            heading = [column[0] for column in cursor.description]
            rows = cursor.fetchone() 
            result = dict(zip(heading,rows))
            for columnName,value in result.items():
                print(f"{columnName}:  {value}")
        finally:
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
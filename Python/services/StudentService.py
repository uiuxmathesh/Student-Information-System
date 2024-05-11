from util.DBConnUtil import DBConnUtil
from exceptions.custom_exceptions import *
from tabulate import tabulate

import pyodbc

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
        rows = list(cursor.fetchone()) 

        table = [heading,rows]
        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
        # result = dict(zip(heading,rows))
        # for columnName,value in result.items():
        #     print(f"{columnName}:  {value}")
        connection = DBConnUtil.closeConnection()

    def enroll_in_course(self, enrollment):
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
        rows = [ [*row] for row in rows ]
        table = [heading, *rows]
        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
        # print(heading)
        # for row in rows:
        #     print(row)
        connection = DBConnUtil.closeConnection()

    def list_payment_history(self, student):
        query = "SELECT * FROM [payments] WHERE [student_id] = ?"
        connection = DBConnUtil.getConnection()
        cursor = connection.cursor()
        cursor = connection.cursor()
        cursor.execute(query, (student.studentId))
        heading = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        rows = [ [*row] for row in rows ]
        table = [heading, *rows]
        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
        # print(heading)
        # for row in rows:
        #     print(row)
        connection = DBConnUtil.closeConnection()
 
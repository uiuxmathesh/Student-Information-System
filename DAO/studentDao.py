from datetime import datetime

class studentDao:

    def __init__(self):
        self.connection = None
        self.cursor = self.connection.cursor()

    def enrollInCourse(self,student, course):
        query = "INSERT INTO enrollments ([student_id], [course_code], [enrollment_date]) VALUES (?, ?, ?)"
        values = (student.studentId, course.code, str(datetime.now().date().strftime('%Y-%m-%d')))
        self.cursor.execute(query, values)
        query = "SELECT IDENT_CURRENT('enrollments')"
        self.cursor.execute(query)
        enrollmentId = self.cursor.fetchone()[0]
        self.cursor.commit()
        self.cursor.close()
        self.connection = None   #After Implementing the method, close the connection
        return enrollmentId

    def updateStudentInfo(self,student):
        if self.displayStudentInfo(student) == []:
            pass
        query ="UPDATE students SET [first_name] = ?, [last_name] = ?, [date_of_birth] = ?, [email] = ?, [phone_number] = ? WHERE [student_id] = ?"
        values = (student.fname, student.lname, student.dob, student.email, student.phone, student.studentId)
        self.cursor.execute(query, values)
        self.cursor.commit()
        self.cursor.close()
        self.connection = None   #After Implementing the method, close the connection        

    def makePayment(self,payment):
        query = "INSERT INTO payments ([student_id], [amount], [payment_date]) VALUES (?, ?, ?)"
        values = (payment.studentId, payment.amount, payment.paymentDate)
        self.cursor.execute(query, values)  
        query = "SELECT IDENT_CURRENT('payments')"
        self.cursor.execute(query)  
        paymentId = self.cursor.fetchone()[0]
        self.cursor.commit()
        self.cursor.close() 
        self.connection = None
        return paymentId

    def displayStudentInfo(self,student):
        query = "SELECT * FROM students WHERE [student_id] = ?"
        values = (student.studentId)
        self.cursor.execute(query, values)
        studentInfo = self.cursor.fetchall()
        self.cursor.close()
        self.connection = None
        return studentInfo

    def getEnrolledCourses(self,student):
        query = "SELECT * FROM enrollments WHERE [student_id] = ?"
        values = (student.studentId)
        self.cursor.execute(query, values)
        enrolledCourses = self.cursor.fetchall()
        self.cursor.close()
        self.connection = None
        return enrolledCourses

    def getPayments(self,student):
        query = "SELECT * FROM payments WHERE [student_id] = ?"
        values = (student.studentId)
        self.cursor.execute(query, values)
        payments = self.cursor.fetchall()
        self.cursor.close()
        self.connection = None
        return payments



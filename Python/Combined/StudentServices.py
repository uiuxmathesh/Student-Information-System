# from model.model import *
from DBConnUtil import DBConnUtil
from model import Student

class StudentServices:

    def create_student(self, student:Student):
        connection = DBConnUtil.getConnection()
        cursor = connection.cursor()
        query = "INSERT INTO students([first_name],[last_name],[date_of_birth],[email],[phone_number]) VALUES (?,?,?,?,?)"
        cursor.execute(query, (student.fname, student.lname, f'{student.dob.year}-{student.dob.month}-{student.dob.day}', student.email, student.phone))
        connection.commit()

        
    
    def update_enrolled_courses():
        pass



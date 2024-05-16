from Exceptions.custom_exceptions import InvalidTeacherDataException, TeacherNotFoundException
from Util import DBConnUtil
class TeacherDao(DBConnUtil):

    def addTeacher(self,teacher): # WORKING GOOD AS EXPECTED
        try:
            query = "INSERT INTO teacher ([teacher_id], [first_name], [last_name], [email], [expertise]) VALUES (?, ?, ?, ?, ?)"
            values = (teacher.teacherId, teacher.fname, teacher.lname, teacher.email, teacher.expertise)
            self.cursor.execute(query, values)
            self.cursor.commit()
        except Exception as e:
            print(e)
        print("Teacher added successfully")

    def updateTeacherInfo(self,teacher): # WORKING GOOD AS EXPECTED
        query = "UPDATE [teacher] SET [first_name] =?, [last_name] = ?, email = ?, [expertise] = ? WHERE [teacher_id] = ?"
        values = (teacher.fname, teacher.lname, teacher.email, teacher.expertise, teacher.teacherId)
        if len(self.displayTeacherInfo(teacher)) == 0:
            raise InvalidTeacherDataException(f"Invalid Teacher ID {teacher.teacherId}. Please enter a valid Teacher ID.")
        else:
            self.cursor.execute(query, values)
            self.cursor.commit() 

    def displayTeacherInfo(self,teacher): # WORKING GOOD AS EXPECTED
        query = "SELECT * FROM [teacher] WHERE [teacher_id] = ?"
        values = (teacher.teacherId,)
        self.cursor.execute(query, values)
        teacherInfo = self.cursor.fetchone()
        if teacherInfo == None:
            raise TeacherNotFoundException(f"Invalid Teacher ID {teacher.teacherId}. Please enter a valid Teacher ID.")
        header = self.cursor.description
        header = tuple(column[0] for column in header)
        teacherInfo = [header, teacherInfo]
        return teacherInfo

    def getAssignedCourses(self,teacher): # WORKING GOOD AS EXPECTED
        query = """
        SELECT 	teacher.teacher_id,
                teacher.first_name,
                teacher.last_name,
                course.course_code,
                course.course_name
        FROM	[course]
                INNER JOIN [teacher] ON teacher.teacher_id = course.teacher_id
        WHERE	teacher.teacher_id = ?

                """
        values = (teacher.teacherId)
        self.cursor.execute(query, values)
        assignedCourses = self.cursor.fetchall()
        headers = self.cursor.description
        headers = tuple(header[0] for header in headers)
        assignedCourses = [headers, *assignedCourses]
        return assignedCourses
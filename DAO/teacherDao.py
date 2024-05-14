from Exceptions.custom_exceptions import InvalidTeacherDataException
from Util import DBConnUtil
class TeacherDao(DBConnUtil):


    def updateTeacherInfo(self,teacher): # WORKING GOOD AS EXPECTED
        query = "UPDATE [teacher] SET [first_name] =?, [last_name] = ?, email = ?, [expertise] = ? WHERE [teacher_id] = ?"
        values = (teacher.fname, teacher.lname, teacher.email, teacher.expertise, teacher.teacherId)
        if self.displayTeacherInfo(teacher) == []:
            raise InvalidTeacherDataException(f"Invalid Teacher ID {teacher.teacherId}. Please enter a valid Teacher ID.")
        self.cursor.execute(query, values)
        self.cursor.commit()    

    def displayTeacherInfo(self,teacher): # WORKING GOOD AS EXPECTED
        query = "SELECT * FROM [teacher] WHERE [teacher_id] = ?"
        values = (teacher.teacherId,)
        self.cursor.execute(query, values)
        teacherInfo = self.cursor.fetchone()
        return teacherInfo

    def getAssignedCourses(self,teacher): # WORKING GOOD AS EXPECTED
        query = "SELECT * FROM [course] WHERE [teacher_id] = ?"
        values = (teacher.teacherId)
        self.cursor.execute(query, values)
        assignedCourses = self.cursor.fetchall()
        return assignedCourses
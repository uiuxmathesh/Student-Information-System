from Util import DBConnUtil
from Model import *

class TeacherDao:


    def updateTeacherInfo(self,teacher): # WORKING GOOD AS EXPECTED
        self.connection = DBConnUtil.getConnection()
        self.cursor = self.connection.cursor()
        query = "UPDATE [teacher] SET [first_name] =?, [last_name] = ?, email = ?, [expertise] = ? WHERE [teacher_id] = ?"
        values = (teacher.fname, teacher.lname, teacher.email, teacher.expertise, teacher.teacherId)
        self.cursor.execute(query, values)
        self.cursor.commit()    
        self.cursor.close()
        self.connection = DBConnUtil.closeConnection()

    def displayTeacherInfo(self,teacher:Teacher): # WORKING GOOD AS EXPECTED
        self.connection = DBConnUtil.getConnection()
        self.cursor = self.connection.cursor()
        query = "SELECT * FROM [teacher] WHERE [teacher_id] = ?"
        values = (teacher.teacherId,)
        self.cursor.execute(query, values)
        teacherInfo = self.cursor.fetchall()
        # headers = (column[0] for column in self.cursor.description)
        # teacherInfo = [headers] + teacherInfo
        self.cursor.close()
        self.connection = DBConnUtil.closeConnection()
        return teacherInfo

    def getAssignedCourses(self,teacher): # WORKING GOOD AS EXPECTED
        self.connection = DBConnUtil.getConnection()
        self.cursor = self.connection.cursor()
        query = "SELECT * FROM [course] WHERE [teacher_id] = ?"
        values = (teacher.teacherId)
        self.cursor.execute(query, values)
        assignedCourses = self.cursor.fetchall()
        # headers = (column[0] for column in self.cursor.description)
        # assignedCourses = [headers] + assignedCourses
        self.cursor.close()
        self.connection = DBConnUtil.closeConnection()
        return assignedCourses
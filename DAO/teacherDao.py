

class TeacherDao:

    def __init__(self):
        self.connection = None
        self.cursor = self.connection.cursor()  

    def updateTeacherInfo(self,teacher):
        query = "UPDATE [teacher] SET [first_name] =?, [last_name] = ?, email = ?, [expertise] = ? WHERE [teacher_id] = ?"
        values = (teacher.fname, teacher.lname, teacher.email, teacher.expertise, teacher.teacherId)
        self.cursor.execute(query, values)
        self.cursor.commit()    
        self.cursor.close()
        self.connection = None

    def displayTeacherInfo(self,teacher):
        query = "SELECT * FROM [teacher] WHERE [teacher_id] = ?"
        values = (teacher.teacherId)
        self.cursor.execute(query, values)
        teacherInfo = self.cursor.fetchall()
        headers = (column[0] for column in self.cursor.description)
        teacherInfo = [headers] + teacherInfo
        self.cursor.close()
        self.connection = None
        return teacherInfo

    def getAssignedCourses(self,teacher):
        query = "SELECT * FROM [courses] WHERE [teacher_id] = ?"
        values = (teacher.teacherId)
        self.cursor.execute(query, values)
        headers = (column[0] for column in self.cursor.description)
        assignedCourses = self.cursor.fetchall()
        assignedCourses = [headers] + assignedCourses
        self.cursor.close()
        self.connection = None
        return assignedCourses
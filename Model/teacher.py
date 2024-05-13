
class Teacher:
    def __init__(self):
        self.teacherId = None
        self.fname = None
        self.lname = None
        self.email = None
        self.expertise = None

    @property
    def teacherId(self):
        return self.teacherId
    
    @teacherId.setter
    def teacherId(self, teacherId):
        self.teacherId = teacherId

    @property
    def fname(self):
        return self.fname
    
    @fname.setter
    def fname(self, fname):
        self.fname = fname

    @property
    def lname(self):
        return self.lname
    
    @lname.setter
    def lname(self, lname):
        self.lname = lname

    @property
    def email(self):
        return self.email
    
    @email.setter
    def email(self, email):
        self.email = email

    @property
    def expertise(self):
        return self.expertise
    
    @expertise.setter
    def expertise(self, expertise):
        self.expertise = expertise

    def __str__(self):
        return f"Teacher ID: {self.teacherId}, First Name: {self.fname}, Last Name: {self.lname}, Email: {self.email}, Expertise: {self.expertise}"
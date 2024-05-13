

class Student:
    def __init__(self):
        self.studentId = None
        self.fname = None
        self.lname = None
        self.dob = None
        self.email = None
        self.phone = None

    @property
    def studentId(self):
        return self.studentId
    
    @studentId.setter
    def studentId(self, studentId):
        self.studentId = studentId

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
    def dob(self):
        return self.dob
    
    @dob.setter
    def dob(self, dob):
        self.dob = dob

    @property
    def email(self):
        return self.email
    
    @email.setter
    def email(self, email):
        self.email = email

    @property
    def phone(self):
        return self.phone
    
    @phone.setter
    def phone(self, phone):
        self.phone = phone

    def __str__(self):
        return f"Student ID: {self.studentId}, First Name: {self.fname}, Last Name: {self.lname}, DOB: {self.dob}, Email: {self.email}, Phone: {self.phone}"
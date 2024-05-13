from Exceptions.custom_exceptions import InvalidStudentDataException
from datetime import datetime

class Student:
    def __init__(self):
        self._studentId = None
        self._fname = None
        self._lname = None
        self._dob = None
        self._email = None
        self._phone = None
        self._enrollments = []

    @property
    def studentId(self):
        return self.studentId
    
    @studentId.setter
    def studentId(self, studentId):
        if len(studentId) == 0:
            raise InvalidStudentDataException("Student ID cannot be empty")
        self.studentId = studentId

    @property
    def fname(self):
        return self.fname
    
    @fname.setter
    def fname(self, fname):
        if len(fname) == 0:
            raise InvalidStudentDataException("First Name cannot be empty")
        self.fname = fname

    @property
    def lname(self):
        return self.lname
    
    @lname.setter
    def lname(self, lname):
        if len(lname) == 0:
            raise InvalidStudentDataException("Last Name cannot be empty")
        self.lname = lname

    @property
    def dob(self):
        return self.dob
    
    @dob.setter
    def dob(self, dob):
        if dob == "":
            raise InvalidStudentDataException("Invalid DOB")
        try:
            self.dob = str(datetime.strptime(dob, "%Y-%m-%d"))
        except Exception as e:
            raise InvalidStudentDataException("Invalid DOB format. Please use YYYY-MM-DD format.")

    @property
    def email(self):
        return self.email
    
    @email.setter
    def email(self, email):
        if len(email) == 0:
            raise InvalidStudentDataException("Email cannot be empty")
        self.email = email

    @property
    def phone(self):
        return self.phone
    
    @phone.setter
    def phone(self, phone):
        if len(phone) == 0:
            raise InvalidStudentDataException("Phone cannot be empty")
        elif len(phone) != 10:
            raise InvalidStudentDataException("Phone number must be at least 10 digits")
        self.phone = phone

    @property
    def enrollments(self):
        return self.enrollments
    
    @enrollments.setter
    def enrollments(self, enrollments):
        self.enrollments.append(enrollments)

    def __str__(self):
        return f"Student ID: {self.studentId}, First Name: {self.fname}, Last Name: {self.lname}, DOB: {self.dob}, Email: {self.email}, Phone: {self.phone}"
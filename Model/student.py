from Exceptions.custom_exceptions import InvalidStudentDataException
from datetime import datetime

class Student:

    _enrollments = []

    def __init__(self):
        self._studentId = None
        self._fname = None
        self._lname = None
        self._dob = None
        self._email = None
        self._phone = None

    @property
    def studentId(self):
        return self._studentId
    
    @studentId.setter
    def studentId(self, studentId):
        if len(studentId) == 0:
            raise InvalidStudentDataException("Student ID cannot be empty")
        self._studentId = studentId

    @property
    def fname(self):
        return self._fname
    
    @fname.setter
    def fname(self, fname):
        if len(fname) == 0:
            raise InvalidStudentDataException("First Name cannot be empty")
        self._fname = fname

    @property
    def lname(self):
        return self._lname
    
    @lname.setter
    def lname(self, lname):
        if len(lname) == 0:
            raise InvalidStudentDataException("Last Name cannot be empty")
        self._lname = lname

    @property
    def dob(self):
        return self._dob
    
    @dob.setter
    def dob(self, dob):
        if dob == "":
            raise InvalidStudentDataException("Invalid DOB")
        try:
            self._dob = str(datetime.strptime(dob, "%Y-%m-%d").date())
        except Exception as e:
            raise InvalidStudentDataException("Invalid DOB format. Please use YYYY-MM-DD format.")

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        if len(email) == 0:
            raise InvalidStudentDataException("Email cannot be empty")
        self._email = email

    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self, phone):
        if len(phone) == 0:
            raise InvalidStudentDataException("Phone cannot be empty")
        elif len(phone) != 10:
            raise InvalidStudentDataException("Phone number must be at least 10 digits")
        self._phone = phone

    @classmethod
    def enrollments(cls):
        return cls._enrollments
    
    @classmethod
    def enrollments(cls, enrollments):
        cls._enrollments.append(enrollments)

    def create_by_list(self,data):
        self.studentId = data[0]
        self.fname = data[1]
        self.lname = data[2]
        self.dob = data[3]
        self.email = data[4]
        self.phone = data[5]

    def __str__(self):
        return f"Student ID: {self._studentId}, First Name: {self._fname}, Last Name: {self._lname}, DOB: {self._dob}, Email: {self._email}, Phone: {self._phone}"
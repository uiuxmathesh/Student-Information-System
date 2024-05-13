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
    def _studentId(self):
        return self._studentId
    
    @_studentId.setter
    def _studentId(self, studentId):
        if len(studentId) == 0:
            raise InvalidStudentDataException("Student ID cannot be empty")
        self._studentId = studentId

    @property
    def _fname(self):
        return self._fname
    
    @_fname.setter
    def _fname(self, fname):
        if len(fname) == 0:
            raise InvalidStudentDataException("First Name cannot be empty")
        self._fname = fname

    @property
    def _lname(self):
        return self._lname
    
    @_lname.setter
    def _lname(self, lname):
        if len(lname) == 0:
            raise InvalidStudentDataException("Last Name cannot be empty")
        self._lname = lname

    @property
    def _dob(self):
        return self._dob
    
    @_dob.setter
    def _dob(self, dob):
        if dob == "":
            raise InvalidStudentDataException("Invalid DOB")
        try:
            self._dob = str(datetime.strptime(dob, "%Y-%m-%d"))
        except Exception as e:
            raise InvalidStudentDataException("Invalid DOB format. Please use YYYY-MM-DD format.")

    @property
    def _email(self):
        return self._email
    
    @_email.setter
    def _email(self, email):
        if len(email) == 0:
            raise InvalidStudentDataException("Email cannot be empty")
        self._email = email

    @property
    def _phone(self):
        return self._phone
    
    @_phone.setter
    def _phone(self, phone):
        if len(phone) == 0:
            raise InvalidStudentDataException("Phone cannot be empty")
        elif len(phone) != 10:
            raise InvalidStudentDataException("Phone number must be at least 10 digits")
        self._phone = phone

    @property
    def _enrollments(self):
        return self._enrollments
    
    @_enrollments.setter
    def _enrollments(self, enrollments):
        self._enrollments.append(enrollments)

    def __str__(self):
        return f"Student ID: {self._studentId}, First Name: {self._fname}, Last Name: {self._lname}, DOB: {self._dob}, Email: {self._email}, Phone: {self._phone}"
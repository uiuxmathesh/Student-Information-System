from Exceptions.custom_exceptions import InvalidTeacherDataException
class Teacher:
    def __init__(self):
        self._teacherId = None
        self._fname = None
        self._lname = None
        self._email = None
        self._expertise = None
        self._assignedCourses = list()

    @property
    def _teacherId(self):
        return self._teacherId
    
    @_teacherId.setter
    def _teacherId(self, teacherId):
        if len(teacherId) == 0:
            raise InvalidTeacherDataException("Teacher ID cannot be empty")
        self._teacherId = teacherId

    @property
    def _fname(self):
        return self._fname
    
    @_fname.setter
    def _fname(self, fname):
        if len(fname) == 0:
            raise InvalidTeacherDataException("First Name cannot be empty")
        self._fname = fname

    @property
    def _lname(self):
        return self._lname
    
    @_lname.setter
    def _lname(self, lname):
        if len(lname) == 0:
            raise InvalidTeacherDataException("Last Name cannot be empty")  
        self._lname = lname

    @property
    def _email(self):
        return self._email
    
    @_email.setter
    def _email(self, email):
        if len(email) == 0:
            raise InvalidTeacherDataException("Please provide email")
        self._email = email

    @property
    def _expertise(self):
        return self._expertise
    
    @_expertise.setter
    def _expertise(self, expertise):
        if len(expertise) == 0:
            raise InvalidTeacherDataException("Please provide expertise")
        self._expertise = expertise

    @property
    def _assignedCourses(self):
        return self._assignedCourses
    
    @_assignedCourses.setter
    def _assignedCourses(self, assignedCourses):
        self._assignedCourses = assignedCourses


    def __str__(self):
        return f"Teacher ID: {self._teacherId}, First Name: {self._fname}, Last Name: {self._lname}, Email: {self._email}, Expertise: {self._expertise}"
from Exceptions.custom_exceptions import InvalidTeacherDataException
class Teacher:

    _assignedCourses = list()

    def __init__(self):
        self._teacherId = None
        self._fname = None
        self._lname = None
        self._email = None
        self._expertise = None

    @property
    def teacherId(self):
        return self._teacherId
    
    @teacherId.setter
    def teacherId(self, teacherId):
        if not isinstance(teacherId, int):
            raise InvalidTeacherDataException("Teacher ID cannot be empty")
        self._teacherId = teacherId

    @property
    def fname(self):
        return self._fname
    
    @fname.setter
    def fname(self, fname):
        if len(fname) == 0:
            raise InvalidTeacherDataException("First Name cannot be empty")
        self._fname = fname

    @property
    def lname(self):
        return self._lname
    
    @lname.setter
    def lname(self, lname):
        if len(lname) == 0:
            raise InvalidTeacherDataException("Last Name cannot be empty")  
        self._lname = lname

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        if len(email) == 0:
            raise InvalidTeacherDataException("Please provide email")
        self._email = email

    @property
    def expertise(self):
        return self._expertise
    
    @expertise.setter
    def expertise(self, expertise):
        if len(expertise) == 0:
            raise InvalidTeacherDataException("Please provide expertise")
        self._expertise = expertise

    @classmethod
    def assignedCourses(cls):
        return cls._assignedCourses
    
    @classmethod
    def assignedCourses(cls, assignedCourses):
        cls._assignedCourses.append(assignedCourses)

    def create_by_list(self, data):
        self.teacherId = data[0]
        self.fname = data[1]
        self.lname = data[2]
        self.email = data[3]
        self.expertise = data[4]

    def __str__(self):
        return f"Teacher ID: {self.teacherId}, First Name: {self.fname}, Last Name: {self.lname}, Email: {self.email}, Expertise: {self.expertise}"
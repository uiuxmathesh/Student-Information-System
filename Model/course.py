from Exceptions.custom_exceptions import InvalidCourseDataException
class Course:

    _enrollments = list()
    def __init__(self):
        self._code = None
        self._name = None
        self._fee = None
        self._credit = None
        self._teacherId = None

    @property
    def code(self):
        return self._code
    
    @code.setter
    def code(self, code):
        if len(code) == 0:
            raise InvalidCourseDataException("Course code cannot be empty")
        self._code = code

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if len(name) == 0:
            raise InvalidCourseDataException("Course name cannot be empty")
        self._name = name    

    @property
    def fee(self):
        return self._fee
    
    @fee.setter
    def fee(self, fee):
        if fee < 0:
            raise InvalidCourseDataException("Course fee cannot be negative")
        self._fee = fee

    @property
    def credit(self):
        return self._credit
    
    @credit.setter
    def credit(self, credit):
        if credit < 0:
            raise InvalidCourseDataException("Course credit cannot be negative")
        self._credit = credit

    @property
    def teacherId(self):
        return self._teacherId
    
    @teacherId.setter
    def teacherId(self, teacherId):
        if len(teacherId) == 0:
            raise InvalidCourseDataException("Teacher ID cannot be empty")
        self._teacherId = teacherId  

    @classmethod
    def enrollments(cls):
        return cls._enrollments

    @classmethod
    def enrollments(cls, enrollments):
        cls._enrollments.append(enrollments)
    
    def create_by_list(self, data):
        self.code = data[0]
        self.name = data[1]
        self.credit = data[2]
        self.teacherId = data[3]
        self.fee = data[4]
        

    def __str__(self):
        return f"Course Code: {self.code}, Name: {self.name}, Credits: {self.credit}, course fee: {self.fee} ,Instructor Name: {self.teacherId}"
    
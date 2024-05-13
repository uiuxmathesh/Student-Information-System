from Exceptions.custom_exceptions import InvalidCourseDataException
class Course:
    def __init__(self):
        self.code = None
        self.name = None
        self.fee = None
        self.credit = None
        self.teacherId = None

    @property
    def code(self):
        return self.code
    
    @code.setter
    def code(self, code):
        if len(code) == 0:
            raise InvalidCourseDataException("Course code cannot be empty")
        self.code = code

    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, name):
        if len(name) == 0:
            raise InvalidCourseDataException("Course name cannot be empty")
        self.name = name    

    @property
    def fee(self):
        return self.fee
    
    @fee.setter
    def fee(self, fee):
        if fee < 0:
            raise InvalidCourseDataException("Course fee cannot be negative")
        self.fee = fee

    @property
    def credit(self):
        return self.credit
    
    @credit.setter
    def credit(self, credit):
        if credit < 0:
            raise InvalidCourseDataException("Course credit cannot be negative")
        self.credit = credit

    @property
    def teacherId(self):
        return self.teacherId
    
    @teacherId.setter
    def teacherId(self, teacherId):
        if len(teacherId) == 0:
            raise InvalidCourseDataException("Teacher ID cannot be empty")
        self.teacherId = teacherId   

    def __str__(self):
        return f"Course ID: {self.credit}, Name: {self.name}, Code: {self.code}, course fee: {self.fee} ,Instructor Name: {self.teacherId}"
    
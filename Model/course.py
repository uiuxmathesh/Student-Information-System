from Exceptions.custom_exceptions import InvalidCourseDataException
class Course:
    def __init__(self):
        self._code = None
        self._name = None
        self._fee = None
        self._credit = None
        self._teacherId = None
        self._enrollments = list()

    @property
    def _code(self):
        return self._code
    
    @_code.setter
    def _code(self, code):
        if len(code) == 0:
            raise InvalidCourseDataException("Course code cannot be empty")
        self._code = code

    @property
    def _name(self):
        return self._name
    
    @_name.setter
    def _name(self, name):
        if len(name) == 0:
            raise InvalidCourseDataException("Course name cannot be empty")
        self._name = name    

    @property
    def _fee(self):
        return self._fee
    
    @_fee.setter
    def _fee(self, fee):
        if fee < 0:
            raise InvalidCourseDataException("Course fee cannot be negative")
        self._fee = fee

    @property
    def _credit(self):
        return self._credit
    
    @_credit.setter
    def _credit(self, credit):
        if credit < 0:
            raise InvalidCourseDataException("Course credit cannot be negative")
        self._credit = credit

    @property
    def _teacherId(self):
        return self._teacherId
    
    @_teacherId.setter
    def _teacherId(self, teacherId):
        if len(teacherId) == 0:
            raise InvalidCourseDataException("Teacher ID cannot be empty")
        self._teacherId = teacherId  

    @property
    def _enrollments(self):
        return self._enrollments

    @_enrollments.setter
    def _enrollments(self, enrollments):
        self._enrollments.append(enrollments)

    def __str__(self):
        return f"Course ID: {self._credit}, Name: {self._name}, Code: {self._code}, course fee: {self._fee} ,Instructor Name: {self._teacherId}"
    
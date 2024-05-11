 
class DuplicateEnrollmentException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class CourseNotFoundException(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(self.message)

class StudentNotFoundException(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(self.message)

class TeacherNotFoundException(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(self.message)

class PaymentValidationException(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(self.message)

class InvalidStudentDataException(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(self.message)

class InvalidCourseDataException(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(self.message)

class InvalidTeacherDataException(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(self.message)

class InvalidEnrollmentDataException(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(self.message)
class InvalidPaymentDataException(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(self.message)

class InsufficientFundsException(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(self.message)

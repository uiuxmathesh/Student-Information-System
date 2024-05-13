
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
        self.code = code

    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, name):
        self.name = name    

    @property
    def fee(self):
        return self.fee
    
    @fee.setter
    def fee(self, fee):
        self.fee = fee

    @property
    def credit(self):
        return self.credit
    
    @credit.setter
    def credit(self, courseId):
        self.credit = courseId

    @property
    def teacherId(self):
        return self.teacherId
    
    @teacherId.setter
    def teacherId(self, teacherId):
        self.teacherId = teacherId   

    def __str__(self):
        return f"Course ID: {self.credit}, Name: {self.name}, Code: {self.code}, course fee: {self.fee} ,Instructor Name: {self.teacherId}"
    
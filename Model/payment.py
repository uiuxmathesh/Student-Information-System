
class Payment:
    def __init__(self):
        self.paymentId = None
        self.studentId = None
        self.amount = None
        self.paymentDate = None

    @property
    def paymentId(self):
        return self.paymentId
    
    @paymentId.setter
    def paymentId(self, paymentId):
        self.paymentId = paymentId

    @property
    def studentId(self):
        return self.studentId
    
    @studentId.setter
    def studentId(self, studentId):
        self.studentId = studentId

    @property
    def amount(self):
        return self.amount
    
    @amount.setter
    def amount(self, amount):
        self.amount = amount

    @property
    def paymentDate(self):
        return self.paymentDate
    
    @paymentDate.setter
    def paymentDate(self, paymentDate):
        self.paymentDate = paymentDate

    def __str__(self):
        return f"Payment ID: {self.paymentId}, Student ID: {self.studentId}, Amount: {self.amount}, Payment Date: {self.paymentDate}"
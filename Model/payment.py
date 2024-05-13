from Exceptions.custom_exceptions import InvalidPaymentDataException
from datetime import datetime
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
        if not isinstance(paymentId,int):
            raise InvalidPaymentDataException("Payment ID must be an integer")
        self.paymentId = paymentId

    @property
    def studentId(self):
        return self.studentId
    
    @studentId.setter
    def studentId(self, studentId):
        if not isinstance(studentId,str):
            raise InvalidPaymentDataException("Student ID must be an integer")
        self.studentId = studentId

    @property
    def amount(self):
        return self.amount
    
    @amount.setter
    def amount(self, amount):
        if amount < 0:
            raise InvalidPaymentDataException("Amount cannot be negative")
        self.amount = amount

    @property
    def paymentDate(self):
        return self.paymentDate
    
    @paymentDate.setter
    def paymentDate(self, paymentDate):
        if paymentDate == "":
            raise InvalidPaymentDataException("Invalid Payment Date")
        try:
            self.paymentDate = str(datetime.strptime(paymentDate, "%Y-%m-%d"))
        except Exception as e:
            raise InvalidPaymentDataException("Invalid Payment Date format. Please use YYYY-MM-DD format.")

    def __str__(self):
        return f"Payment ID: {self.paymentId}, Student ID: {self.studentId}, Amount: {self.amount}, Payment Date: {self.paymentDate}"
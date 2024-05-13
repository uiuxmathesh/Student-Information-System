from Exceptions.custom_exceptions import InvalidPaymentDataException
from datetime import datetime
class Payment:

    _student = list()

    def __init__(self):
        self._paymentId = None
        self._studentId = None
        self._amount = None
        self._paymentDate = None


    @property
    def paymentId(self):
        return self._paymentId
    
    @paymentId.setter
    def paymentId(self, paymentId):
        if not isinstance(paymentId,int):
            raise InvalidPaymentDataException("Payment ID must be an integer")
        self._paymentId = paymentId

    @property
    def studentId(self):
        return self._studentId
    
    @studentId.setter
    def studentId(self, studentId):
        if not isinstance(studentId,str):
            raise InvalidPaymentDataException("Student ID must be an integer")
        self._studentId = studentId

    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, amount):
        if amount < 0:
            raise InvalidPaymentDataException("Amount cannot be negative")
        self._amount = amount

    @property
    def paymentDate(self):
        return self._paymentDate
    
    @paymentDate.setter
    def paymentDate(self, paymentDate):
        if paymentDate == "":
            raise InvalidPaymentDataException("Invalid Payment Date")
        try:
            self._paymentDate = str(datetime.strptime(paymentDate, "%Y-%m-%d"))
        except Exception as e:
            raise InvalidPaymentDataException("Invalid Payment Date format. Please use YYYY-MM-DD format.") 

    @classmethod
    def student(cls):
        return cls._student
    
    @classmethod
    def student(cls, student):
        cls._student = student

    def __str__(self):
        return f"Payment ID: {self.paymentId}, Student ID: {self.studentId}, Amount: {self.amount}, Payment Date: {self.paymentDate}"
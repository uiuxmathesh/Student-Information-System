from Exceptions.custom_exceptions import InvalidPaymentDataException
from datetime import datetime
class Payment:
    def __init__(self):
        self._paymentId = None
        self._studentId = None
        self._amount = None
        self._paymentDate = None
        self._student = None


    @property
    def _paymentId(self):
        return self._paymentId
    
    @_paymentId.setter
    def _paymentId(self, paymentId):
        if not isinstance(paymentId,int):
            raise InvalidPaymentDataException("Payment ID must be an integer")
        self._paymentId = paymentId

    @property
    def _studentId(self):
        return self._studentId
    
    @_studentId.setter
    def _studentId(self, studentId):
        if not isinstance(studentId,str):
            raise InvalidPaymentDataException("Student ID must be an integer")
        self._studentId = studentId

    @property
    def _amount(self):
        return self._amount
    
    @_amount.setter
    def _amount(self, amount):
        if amount < 0:
            raise InvalidPaymentDataException("Amount cannot be negative")
        self._amount = amount

    @property
    def _paymentDate(self):
        return self._paymentDate
    
    @_paymentDate.setter
    def _paymentDate(self, paymentDate):
        if paymentDate == "":
            raise InvalidPaymentDataException("Invalid Payment Date")
        try:
            self._paymentDate = str(datetime.strptime(paymentDate, "%Y-%m-%d"))
        except Exception as e:
            raise InvalidPaymentDataException("Invalid Payment Date format. Please use YYYY-MM-DD format.") 

    @property
    def _student(self):
        return self._student
    
    @_student.setter
    def _student(self, student):
        self._student = student

    def __str__(self):
        return f"Payment ID: {self._paymentId}, Student ID: {self._studentId}, Amount: {self._amount}, Payment Date: {self._paymentDate}"
from datetime import datetime
class Payment:
    def __init__(self, paymentId:int, studentId:int, amount:int, paymentDate:datetime):
        self.__paymentId = paymentId
        self.__studentId = studentId
        self.__amount = amount
        self.__paymentDate = datetime.strptime(paymentDate, "%d-%m-%Y").date()

    def get_student(self):
        return self.__studentId
    
    def get_payment_amount(self):
        return self.__amount
    
    def get_payment_date(self):
        return self.__paymentDate

# Testing class
payment1 = Payment(1, 1, 2000, "02-03-2024")


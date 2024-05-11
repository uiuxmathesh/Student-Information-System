from services import *
from datetime import datetime
class Payment:

    student = None
    def __init__(
        self, paymentId: int = None, studentId: int = None, amount: int = None
    ):
        self.paymentId = paymentId
        self.studentId = studentId
        self.amount = amount
        self.paymentDate = str(datetime.now().date())

    @classmethod
    def getStudent(cls):
        print("Student Details for Payment-ID:-")
        paymentId = input("Payment ID: ")
        payment = Payment(paymentId=paymentId)
        paymentService = PaymentService()
        paymentService.get_student_details(payment)
        return

    def setStudents(self, student):
        self.student = student

    @classmethod    
    def getPaymentAmount(cls):
        print("Payment amount for Payment-ID:-")
        paymentId = input("Payment ID: ")
        payment = Payment(paymentId=paymentId)
        paymentService = PaymentService()
        paymentService.get_payment_amount(payment)
        return

    @classmethod    
    def getPaymentDate(cls):
        print("Payment amount for Payment-ID:-")
        paymentId = input("Payment ID: ")
        payment = Payment(paymentId=paymentId)
        paymentService = PaymentService()
        paymentService.get_payment_date(payment)
        return

    @staticmethod
    def paymentMenu():
        """
        Catalog for payment operations
        """
        while True:
            choice = int(
                input(
                    """
        *********PAYMENT MENU*********
        1. Get Student details for Payment ID
        2. Get Payment Amount Details for Payment ID
        3. Get Payment Date Details for Payment ID
        4. Go to Main menu
        *******************************
        Please select a option to continue...  """
                )
            )
            print()
            print()

            if choice == 1:
                Payment.getStudent()

            elif choice == 2:
                Payment.getPaymentAmount()

            elif choice == 3:
                Payment.getPaymentDate()

            elif choice == 4:
                break


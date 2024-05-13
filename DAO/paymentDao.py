
class PaymentDao:

    def _init__(self):
        self.connection = None
        self.cursor = self.connection.cursor()

    def getStudent(self,payment):
        query = "SELECT * FROM [students] WHERE [student_id] = (SELCT [student_id] FROM [payments] WHERE [payment_id] = ?)"
        values = (payment.paymentId)
        self.cursor.execute(query, values)
        headers = (column[0] for column in self.cursor.description)
        student = self.cursor.fetchall()
        student = [headers] + student
        self.cursor.close()
        self.connection = None
        return student


    def getPaymentDate(self,payment):
        query = "SELECT [payment_date] FROM [payments] WHERE [payment_id] = ?"
        values = (payment.paymentId)
        self.cursor.execute(query, values)
        headers = (column[0] for column in self.cursor.description)
        paymentDate = self.cursor.fetchone()[0]
        paymentDate = [headers] + paymentDate
        self.cursor.close()
        self.connection = None
        return paymentDate

    def getAmount(self,payment):
        query = "SELECT [amount] FROM [payments] WHERE [payment_id] = ?"
        values = (payment.paymentId)
        self.cursor.execute(query, values)
        headers = (column[0] for column in self.cursor.description)
        amount = self.cursor.fetchone()[0]
        amount = [headers] + amount
        self.cursor.close()
        self.connection = None
        return amount
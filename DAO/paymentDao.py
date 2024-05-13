from Util import DBConnUtil

class PaymentDao:

        

    def getStudent(self,payment):
        self.connection = DBConnUtil.getConnection()
        self.cursor = self.connection.cursor()
        query = "SELECT * FROM [students] WHERE [student_id] = (SELECT [student_id] FROM [payments] WHERE [payment_id] = ?)"
        values = (payment.paymentId)
        self.cursor.execute(query, values)
        headers = (column[0] for column in self.cursor.description)
        student = self.cursor.fetchall()
        student = [headers] + student
        self.cursor.close()
        self.connection = DBConnUtil.closeConnection()
        return student


    def getPaymentDate(self,payment):
        self.connection = DBConnUtil.getConnection()
        self.cursor = self.connection.cursor()
        query = "SELECT [payment_date] FROM [payments] WHERE [payment_id] = ?"
        values = (payment.paymentId)
        self.cursor.execute(query, values)
        # headers = (column[0] for column in self.cursor.description)
        paymentDate = self.cursor.fetchone()[0]
        # paymentDate = [headers] + paymentDate
        self.cursor.close()
        self.connection = DBConnUtil.closeConnection()
        return paymentDate

    def getAmount(self,payment):
        self.connection = DBConnUtil.getConnection()
        self.cursor = self.connection.cursor()
        query = "SELECT [amount] FROM [payments] WHERE [payment_id] = ?"
        values = (payment.paymentId)
        self.cursor.execute(query, values)
        # headers = (column[0] for column in self.cursor.description)
        amount = self.cursor.fetchone()[0]
        # amount = [headers] + amount
        self.cursor.close()
        self.connection = DBConnUtil.closeConnection()
        return amount
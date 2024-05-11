from util.DBConnUtil import DBConnUtil
from exceptions.custom_exceptions import *
import pyodbc
from tabulate import tabulate

class PaymentService:

    def get_student_details(self, payment):
        query = """
        SELECT	*
        FROM	[students]
        WHERE	[student_id] = (
                                SELECT	[student_id]
                                FROM	[payments]
						        WHERE	[payment_id] = ?)"""
        connection = DBConnUtil.getConnection()
        cursor = connection.cursor()
        try:
            if payment.paymentId == "":
                raise InvalidPaymentDataException("Enter a valid payment-ID to fetch records")
        except Exception as e:
            print(f"ERROR: Unable to fetch records {e}")
        else:
            cursor.execute(query, (payment.paymentId))
            heading = [column[0] for column in cursor.description]
            rows = cursor.fetchall()
            rows = [ [*row] for row in rows ]
            table = [heading, rows]
            print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
        finally:
            connection = DBConnUtil.closeConnection()
        
    def get_payment_amount(self, payment):
        query = """
                SELECT	[amount]
                FROM	[payments]
				WHERE	[payment_id] = ?"""
        connection = DBConnUtil.getConnection()
        cursor = connection.cursor()
        cursor.execute(query, (payment.paymentId))
        heading = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        rows = [ [*row] for row in rows ]
        table = [heading, rows]
        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
        connection = DBConnUtil.closeConnection()

    def get_payment_date(self, payment):
        query = """
                SELECT	[payment_date]
                FROM	[payments]
				WHERE	[payment_id] = ?"""
        connection = DBConnUtil.getConnection()
        cursor = connection.cursor()
        cursor.execute(query, (payment.paymentId))
        heading = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        rows = [ [*row] for row in rows ]
        table = [heading, rows]
        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
        connection = DBConnUtil.closeConnection()

from DAO import *
from Model import *

paymentDao = PaymentDao()

payment = Payment()
payment.paymentId = 101

print('Student Info:',paymentDao.getStudent(payment))
print('Payment Date:',paymentDao.getPaymentDate(payment))
print('Amount:',paymentDao.getAmount(payment))
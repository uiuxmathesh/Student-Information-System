class Payment:
    def __init__(self, paymentId, studentId, amount, paymentDate):
        self.paymentId = paymentId
        self.studentId = studentId
        self.amount = amount
        self.paymentDate = paymentDate


# Testing class
payment1 = Payment("P1001", "S1001", 2000, "2024-03-02")

print(f"{payment1.paymentDate}")

class Student:

    def __init__(self, studemtId, fname, lname, dob, email, phone):
        self.studentId = studemtId
        self.fname = fname
        self.lname = lname
        self.dob = dob
        self.email = email
        self.phone = phone


# Testing class
s1 = Student(
    "S0001",
    "Mathesh",
    "Premkumar",
    "2003-01-21",
    "matheshpremkumar@gmail.com",
    "6374621004",
)
print(f"{s1.fname} {s1.lname}")

class Teacher:

    def __init__(self, teacherId, fname, lname, email):
        self.teacherId = teacherId
        self.fname = fname
        self.lname = lname
        self.email = email


# Testing class
teacher1 = Teacher("T1001", "Lokesh", "Kanagaraj", "loki@lcu.com")
print(f"{teacher1.fname} {teacher1.lname}")

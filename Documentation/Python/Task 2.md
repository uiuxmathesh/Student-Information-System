# Creating Constructors


## 1. Student Class Constructor

**Creating Student Class**
```python
class Student:
    def __init__(self):
        self.studentId = None
        self.fname = None
        self.lname = None
        self.dob = None
        self.email = None
        self.phone = None

    @property
    def studentId(self):
        return self.studentId
    
    @studentId.setter
    def studentId(self, studentId):
        self.studentId = studentId

    @property
    def fname(self):
        return self.fname
    
    @fname.setter
    def fname(self, fname):
        self.fname = fname

    @property
    def lname(self):
        return self.lname
    
    @lname.setter
    def lname(self, lname):
        self.lname = lname

    @property
    def dob(self):
        return self.dob
    
    @dob.setter
    def dob(self, dob):
        self.dob = dob

    @property
    def email(self):
        return self.email
    
    @email.setter
    def email(self, email):
        self.email = email

    @property
    def phone(self):
        return self.phone
    
    @phone.setter
    def phone(self, phone):
        self.phone = phone

    def __str__(self):
        return f"Student ID: {self.studentId}, First Name: {self.fname}, Last Name: {self.lname}, DOB: {self.dob}, Email: {self.email}, Phone: {self.phone}"
```



## 2. Course Class Constructor

**Creating Course Class**
```python
class Course:
    def __init__(self):
        self.courseId = None
        self.name = None
        self.code = None
        self.instructor_name = None
    
    @property
    def courseId(self):
        return self.courseId
    
    @courseId.setter
    def courseId(self, courseId):
        self.courseId = courseId

    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, name):
        self.name = name

    @property
    def code(self):
        return self.code
    
    @code.setter
    def code(self, code):
        self.code = code

    @property
    def instructor_name(self):
        return self.instructor_name
    
    @instructor_name.setter
    def instructor_name(self, instructor_name):
        self.instructor_name = instructor_name

    def __str__(self):
        return f"Course ID: {self.courseId}, Name: {self.name}, Code: {self.code}, Instructor Name: {self.instructor_name}"
    
```


## 3. Teacher Class Constructor

**Creating Teacher Class**
```python
class Teacher:
    def __init__(self):
        self.teacherId = None
        self.fname = None
        self.lname = None
        self.email = None
        self.expertise = None
    
    @property
    def teacherId(self):
        return self.teacherId
    
    @teacherId.setter
    def teacherId(self, teacherId):
        self.teacherId = teacherId

    @property
    def fname(self):
        return self.fname
    
    @fname.setter
    def fname(self, fname):
        self.fname = fname

    @property
    def lname(self):
        return self.lname
    
    @lname.setter
    def lname(self, lname):
        self.lname = lname

    @property
    def email(self):
        return self.email
    
    @email.setter
    def email(self, email):
        self.email = email

    @property
    def expertise(self):
        return self.expertise
    
    @expertise.setter
    def expertise(self, expertise):
        self.expertise = expertise

    def __str__(self):
        return f"Teacher ID: {self.teacherId}, First Name: {self.fname}, Last Name: {self.lname}, Email: {self.email}, Expertise: {self.expertise}"
```


## 4. Enrollment Class Constructor

**Creating Enrollment Class**
```python
class Enrollment:
    def __init__(self):
        self.enrollmentId = None
        self.studentId = None
        self.courseId = None
        self.enrollmentDate = None
    
    @property
    def enrollmentId(self):
        return self.enrollmentId
    
    @enrollmentId.setter
    def enrollmentId(self, enrollmentId):
        self.enrollmentId = enrollmentId

    @property
    def studentId(self):
        return self.studentId
    
    @studentId.setter
    def studentId(self, studentId):
        self.studentId = studentId

    @property
    def courseId(self):
        return self.courseId
    
    @courseId.setter
    def courseId(self, courseId):
        self.courseId = courseId

    @property
    def enrollmentDate(self):
        return self.enrollmentDate
    
    @enrollmentDate.setter
    def enrollmentDate(self, enrollmentDate):
        self.enrollmentDate = enrollmentDate

    def __str__(self):
        return f"Enrollment ID: {self.enrollmentId}, Student ID: {self.studentId}, Course ID: {self.courseId}, Enrollment Date: {self.enrollmentDate}"
```

## 5. Payment Class Constructor

**Creating Payment Class**
```python
class Payment:
    def  __init__(self):
        self.paymentId = None
        self.studentId = None
        self.amount = None
        self.paymentDate = None
    
    @property
    def paymentId(self):
        return self.paymentId
    
    @paymentId.setter
    def paymentId(self, paymentId):
        self.paymentId = paymentId

    @property
    def studentId(self):
        return self.studentId
    
    @studentId.setter
    def studentId(self, studentId):
        self.studentId = studentId

    @property
    def amount(self):
        return self.amount
    
    @amount.setter
    def amount(self, amount):
        self.amount = amount

    @property
    def paymentDate(self):
        return self.paymentDate
    
    @paymentDate.setter
    def paymentDate(self, paymentDate):
        self.paymentDate = paymentDate

    def __str__(self):
        return f"Payment ID: {self.paymentId}, Student ID: {self.studentId}, Amount: {self.amount}, Payment Date: {self.paymentDate}"
```
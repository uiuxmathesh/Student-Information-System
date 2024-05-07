# Defining Classes & Initializing constructors

## 1. Student Class

**1.1 Creating Student Class and its constructor**
```python
class Student:

    def __init__(self, studentId, fname, lname, dob, email, phone):
        self.studentId = studentId
        self.fname = fname
        self.lname = lname
        self.dob = dob
        self.email = email
        self.phone = phone
```

**1.2 Testing Student Class by Creating a object**
```python
# Testing student class
s1 = Student(
    "S0001",
    "Mathesh",
    "Premkumar",
    "2003-01-21",
    "matheshpremkumar@gmail.com",
    "6374621004",
)
print(f"{s1.fname} {s1.lname}")
```


## 2. Course Class

**2.1 Creating Course Class and its constructor**
```python
class Course:

    def __init__(self, courseId, name, code, instructor_name):
        self.courseId = courseId
        self.name = name
        self.code = code
        self.instructor_name = instructor_name
```

**2.2 Testing Course Class by Creating a object**
```python
# Testing Course class
course1 = Course("C1001", "Python Programming", "3", "Nandhakumar")
print(f"{course1.instructor_name}")
```

## 3. Teacher Class

**3.1 Creating Teacher Class and its constructor**
```python
class Teacher:

    def __init__(self, teacherId, fname, lname, email):
        self.teacherId = teacherId
        self.fname = fname
        self.lname = lname
        self.email = email
```

**3.2 Testing Teacher Class by Creating a object**
```python
# Testing Teacher class
teacher1 = Teacher("T1001", "Lokesh", "Kanagaraj", "loki@lcu.com")
print(f"{teacher1.fname} {teacher1.lname}")
```

## 4. Enrollment Class

**4.1 Creating Enrollment Class and its constructor**
```python
class Enrollment:

    def __init__(self, enrollmentId, studentId, courseId, enrollmentDate):
        self.enrollmentId = enrollmentId
        self.studentId = studentId
        self.courseId = courseId
        self.enrollmentDate = enrollmentDate
```

**4.2 Testing Enrollment Class by Creating a object**
```python
# Testing Enrollment class
enrollment1 = Enrollment("E1001", "S1001", "C1001", "2023-04-21")
print(enrollment1.enrollmentDate)
```

## 5. Payment Class

**5.1 Creating Payment Class and its constructor**
```python
class Payment:
    def __init__(self, paymentId, studentId, amount, paymentDate):
        self.paymentId = paymentId
        self.studentId = studentId
        self.amount = amount
        self.paymentDate = paymentDate
```

**5.2 Testing Payment Class by Creating a object**
```python
# Testing Payment class
payment1 = Payment("P1001", "S1001", 2000, "2024-03-02")

print(f"{payment1.paymentDate}")
```
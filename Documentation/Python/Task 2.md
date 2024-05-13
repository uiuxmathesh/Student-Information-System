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
```

## 5. Payment Class Constructor

**Creating Payment Class**
```python
class Payment:
    self.paymentId = None
        self.studentId = None
        self.amount = None
        self.paymentDate = None
```
# Task 3: Implementing Methods

- As the following methods will be interacting with databases, it is better to create separate classes with in `dao` or `service` package
  

This is Just a Abstract implementation of the tasks. To see the actual code, Open the 
- [Student Service](../../DAO/studentDao.py)<br>
- [Course Service](../../DAO/courseDao.py)<br>
- [Teacher Service](../../DAO/teacherDao.py)<br>
- [Enrollment Service](../../DAO/enrollmentDao.py)<br>
- [Payment Service](../../DAO/paymentDao.py)<br>
- [SIS Service](../../Model/SIS.py)



 ### Student Class Methods:

 ```python
from datetime import datetime
from Exceptions.custom_exceptions import *
import pyodbc
from Util import DBConnUtil

class StudentDao(DBConnUtil):

    def enrollInCourse(self,student, course):
        pass                    

    def updateStudentInfo(self,student): # WORKING GOOD AS EXPECTED
        pass

    def makePayment(self,studentId,amount:float, paymentDate:str): # WORKING GOOD AS EXPECTED
        pass
            
    def displayStudentInfo(self,student): # WORKING GOOD AS EXPECTED
        pass

    def getEnrolledCourses(self,student): # WORKING GOOD AS EXPECTED
        pass

    def getPaymentHistory(self,student):  # WORKING GOOD AS EXPECTED
        pass
 ```

 ### Course class methods
 ```python
class CourseDao(DBConnUtil):
        

    def assignTeacher(self, teacher, course): # WORKING GOOD AS EXPECTED
        pass

    def updateCourseInfo(self,course): # WORKING GOOD AS EXPECTED
        pass


    def displayCourseInfo(self,course): # WORKING GOOD AS EXPECTED
        pass

    def getTeacher(self,course): # WORKING GOOD AS EXPECTED
        pass

    def getEnrollments(self,course): # WORKING GOOD AS EXPECTED
        pass
 ```

 ### Teacher class methods
 ```python
class TeacherDao(DBConnUtil):


    def updateTeacherInfo(self,teacher): # WORKING GOOD AS EXPECTED
        pass 

    def displayTeacherInfo(self,teacher): # WORKING GOOD AS EXPECTED
        pass

    def getAssignedCourses(self,teacher): # WORKING GOOD AS EXPECTED
        pass
 ```

 ### Enrollment class methods
 ```python
 from Util import DBConnUtil

class EnrollmentDao(DBConnUtil):
        
    def getStudent(self,enrollment): # WORKING GOOD AS EXPECTED
       pass

    def getCourse(self,enrollment): # WORKING GOOD AS EXPECTED
       pass
```

### Payment class methods

```python
class PaymentDao:
     def getStudent(self,payment):
        pass


    def getPaymentDate(self,payment):
        pass

    def getAmount(self,payment):
        pass
```
### SIS class methods
```python
class SIS:
    def __init__(self):
        pass

    def enrollStudentInCourse(self, student: Student, course: Course):
        pass

    def assignTeacherToCourse(self, teacher: Teacher, course: Course):
        pass

    def recordPayment(self, studentId: int, amount: float, paymentDate: str):
        pass

    def getEnrollmentReport(self, student: Student):
        pass

    def getPaymentReport(self, student: Student):
        pass

    def calculateCourseStatistics(self, course: Course):
        pass

    def addEnrollment(self, student, course, enrollmentDate):
        pass

    def assignCourseToTeacher(self, course: Course, teacher: Teacher):
        pass

    def addPayment(self, student: Student, amount, paymentDate):
        pass

    def getEnrollmentForStudent(self, student):
        pass

    def getCoursesForTeacher(self, teacher):
        pass

    def closeConnections(self):
        pass

```

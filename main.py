from DAO import *
from Model import *


# sis = SIS()
# student = Student()
# course = Course()
# teacher = Teacher()
# teacher.teacherId = 'T0001'
# student.studentId = 'S0001'
# course.code = 'CS100'
# sis.enrollStudentInCourse(student, course)
# sis.assignTeacherToCourse(teacher, course)


studentInformationSystem = SIS()

student = Student()
student.studentId = 'S0002'

# course = Course()
# course.code = 'EC006'

# teacher = Teacher()
# teacher.teacherId = 'T0002'

# studentInformationSystem.enrollStudentInCourse(student, course)
# studentInformationSystem.assignTeacherToCourse(teacher, course)

# studentInformationSystem.recordPayment('S0001', 1000, '2021-01-01')

studentInformationSystem.getEnrollmentReport(student)
studentInformationSystem.getPaymentReport(student)

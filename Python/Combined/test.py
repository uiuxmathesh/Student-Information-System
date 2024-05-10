from model import Student
from StudentServices import StudentServices

s1 = Student("Sugapriyan","P K", "2003-06-24", "pakasu@gmail.com","7852220000")
studentServices = StudentServices()
studentServices.create_student(s1)
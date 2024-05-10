from model import Course
from StudentServices import StudentServices

s1 = Course("Sugapriyan", "P K", "2003-06-24", "pakasu@gmail.com", "7852220000")
studentServices = StudentServices()
# studentServices.create_student(s1)

studentServices.test_query(s1)

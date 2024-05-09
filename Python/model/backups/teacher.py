class Teacher:

    def __init__(self, teacherId:int, fname:str, lname:str, email:str):
        self.__teacherId = teacherId
        self.__fname = fname
        self.__lname = lname
        self.__email = email

    def update_teacher_info(self, teacherId:int, fname:str, lname:str, email:str):
        self.__teacherId = teacherId
        self.__fname = fname
        self.__lname = lname
        self.__email = email

    def display_teacher_info(self):
        print(f'Teacher Id: {self.__teacherId}, First name: {self.__fname}, Last name: {self.__lname}, Email: {self.__email}')

# Testing class
teacher1 = Teacher(1, "Lokesh", "Kanagaraj", "loki@lcu.com")
teacher1.display_teacher_info()

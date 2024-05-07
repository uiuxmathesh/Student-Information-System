class Course:

    def __init__(self, courseId, name, code, instructor_name):
        self.courseId = courseId
        self.name = name
        self.code = code
        self.instructor_name = instructor_name


# Testing class
course1 = Course("C1001", "Python Programming", "3", "Nandhakumar")
print(f"{course1.instructor_name}")

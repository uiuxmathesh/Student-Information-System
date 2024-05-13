
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
    
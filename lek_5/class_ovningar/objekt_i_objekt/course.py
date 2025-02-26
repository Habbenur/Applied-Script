class Course:
    def __init__(self, course_name, school_name):
        self.course_name = course_name
        self.school_name = school_name

    def __str__(self):
        return f"{self.course_name},\nStudents skola : {self.school_name}"
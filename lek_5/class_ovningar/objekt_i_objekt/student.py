class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def __str__(self):
        return f"Students namn : {self.name}, \nStudents ålder : {self.age}, \nStudent lektion : {self.course}\n"
class Person:
    pass

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce (self):
        return f"Hej, jag heter {self.name} och är {self.age} år gammal."
    
    def __str__(self):
        return f"Person({self.name}, {self.age} år.)"
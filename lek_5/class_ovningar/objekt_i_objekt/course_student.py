from course import Course
from student import Student

lesson = Course("Engelska", "Frans Schartau")
lesson2 = Course("Matematik", "Åsö grundskola")

person = Student("Alice", 15, lesson)
person2 = Student("Bob", 17, lesson2)

print(person)
print(person2)
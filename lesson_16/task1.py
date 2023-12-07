""" 
School
Make a class structure in python representing people at school. Make a base class called Person, 
a class called Student, and another one called Teacher. 
Try to find as many methods and attributes as you can which belong to different classes, and keep in mind which are common and which are not. 
For example, the name should be a Person attribute, while salary should only be available to the teacher. 
"""

class Person:
    def __init__(self,name,lastname):
        self.name = name
        self.lastname = lastname

    def display_info(self):
        print (f"Name: {self.name}, Lastname: {self.lastname}")


class Student(Person):
    def __init__(self, name, lastname, grade):
        super().__init__(name, lastname)
        self.grade = grade

    def display_info(self):
        super().display_info()
        print (f'Grade: {self.grade}')

class Teacher(Person):
    def __init__(self, name, lastname, subject):
        super().__init__(name, lastname) 
        self.subject = subject
    
    def display_info(self):
        super().display_info()
        print(f'Subject: {self.subject}')

student_1 = Student("Oleksadr", "Rubtsov", "A")
student_1.display_info()
teacher_1 = Teacher("Ihor", "Korolevskyy", "Mathematics")
teacher_1.display_info()
print("OOP - class")
# Class is an object constructor, it is a blue print for our objects

class Myclass :

    # In Python, the __init__ method is a special built-in method (often called a constructor) that’s automatically called when you create a new object from a class.

    def __init__(self, name, number_of_student, class_teacher):
        self.name = name
        self.number_of_student = number_of_student
        self.class_teacher = class_teacher

    x = 5

first_class = Myclass("300 level","78","Miss opatola")
second_class = Myclass("200 level","30","Mister oladipupo")
print(first_class.class_teacher)
print(second_class.class_teacher)
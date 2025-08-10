print("OOP - class")
# Class is an object constructor, it is a blue print for our objects

class Classroom :

    # Class Attributes → Defined outside __init__
    # - Shared across all instances of the class.
    # - Belong to the class itself, not individual objects.
    # - Usually defined directly in the class body, outside any method.

    school_name = "Afe Babalola University"


    # the __init__ method is a special built-in method (often called a constructor) that’s automatically called when you create a new object from a class.

    # Instance Attributes → Usually defined in __init__
    # - Belong to a specific object (instance) of the class.
    # - Each instance gets its own copy.
    # - Usually set inside __init__ using self.attribute.

    def __init__(self, name, number_of_student, class_teacher, student_names = None):
        #  The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
        #  It doesnt have to be self, it can be anything
        self.name = name
        self.number_of_student = number_of_student
        self.class_teacher = class_teacher
        self.student_names = student_names if student_names is not None else []

    # The __str__ is a special method that controls what’s returned when you turn an object into a string — for example, when you use print(obj) or str(obj).

    def __str__(self):
        return f"This is class {self.name}, with {self.number_of_student} students"
    
    def add_student(self,add_student_name):
        self.student_names.append(add_student_name)
    

    # Defining a method inside of a class

    def learn(self, subject_being_learnt):
        print(f"We are leaening {subject_being_learnt}")


first_class = Classroom(name="300 level",number_of_student="78",class_teacher="Miss opatola",student_names=(["muqoddim","eniola"]))
second_class = Classroom(name="200 level",number_of_student="30",class_teacher="Mister oladipupo")
first_class.add_student("ayomide")
print(first_class.student_names)
print(second_class.student_names)

# Delete object properties by using the del keyword
del first_class.student_names
print(first_class.student_names)

# Delete an object by using the del keyword
del first_class
print(first_class)


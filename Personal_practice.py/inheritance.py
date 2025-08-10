# Python Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.


class Parent:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"Hello, my name is {self.name}")

    def walk(self):
        pass # Use the pass keyword when you do not want to add any other properties or methods to the class.

class Child(Parent):
    def __init__(self, name):
        self.name = name

    def play(self):
        print("hey watch me play")

first_child = Child("daniel")
first_child.speak()
first_child.play()

first_parent = Parent("vivian")
first_parent.speak()
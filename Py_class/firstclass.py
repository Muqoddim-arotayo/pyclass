# PRINT
# print("Hello world!!!")

# comment, variable, datatypes, naming conventions, type conversions, python operator and application, inbuilt fun, concatenation

# COMMENT
# comment : types of comment : single line comment and multiline comment

# this is a single line comment

"""
this is a multiline comment
"""

# DATA TYPES

# number - integer and float
print(type(8))
print(type(8.0))

#string : string is created using single quote, double quote, or triple quote
print(type("eniola"))

# datatype list : it is created using the square bracket
print(type(['eniola', 'muqoddim']))

# datatype tuple : it is created using perentesis
print(type(('eniola','muqoddim')))

# datatype dictionary : it is created using curly braces
print(type({'name':"eniola"}))

# datatype set : it is created using curly braces
print(type({'eniola','muqoddim'}))

# datatype boolean : this is a true or false
print(type(True))

# VARIABLES
# Variable is used to store data temporarily on your PC

# name = "Eniola"
# name = "muqoddim"
# print(name)

# Rules for naming a variable
# Do not use integer to store as a variable name 
# 1 = "Eniola"
# print(1)

# Do not use reserved words as your variable name
# list = [1, 2, 3, 4]
# print(list)

# naming must be very descriptive
# no1 = "Eniola"
#print(no1)

# Type of naming a variable
# Camel casing 
# nameOfStudent = ['folake', 'Eniola']

# pascal casing 
# NameOfStudent = ['folake', 'Eniola']

# snake casing
# name_of_student = ['folake', 'Eniola']

first_name = "Muqoddim"
last_name = "Arotayo"
full_name = first_name + last_name

print(full_name)

# INBUILT FUNCTION

# first_name = input("enter your name")
# print(first_name)
# print(len(first_name))

# CONCARTENATION 

first_name = "Muqoddim"
last_name = "Arotayo"
age = 15
print("My name is " + first_name + last_name + "i am " + str(age) + "years old")


# Assignment : resdearch on other concatenation methods and sight one example each

# Using the + operator
first_name = "Muqoddim"
last_name = "Arotayo"
age = 15
print("My name is " + first_name + last_name + ", i am " + str(age) + "years old")

# Using f-string
first_name = "Muqoddim"
last_name = "Arotayo"
age = 15
print(f"My name is {first_name} {last_name}, i am {age} years old")

# Using % formatting
first_name = "Muqoddim"
last_name = "Arotayo"
age = 15
print("My name is %s %s, I am %d years old" % (first_name, last_name, age))

# Using .format()
first_name = "Muqoddim"
last_name = "Arotayo"
age = 15
print("My name is {} {}, I am {} years old".format(first_name, last_name, age))




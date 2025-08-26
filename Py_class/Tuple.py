"""
Tuple is ordered and unchangeable
Accessing tuple item
undating tuple
unpacking (unpacking with var name, Using Asterisk)
looping over tuple
Joining tuple
tuple method
"""

names_of_student = ('titilope','taiwo','eniola')
names_of_student_2 = tuple(('titilope','taiwo','eniola'))

for name, location, gender in names_of_student:
    print(name)
    user_input = input("enter location >> ")
    if user_input == location:
        score += 25
        
# Assignment : resdearch on other concatenation methods and sight one example each

# Using the + operator
first_name = "Muqoddim"
last_name = "Arotayo"
age = 15
print("My name is " + first_name+ "" + last_name + ", i am " + str(age) + " years old")

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

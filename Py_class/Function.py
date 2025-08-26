# FUNCTION
# Function is a block of code that perform a specific task
# We have parametric and un parametric functions

# function
# by convention, you start the naming of a funx should start with small letter

# the doc string

# doc strings (doc string explains the purpose and the usage of a function)
# parameters

# We have 4 type of function
# 1. builtin function 2. user define 3. lamba funtion and 4. recursive function

# to define our function, we use the key word and we have three stages in creating a function
# 1. function declaration 2. function definition 3. function invoking

# def eat():
#     """
#     This returns a user action
#     """
#     print("I am eating...")
# eat()

def mul_Table_gen():
    value_1 = int(input("Start table : "))
    value_2 = int(input("Stop table : "))
    list_1 = [1,2,3,4,5,6,7,8,9,10,11,10]
    if value_1 < value_2 and value_1 != 0:
        for i in range(value_1, value_2+1):
            print(f"\nMultiplication table {value_1}")
            for j in list_1:
                print(f"\n{i} x {j} = {i*j}")
    else:
        print("\nThe first value must be greater than zero and lesser than the second value")
# mul_Table_gen()


# def cbt_test():
#     print("What would you like to do ?")
#     user_action = input("Register [1], Watch resources [2], Take test [3] >>> ")
#     if user_action == "1":
#         user_name = input("\nInput your name >>> ")
#         user_password = input("\nInput your password >>> ")
#         print("\nRedirecting to register page....")
#     elif user_action == "2":
#         print("\nWatching resources...")
#     elif user_action == "3":
#         print("\nTaking test...")
#     else :
#         print("\nInput a valid parameter")

# cbt_test()

# Arguement
# Types of arguements
# arbitraty : 

# x = 1
# y = 2
# z = 3
# print(x,y,z)

first_name = input("\nEnter your first name : ")
last_name = input("\nEnter your last name : ")
password = input("\nEnter your password : ")

def if_empty(*names):
    for each_input in names:
        if not each_input:
            print(f"Input your {each_input}")
        else:
            print("Good job !!! ")

if_empty(first_name,last_name,password)

# def student_names(*names):
#     print("hello")
#     print(names)
#     return 

# name1 = "bola"
# name2 = "fola"
# name3 = "tola"
# student_names(name1, name2, name3)






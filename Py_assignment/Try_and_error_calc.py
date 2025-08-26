first_value = input("Enter the first digit : ")
second_value = input("Enter the second digit : ")

def add() :
    try:
        print(first_value.isdigit())
        result = int(first_value) / int(second_value)
        print(result)
    except TypeError:
        print("Input valid integers")

add()
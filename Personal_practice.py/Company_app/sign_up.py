import welcome as wel

def sign_in():
    user_first_name = input("Enter your first name >> ")
    user_last_name = input("Enter your last name >> ")

    wel.welcome_user(user_first_name)

sign_in()
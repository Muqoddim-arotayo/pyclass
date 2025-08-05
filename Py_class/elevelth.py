# OBJECT ORIENTED PROGRAMMING
# It help to setup yyour code in a way that is easy to debug
# Used malls as an example
# creation of class and object
# Inheritance - genericity : Having things in common feature

# How to creat a class

# class Bank :
#     name = "Bubble Bank"
#     motto = "Bubbling with Opportunities, Growing Your Future."
#     branch = "Main branch"

# uba = Bank()
# uba.name = "United Bank of africa"
# uba.motto = "Everything we do, we do it well - EXECUTION"
# uba.branch = "Main"

# zenith = Bank()
# access = Bank()
# first = Bank()
# print(uba.name)

# class Bank:
#     balance = 0

#     def __init__(self, name, motto, location):
#        self.name = name
#        self.motto = motto
#        self.location = location

#     def saving(self):
#         user_input = input("enter the amount to save: ")
#         print(f"your initial balance is {self.balance}")
#         self.balance += user_input
#         print(f"thank you for saving {user_input} with {self.balance}")

# uba = Bank(location="uba",name="Everything we do, we do it well - EXECUTION", motto="Main")
# print(uba.name)
# print(uba.location)
# print(uba.motto)
    
class Bank:
    balance = 0
    user_register = []

    def __init__(self, name, motto, location):
        self.name = name
        self.motto = motto
        self.location = location

    def saving(self):
        print("Redirecting to the Savings page...")
        print(f"Your current balance is {self.balance}")

    def check_balance(self):
        print(f"\nYour current balance is {self.balance}")
    
    def withdraw(self):
        print("\nRedirecting to withdrawal page...")
        self.withdrawal_amount = input("\nHow much would you like to withdraw")
        self.balance -= self.withdrawal_amount
        print(f"\nWithdraw successful !!!")
        self.withdraw_option = input("\nCheck balance [1] | Withdraw :")
        self.check_balance() if self.withdraw_option == "1" else self.withdraw()
    
    def loan_application(self):
        print("\nRedirecting to Loan Application page...")

    def dash_board(self):
        pass

    def landing_page(self):
        self.landing_page_option = input("Sign in [1], Sign up [2]")
        if self.landing_page_option == "1":
            pass
        elif self.landing_page_option == "2":
            print("Redirecting to sign up page...")
            self.sign_up() 

    def sign_up(self):
        self.user_first_name = input("\nEnter your first name : ")
        self.user_last_name = input("\nEnter your last name : ")
        self.user_phone_number = input("\nEnter your phone number : ")
        self.confirm_password()

    def sign_in(self):
        self.sign_in_first_name = input("\nEnter your first name : ")
        self.sign_in_password = input("\nEnter your password")
        for self.each_user_detail in range(len(self.user_register)):
            if self.sign_in_first_name == self.each_user_detail[0] and self.sign_in_password == self.each_user_detail[3]:
                print("\nLogin successful")
                print("\nRedirecting to dashboard")
                self.dash_board()
            else :
                print("\nIncorrect details")
                self.sign_in()

        

    def confirm_password(self):
        self.user_password = input("Enter your password : ")
        self.user_confirm_password = input("\nConfirm your password : ")
        if self.user_confirm_password != self.user_password :
            print("password does not match")
        else :
            self.check_if_empty(self.user_first_name,self.user_last_name,self.user_phone_number,self.user_password,self.user_confirm_password)
            self.user_register.append(self.user_first_name,self.user_last_name,self.user_phone_number,self.user_password)


    
    def check_if_empty(self):
        for i in [self.user_first_name,self.user_last_name,self.user_phone_number,self.user_password,self.user_confirm_password]:
            if not i :
                print("Do not leave any space empty")
                self.sign_up()
            
        







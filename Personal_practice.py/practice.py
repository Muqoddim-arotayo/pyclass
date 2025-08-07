# print("Practice Session")
# nine = 8
# ten = 10
# print("yes") if ten > nine else print("no")
# print("the correct value if 9" if nine != 9 else "it already is 9")

# for i in range(4):
#     name = input("what is your name >> ")
#     match name :
#         case "muqoddim"|"eniola"|"ayomide":
#             print("Arotayo Muqoddim Eniola")
#         case "deborah"|"titiloye"|"peace":
#             print("Titiloye Deborah Peace")
#         case "ayomide":
#             print("ayomide")
#         case _:
#             print("your name no dey")

# def knock(*door):
#     print(f"ko ko ko on {door[2]}")

# knock("my door","your door","our door")

# def knock(door_1,door_2,door_3):
#     print(f"He knocked on {door_3}, i knocked on {door_2}, and they knocked on {door_1}")

# knock(door_3="my door",door_1="our door",door_2="your door")

class Bank:
    user_register = []

    def __init__(self, name, motto, location):
        self.name = name
        self.motto = motto
        self.location = location


    def landing_page(self):
        print("\nLANDING PAGE")
        self.landing_page_option = input("\nSign in [1], Sign up [2] : ")
        if self.landing_page_option == "1":
            print("\nRedirecting to sign in page...")
            self.sign_in()
        elif self.landing_page_option == "2":
            print("\nRedirecting to sign up page...")
            self.sign_up() 

    def sign_up(self):
        self.user_first_name = input("\nEnter your first name : ")
        self.user_last_name = input("\nEnter your last name : ")
        self.user_phone_number = input("\nEnter your phone number : ")
        self.confirm_password()
        print("\nAccount creation successful")
        print("\nRedirecting to sign in page...")
        self.sign_in()

    def sign_in(self):
        self.sign_in_first_name = input("\nEnter your first name : ")
        self.sign_in_password = input("\nEnter your password : ")
        for self.each_user_detail in self.user_register:
            print(self.each_user_detail)
            if self.sign_in_first_name == self.each_user_detail[0] and self.sign_in_password == self.each_user_detail[3]:
                print("\nLogin successful")
                print("\nRedirecting to dashboard")
                self.current_user_name = self.each_user_detail[0]
                self.current_user_balance = self.each_user_detail[4]
                self.current_user_loan_balance = self.each_user_detail[5]
                self.current_user_transaction_pin = self.each_user_detail[6]
                print(self.current_user_name)
                self.dash_board()
            else :
                print("\nIncorrect details")
                self.incorrect_password_option = input("\nTry again [1] | Sign up [2] | Recover password [3] : ")
                if self.incorrect_password_option == "2":
                    print("\nRedirecting to sign up page...")
                    self.sign_up()
                elif self.incorrect_password_option == "3":
                    print("Redirecting to password recovery page")
                else :
                    self.sign_in()
    
    def check_if_empty(self):
        for i in [self.user_first_name,self.user_last_name,self.user_phone_number,self.user_password,self.user_confirm_password]:
            if not i :
                print("Do not leave any space empty")
                self.sign_up()
    
    def generate_pin (self):
        if self.current_user_transaction_pin == 0 :
            print("TRANSACTION PIN")
            self.user_transaction_pin_gen = input("Enter your pin : ")
            self.user_confirm_transaction_pin_gen = input("Re-enter your pin : ")
            if self.user_transaction_pin_gen == self.user_confirm_transaction_pin_gen:
                self.current_user_transaction_pin = self.user_transaction_pin_gen
                print("Transaction pin generated !!!")
            else:
                print("Pin does not match")
                self.generate_pin()

    def confirm_password(self):
        self.user_password = input("\nEnter your password : ")
        self.user_confirm_password = input("\nConfirm your password : ")
        if self.user_confirm_password != self.user_password :
            print("password does not match")
            self.confirm_password()
        else :
            print("\nPassword match !!!")
            self.user_account_balance = 50000
            self.user_loan_balance = 0
            self.user_transaction_pin = ""
            self.push_user_details()

    def push_user_details(self):
        self.user_register.append([self.user_first_name,self.user_last_name,self.user_phone_number,self.user_password,self.user_account_balance,self.user_loan_balance,self.user_transaction_pin])


    def dash_board(self):
        print("DASHBOARD")
        print(f"\nWelcome {self.current_user_name}")
        print("\nWhat would you like to do today ? ")
        self.dash_board_action_list()

    def dash_board_action_list(self):
        self.dash_user_action = input("\nWithdraw [1] | Save [2] | Loan [3] : ")
        if self.dash_user_action == "1":
            print("\nRedirecting to Withdrawal page...")
            self.withdraw()
        elif self.dash_user_action == "2":
            print("\nRedirecting to Savings page")
            self.saving()
        elif self.dash_user_action == "3":
            print("\nRedirecting to Loan page...")
            self.loan_application_menu()
        else:
            print("\nAction not defined !!!")
            self.dash_board_action_list()

    def check_balance(self):
        print(f"\nYour current balance is {self.current_user_balance}")

    def saving(self):
        print("\nSAVINGS")
        print(f"\nYour current balance is {self.current_user_balance}")
        self.savings_amount = int(input("\nEnter amount to save : "))
        self.current_user_balance += self.savings_amount
        print("\nSaving successful !!!")
        self.check_balance()
        self.dormant_saving = input("save again [1] | Go to Dashboard [2] : ")
        if self.dormant_saving == "1":
            self.saving()
        else:
            print("Redirectin to the dashboard page...")
            self.dash_board()

    
    def withdraw(self):
        print("\nWITHDRAW")
        self.generate_pin()
        self.withdrawal_amount = int(input("\nHow much would you like to withdraw : "))
        self.current_user_balance -= self.withdrawal_amount
        print(f"\nWithdraw successful !!!")
        self.check_balance()
        self.withdraw_option = input("\nWithdraw again [1] | Go to dashboard [2] : ")
        if self.withdraw_option == "1":
            self.withdraw()
        else :
            print("Redirecting to dashboard...")
            self.dash_board()

            
class loan_app(Bank):
    def loan_application_menu(self):
        self.loan_application_option = input("\nLoan aplication [1], Loan repayment [2], Loan interest calculator [3] : ")
        if self.loan_application_option == "1":
            print("LOAN APPLICATION PAGE") 
            self.loan_application()
        elif self.loan_application_option == "2":
            print("LOAN REPAYMENT PAGE")
            self.loan_repayment()
        elif self.loan_application_option == "3":
            print("LOAN INTEREST CALCULATOR")
            self.loan_interest_calculator()
        else :
            print("\nAction not defined !!!")
            self.loan_application_menu() 

    def loan_interest_calculator(self):
        self.calc_loan_amount = int(input("\nEnter loan amount : "))
        self.calc_loan_duration = int(input("\nHow many month: "))
        self.calc_repay_amount = self.calc_loan_amount + self.calc_loan_amount * 0.05
        print("\nLoan interest rate = 5%")
        print(f"\nTotal interest = {self.calc_loan_amount*0.05}")
        print(f"\nMonthly repayment = {self.calc_loan_amount/self.calc_loan_duration}")
        print(f"\nTotal repayment = {self.calc_loan_amount}")
        self.dormant_loan_application()

    def loan_application(self):
        self.loan_amount = int(input("\nEnter loan amount : "))
        self.loan_app_amount = self.loan_amount+self.current_user_loan_balance
        self.loan_threshold = self.current_user_balance*2
        if self.loan_app_amount > self.loan_threshold :
            print(f"\nYou have exceeded your loan threshold, you can only collect {self.current_user_balance*2 - self.current_user_loan_balance}")
        else :
            print(f"\nLoan application for {self.loan_amount} naira submitted successfully.")
            self.loan_interest = self.loan_amount * 0.05
            print(f"\nInterest on loan is {self.loan_interest}, You are to pay {self.loan_amount+self.loan_interest}")
            self.current_user_loan_balance += self.loan_amount + self.loan_interest
            print(f"\nUpdated loan balance: {self.current_user_loan_balance} naira")
            self.dormant_loan_application()


    def loan_repayment(self):
        self.loan_repay_amount = int(input("\nEnter repay amount :"))
        if self.loan_repay_amount > 0:
            self.current_user_loan_balance -= self.loan_repay_amount
            print(f"\nUpdated loan outstanding : {self.current_user_loan_balance}")
            self.dormant_loan_application()
        else :
            print("Enter a valid amount")
            self.loan_repayment()

    def dormant_loan_application(self):
        self.dormant_loan_application_option = input("\nPerform loan operation [1] | Go to dashboard [2] :")
        if self.dormant_loan_application_option == 1:
            self.loan_application_menu()
        else :
            print("\nRedirecting to dashboard...")
            self.dash_board()

        

uba = Bank(location="uba",name="Everything we do, we do it well - EXECUTION", motto="Main")
uba.landing_page()

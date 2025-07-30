
print('SIGN UP PAGE ')
first_name = input('Enter your first name >>> ')
last_name = input('Enter your last name >>> ')
phone_number = input('enter your phone number >>> ')
if not first_name or not last_name or not phone_number :
    print('do not leave any input blank')
elif len(phone_number) < 11 or phone_number[0] != '0' and phone_number[0] != '+':
    print('input a valid phone number')
else :
    email_address = input('enter your email address >>> ')
    if '@gmail.com' in email_address :
        password = input('user a password >>> ')
        confirm_password = input('confirm your password >>>')
        if password != confirm_password :
            print("password doesn't match")
        else :
            print('Account creation successful')
            print(f'welcome, {first_name}')
    else :  
        print('input a valid email address')




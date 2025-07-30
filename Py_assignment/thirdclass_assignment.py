old_password = input('Input a password >>> ')
confirm_password = input('\nconfirm your password >>> ')
if old_password != confirm_password :
    print("\npassword doesn't match")
else :
    print('\nAccount creation successful')
    print(f'Your password is {confirm_password}\t')
    change_password = input('\nInput your new password >>> ')
    confirm_password.replace(confirm_password,change_password)
    print(f'\nYour new password is {change_password}')
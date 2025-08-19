user_mail = input("Enter your user name : ")
if "@" in user_mail and ".com" in user_mail:
    at_index = user_mail.find("@")
    dot_index = user_mail.find(".com")
    print(user_mail[at_index+1:dot_index])

    
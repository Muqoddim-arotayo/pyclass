print("Practice Session")
nine = 8
ten = 10
print("yes") if ten > nine else print("no")
print("the correct value if 9" if nine != 9 else "it already is 9")

for i in range(4):
    name = input("what is your name >> ")
    match name :
        case "muqoddim"|"eniola"|"ayomide":
            print("Arotayo Muqoddim Eniola")
        case "deborah"|"titiloye"|"peace":
            print("Titiloye Deborah Peace")
        case "ayomide":
            print("ayomide")
        case _:
            print("your name no dey")
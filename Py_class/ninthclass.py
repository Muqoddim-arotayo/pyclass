list_1 = int(input("Table start >> "))
list_2 = int(input("Table stop >> "))
list_3 = [1,2,3,4,5,6,7,8,9,10,11,12]
for i in range(list_1, list_2+1):
    print(f"\nMultiplication table {i}\n")
    for j in list_3:
        print(f"{i} x {j} = {i*j}")
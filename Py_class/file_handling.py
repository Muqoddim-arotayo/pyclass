myfile="example1.txt"

# with open(myfile, "w") as file:
    # file.write("helooooooooooooo")
    # print('text written successfully')

# with open(myfile, "a") as file:
    # file.write("you are welcome")
    # print('text written successfully')

# with open(myfile, "r") as file:
#     content=file.read()
#     print(content)

# with open(r"C:\Allproject\example3.pdf", "r") as file:
#     # file.write("mr emma is unhappy because his baby mama did  not cook for him")
#     content=file.read()
#     # print('done')
#     print(content)

# with open(r"C:\Users\Lenovo\Pictures\waetherf\clear-w.jpg", "rb") as file:  
#     data = file.read()
#     print(data)

# with open(r"C:\Users\Lenovo\Downloads\sqi.csv", "r") as file:  
#     data = file.read()
#     print(data, "an excel file") #this will throw an error becos  Python has encounter characters in the file that it cannot decode

# READING EXCEL FILE
# with open(r"C:\Users\Lenovo\Downloads\sqi.csv", "r", encoding='utf-8') as file:  
#     data = file.read()
#     print(data, "an excel file")

# with open("example2.pdf", "r+") as file:
#     content = file.read()  # Read the entire file content
#     file.seek(0, 2)  # Move the file pointer to the end of the file
#     file.write("this mode is a special mode\n")  # Write to the file
#     file.seek(0)  # Move the file pointer back to the beginning
#     updated_content = file.read()  # Read the file again to get updated content
#     print(updated_content)

# with open("example2.pdf", "a+") as file:
#     file.write("this mode is a special mode\n")  # Append the text
#     file.seek(0)  # Move the file pointer to the beginning
#     updated_content = file.read()  # Read the entire file content
#     print(updated_content)  # Print the updated content

# try:
#     with open("example4.html", "a") as file:

#         file.write("<h5>this file is opened using python</h5>")
#         print("file created")
#         # print(file.read())
# except FileExistsError:
#     print("File already exists!!!")

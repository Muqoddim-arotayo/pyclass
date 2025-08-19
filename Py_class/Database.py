# Computer Data are 


# Example of relational database : Mysql, Sql lite, Oracle
# Example of non-relational database : mongodb, redis, neoj4

# DBMS - Data Base Management System
# software you can use to create your own database

import pymysql as pyms
import os   
from dotenv import load_dotenv
load_dotenv()

db_password = os.getenv("DB_PASS")

my_con = pyms.connect(host='127.0.0.1', user='root', passwd=db_password, db="MyDatabase")
print("connection succesful")
   
myCursor = my_con.cursor()
print("done")

# myCursor.execute("CREATE DATABASE MyDatabase")
# print("Database created successfully !!!")

# myCursor.execute("CREATE TABLE Registration_Table (std_id INT(4), full_name VARCHAR(40), address VARCHAR(50), password VARCHAR(20))")
# print("Table creation successful")

# myCursor.execute("SHOW DATABASES")
# for db in myCursor:
#     print(db)
# myCursor.close()

# myCursor.execute("SHOW COLUMNS FROM Registration_Table")
# for col in myCursor:
#     print(col[0])
# myCursor.close()

# my_query = "ALTER TABLE Registration_Table MODIFY full_name VARCHAR(25) AFTER password"
# my_query = "ALTER TABLE Registration_Table CHANGE std_id student_id INT(5) PRIMARY KEY AUTO_INCREMENT"
# my_query = "ALTER TABLE Registration_Table ADD phone_number VARCHAR(11) UNIQUE"
for i in range(3):
    full_name = input("Enter your Full name : ")
    address = input("Enter your address : ")
    password = input("Enter your password : ")
    phone_number = input("Enter your phone number : ")

    my_query = "INSERT INTO Registration_Table (full_name, address, password, phone_number) VALUES (%s,%s,%s,%s)"
    val = (full_name,address,password,phone_number)
    myCursor.execute(my_query,val)
    my_con.commit()

print(myCursor.rowcount,"record inserted successfully")
# print("done 2")
# my_con.cursor()
# myCursor.execute(my_query)
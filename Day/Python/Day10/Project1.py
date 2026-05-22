#Login System using python
# where the username and password store in the JSON file
#program read the data from json file at the time of login

import json
import os

def register():
    username=input("Create username:")
    password=input("Create password:")

    data={"username":username,"password":password}   # store in form of json

    with open("users.json","w") as f:
        json.dump(data,f)     #user data ko file me save karta hai

    print("Register sucessful !")

def login():
    username=input("Enter username:")
    password=input("Enter the password")

    if os.path.exists("users.json"):    #check file existing or not
        with open("users.json","r") as f:   #open the file to read
            data=json.load(f)    #file se data read karta hai

        if(data["username"]==username and data["password"]==password):
            print("Login successfull")
        else:
            print("Invallid credentials")
    else:
        print("No user found , please register first")



print("1. Register")
print("2. Login")

choice=input("choose option:")

if(choice=="1"):
    register()
elif choice=="2":
    login()
else:
    print("Invalid choice")
  


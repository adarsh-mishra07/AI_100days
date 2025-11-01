username="Adarsh"
password="12345"

user_input=input("Enter the user name:")
pass_input=input("Enter passsword:")

if(user_input == username and pass_input== password):
    print("Login Successful")
else:
    print("Invallid Credentials")
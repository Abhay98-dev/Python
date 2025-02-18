#Create a program that simulates a simple login system and access levels:

'''Ask the user for a username and password.
If the credentials are correct:
"admin": Print "Welcome, Admin! Full access granted."
"user": Print "Welcome, User! Limited access granted."
Any other username: Print "Invalid credentials."'''

username=input("Enter your username: ")
pas=input("Enter your password: ")
if username=="admin":
    if pas=="password123":
        print("welcome, admin full access granted")
    else:
        print("wrong password")
elif username=="user":
    if pas=="123password":
        print("welcome, user limited access granted")
    else:
        print("Wrong password")
else:
    print("Invalid credentials")
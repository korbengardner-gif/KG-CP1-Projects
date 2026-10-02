#KG user signin assignment

users = []
passwords = []
#I put a empty list for both usernams and passwords so that the user is forced to create an account if they want to login in

while True:
    username = input("What's your username: ")
    if username in users:
        password = input("What's your password: ")
        if password not in passwords:
            print("Incorrect password!")
        else:
            print("Welcome to the program!")
            break
    elif username not in users:
        print("That username does not exist")
        setup = input("Do you want to make a new account? (Y/N): ")
        if setup == "Y":
            username = input("What's your username: ")
            users.append(username)
            password = input("What's your password: ")
            passwords.append(password)
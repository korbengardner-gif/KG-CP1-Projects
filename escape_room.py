#KG escape room assignment

guess = 0
while guess <3:
    password = input("What is the password: \n")
    if password == "Cayde-6":
        print("")
        break
    else:
        guess +=1
    if guess == 1:
        
    elif guess == 2:
        print("Try again")
        print("It starts with 'Cayde'")
    elif guess == 3:

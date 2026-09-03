#Korben Gardner, average grade assignment
while True:
    try:
        class1 = float(input("What is your grade in 1st period: "))
    except: 
        print("That's not a number!")
    else:
        break
while True:  
    try:
        class2 = float(input("What is your grade in 2nd period: "))
    except:
        print("That's not a number!")
    else:
        break
while True:
    try:
        class3 = float(input("What is your grade in 3rd period: "))
    except:
        print("That's not a number!")
    else:
        break
while True:
    try:
        class45 = float(input("What is your grade in 4th/5th period: "))
    except:
        print("That's not a number!")
    else:
        break
while True:
    try:
        class6 = float(input("What is your grade in 6th period: "))
    except:
        print("That's not a number")
    else:
        break
while True:
    try:
        class7 = float(input("What is your grade in 7th period: "))
    except:
        print("That's not a number!")
    else:
        break
while True:
    try:
        class8 = float(input("What is your grade in 8th period: "))
    except:
        print("That's not a number!")
    else:
        break
                    


print("Your average grade is ",round((class1 + class2 + class3 + class45 + class6 + class7 + class8)/7,2),"%")
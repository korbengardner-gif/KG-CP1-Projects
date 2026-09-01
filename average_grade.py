#Korben Gardner, average grade assignment

try:
    class1 = float(input("What is your grade in 1st period: "))
except: 
    ("That's not a number!")
else:
    
    try:
        class2 = float(input("What is your grade in 2nd period: "))
    except:
        ("That's not a number!")
    else:
        try:
            class3 = float(input("What is your grade in 3rd period: "))
        except:
            ("That's not a number!")
        else:
            try:
                class45 = float(input("What is your grade in 4th/5th period: "))
            except:
                class6 = float(input("What is your grade in 6th period: "))
            else:
                try:
                    class7 = float(input("What is your grade in 7th period: "))
                except:
                    ("That's not a number!")
                else:
                    try:
                        class8 = float(input("What is your grade in 8th period: "))
                    except:
                        ("That's not a number!")
                    else:
                    


print("Your average grade is ",round((class1 + class2 + class3 + class45 + class6 + class7 + class8)/7,2),"%")
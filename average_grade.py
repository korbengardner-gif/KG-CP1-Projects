#Korben Gardner, average grade assignment


class1 = float(input("What is your grade in 1st period: "))
class2 = float(input("What is your grade in 2nd period: "))
class3 = float(input("What is your grade in 3rd period: "))
class45 = float(input("What is your grade in 4th/5th period: "))
class6 = float(input("What is your grade in 6th period: "))
class7 = float(input("What is your grade in 7th period: "))
class8 = float(input("What is your grade in 8th period: "))

print("Your average grade is ",round((class1 + class2 + class3 + class45 + class6 + class7 + class8)/7,2),"%")
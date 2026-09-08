# Korben Gardner, idiot proof

first_name = input("What is your first name: ".strip().title())

last_name = input("What is your last name: ".strip().title())
full_name = (first_name + " " + last_name)
while True:
    try:
        phone = int(input("What is your phone number: "))
    except:
        print("That's not a valid input")
    else:
        break
phone = str(phone)
while True:
    try:
        gpa = float(input("What is your GPA: "))
    except:
        print("That's not a valid input")
    else:
        break
gpa = str(gpa)

print("Name: " + full_name)
print("Phone Number: ",phone{3}," ",phone{3,6}," ",phone{6,10})
print("GPA: " + gpa)




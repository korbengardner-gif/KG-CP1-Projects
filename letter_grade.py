#KG letter grade assignment
while True:
    grade_percent = input("What is your grade: ")
    if grade_percent == int:
        if grade_percent >= 90:
            print(f"Your grade is {grade_percent} which is an A! Congrats!")
        elif grade_percent >= 80:
            print(f"Your grade is {grade_percent} which is an B. Nice!")
        elif grade_percent >= 70:
            print(f"Your grade is {grade_percent} which is an C. You might want to work on that.")
        elif grade_percent >= 65:
            print(f"Your grade is {grade_percent} which is an D. Most teachers will bug you for having that, so fix it!")
        elif grade_percent <= 65:
            print(f"Your grade is {grade_percent} which is an F... Get some help please.")
        else:
            print("please put a valid number (1-100)")
    else:
        print("Put a number please")
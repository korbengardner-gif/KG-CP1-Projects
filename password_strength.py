#KG password checker assignment
import string
import getpass

while True:

    score = 0
    feedback = []

    

    password =input("Create a password and I'll check its strength:\n")

    # konami code easter egg
    if password.strip() == "^^vv<><>ba":
            score = 6

    # 1. Check length

    if len(password) >= 8:
        score += 1
        feedback.append("At least 8 characters long")
    else:
        feedback.append("Needs to be at least 8 characters long")
                
    # 2. Check for uppercase

    if any(char.isupper() for char in password):
        score += 1 
        feedback.append("Includes an uppercase letter")
    else:
        feedback.append("Missing an uppercase letter")
                
    # 3. Check for lowercase

    if any(char.islower() for char in password):
        score += 1
        feedback.append("Includes a lowercase letter")
    else:
        feedback.append("Missing a lowercase letter")
                
    # 4. Check for special characters

    if any(char in string.punctuation for char in password):
        score += 1
        feedback.append("Includes a special character")
    else:
        feedback.append("Missing a special character")
                
    # 5. Check for numbers

    if any(char.isdigit() for char in password):
        score += 1
        feedback.append("Includes a number")
    else:
        feedback.append("Missing a number")
                
    

    print(f"\nPassword strength score: {score}/5\n")
    print("Breakdown:\n")
    for line in feedback:
        print(f"{line}\n")
    print()  # Empty line for spacing
                
    if score > 5:
        print("[ERROR] HOW DID YOU DO THAT?! You have broken the laws of mathematics via the power of konami! Please repent for getting the impossible score and don’t tell anyone about this or else...")
        print("-" * 30) #this will add a line so it looks nice
                
    elif score == 3:
        print("Your password is moderate.")
        break  
    elif score == 4:
        print("Your password is strong.")
        break   
    elif score == 5:
        print("Your password is perfect!")
        break  
    elif score in(1, 2):
        print("That password is too weak. Please try again and make it stronger!")
        print("-" * 30)
                
    else:  # This catches scores less than 1 (score == 0)
        print("Oh dear... that password didn't meet a single requirement. Please kindly seek help from a trusted adult.")
        print("-" * 30)

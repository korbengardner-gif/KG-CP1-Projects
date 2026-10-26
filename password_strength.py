#KG password checker assignment
while True:

    score = 0

    password = input("Create a password and I'll check its strength:\n")
    print(len(password))
    if len(password) >= 8:
        score += 1
    if password != password.lower():
        score += 1 
    if password != password.upper():
        score += 1
    if password 
    print(score)
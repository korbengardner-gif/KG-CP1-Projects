#KG multiplication table assignment
while True:
    try:
        user_range = input("Pick a number for your multiplication chart: ")
    except:
        print("Put a number!")
    else:
        break
user_range = int(user_range)
for i in range(1, user_range +1):
    for x in range(1, user_range +1):
        print(x * i, end="\t")
    print("\n\n")

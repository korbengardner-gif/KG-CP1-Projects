# KG dice roller


import random

while True:
    try:
        dice = int(input("What dice will I roll -JUST PUT THE NUMBER- D4, D6, D8, D10, D12, or D20:  "))
    except:
        print("That's not an option!")
    else:
        break



d4 = random.randint(1,4)
d6 = random.randint(1,6)
d8 = random.randint(1,8)
d10 = random.randint(1,10)
d12 = random.randint(1,12)
d20 = random.randint(1,20)


if dice == 4:
    print(f"You picked D{dice}")
    print(f"You rolled {d4}")
if dice == 6:
    print(f"You picked D{dice}")
    print(f"You rolled {d6}")
if dice == 8:
    print(f"You picked D{dice}")
    print(f"You rolled {d8}")
if dice == 10:
    print(f"You picked D{dice}")
    print(f"You rolled {d10}")
if dice == 12:
    print(f"You picked D{dice}")
    print(f"You rolled {d12}")
if dice == 20:
    print(f"You picked D{dice}")
    print(f"You rolled {d20}")
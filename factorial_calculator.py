#KG factorial calculator


import math
while True:
    try:
        num = int(input("What number do you want the factorial of: \n"))
    except:
        print("Put a number!")
    else:
        if num <0:
            print("Nice try buddy.")
        else:
            if num == 0:
                print()
                print("0! = 1")
            else:
                break
numbers = list(range(num, 0, -1))
factorials = list(map(math.factorial,numbers))
print()
for i in range(len(numbers)):
    print(numbers[i],factorials[i], sep= "! = ")
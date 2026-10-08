#KG factorial calculator


import math

num = int(input("What number do you want the factorial of: "))
numbers = list(range(num, 0, -1))
print(*numbers, sep = " x ")
print(math.factorial(num))
factorials = []

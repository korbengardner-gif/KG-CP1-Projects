#KG flexible calculator

import statistics as s
import math as m

def number_sum(*args):
    """Calculates the sum"""
    return sum(args)

def number_average(*args):
    """Calculates the average"""
    total = sum(args)
    for num in args:
        divide += 1
    average = total/divide
    return round(average, 2)

def number_max(*args):
    """Calculates the max"""
    max = 0
    for num in args:
        if num >= max:
            max = num
    return max

def number_min(*args):
    """Calculates the min"""
    min = 10000
    for num in args:
        if num <= min:
            min = num
    return min

def number_product(*args):
    """Calculates the product"""
    return m.prod(args)



def get_numbers():
    """Gets the numbers from user"""
    my_numbers = []
    while True:
        user_input = input("Number: ").strip

        if user_input.lower() == "done":
            break


        try:
            numbr = float(user_input)
            my_numbers.append(numbr)
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")


    return my_numbers


Calculator_on = True
while Calculator_on:
    print("Welcome to the Flexible Calculator!\n\n")
    print("Available operations: sum, average, max, min, product\n\n")
    calculate = input("Which operation would you like to perform?\n")
    numbers = get_numbers()
    if calculate == "sum":
        sum = number_sum(numbers)
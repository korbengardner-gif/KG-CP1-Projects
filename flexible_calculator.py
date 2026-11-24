#KG flexible calculator

import statistics as s
import math as m

def clear_terminal():
    """clears the extra stuff from the terminal"""
    print("\033[H\033[J", end="")

clear_terminal()

def number_sum(*args):
    """Calculates the sum"""
    return sum(args)

def number_average(*args):
    """Calculates the average"""
    return round(s.mean(args), 2)

def number_max(*args):
    """Calculates the biggest"""
    return max(args)

def number_min(*args):
    """Calculates the smallest"""
    return min(args)

def number_product(*args):
    """Calculates the product"""
    return m.prod(args)



def get_numbers():
    """Gets the numbers from user"""
    my_numbers = []
    print("Type your numbers. Type 'done' when done.")
    while True:
        user_input = input("Number: ").strip()

        if user_input.lower() == "done":
            if not my_numbers:
                print("Please enter at least one number first.")
                continue
            break
        try:
            numbr = float(user_input)
            my_numbers.append(numbr)
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")


    return my_numbers

valid_operations = ("sum", "average", "max", "min", "product")

Calculator_on = True
while Calculator_on:
    
    print("\nWelcome to the Flexible Calculator!\n\n")
    print("Available operations: sum, average, max, min, product\n\n")
    calculate = input("Which operation would you like to perform?\n").strip().lower()
    if calculate not in valid_operations:
        print("That's not an option. Maybe you typed it wrong.")
    else:
        numbers = get_numbers()
        if calculate == "sum":
            answer = number_sum(*numbers)
            if answer.is_integer():
                answer = int(answer)
            print(f"Your answer is {answer}\n")
        elif calculate == "average":
            answer = number_average(*numbers)
            if answer.is_integer():
                answer = int(answer)
            print(f"Your answer is {answer}\n")
        elif calculate == "max":
            answer = number_max(*numbers)
            if answer.is_integer():
                answer = int(answer)
            print(f"Your answer is {answer}\n")
        elif calculate == "min":
            answer = number_min(*numbers)
            if answer.is_integer():
                answer = int(answer)
            print(f"Your answer is {answer}\n")
        elif calculate == "product":
            answer = number_product(*numbers)
            if answer.is_integer():
                answer = int(answer)
            print(f"Your answer is {answer}\n")
        continue_calculating = input("Do you want to contuniue? (Y/N)\n").strip().capitalize()
        while True:
            if continue_calculating == "Y":
                break
            elif continue_calculating == "N":
                Calculator_on = False
                break
            else:
                print("Just type y or n, it doesn't work otherwise.\n")
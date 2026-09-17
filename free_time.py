#Korben Gardner Ravager Snack Bar
import random

pirate_name = input("What's your name, pirate? ")
snack_name = input("What snack do you want? ")

price = random.randint(2, 8)  # random price in credits
while True: # add while true to make them only give a number
    try:
        quantity = int(input("How many would you like? ")) # made it an integer
    except:
        print("Please put a number")
    else:
        break
total = price * quantity

discounted_total = total - total * 0.10 # discount is total minus total with discount

tax_rate = 0.08
total_with_tax = discounted_total + (discounted_total * tax_rate)

print("Hello, " + pirate_name + "! Here's your order summary:")
print("Snack: " + snack_name) #changed snackName to snack_name
print("Price per snack: " + str(price) + " credits")
print("Total before tax: " + str(discounted_total) + " credits") # changed from price per snack to discount total and put it in credits
print("Total with tax: " + str(round(total_with_tax, 2)) + " credits") # put end parentheses
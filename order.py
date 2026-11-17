#KG order up! assignment
import time as t

def clear_terminal():
    """clears the extra stuff from the terminal"""
    print("\033[H\033[J", end="")

clear_terminal()

menu = {
    "Plates": {
        "1 Entree + Fried Rice or Chow Mein": 14,
        "2 Entrees + Fried Rice or Chow Mein": 16,
        "3 Entrees + Fried Rice or Chow Mein": 18,
    },
    "Entrees": {

    "Orange Chicken": 13,
    "String Bean Chicken Breast": 13,
    "Beijing Beef": 13,
    "Honey Walnut Shrimp": 15,
    "Kung Pao Chicken": 13,
    "Broccoli Beef": 13,
    "Black Pepper Chicken": 13,
    "Mushroom Chicken": 14,
    "Veggie Spring Rolls": 15,
    
    },
    "Sides": {
        "Fried Rice": 4,
        "Chow Mein": 4,
        "Super Greens": 3
    },
    "Drinks": {
        "Fountain Drink": 3,
        "Iced Tea": 3,
        "Bottled Water": 2
    }
}





t.sleep(1)
print("Welcome to Panda Express!\n\n")
t.sleep(2)
print("Here's your menu:\n\n")

for category, items in menu.items():
    print(f"\n--- {category.upper()} ---")
    for item, price in items.items():
        print(f"  {item:<38} ${price}")

t.sleep(4)
print()
print()
order = input("What would you like to order?\n").capitalize()
for categpory, items in menu.items():
    if order in menu:
        for order in 
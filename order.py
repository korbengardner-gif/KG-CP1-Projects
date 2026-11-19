#KG order up! assignment
import time as t

def clear_terminal():
    """clears the extra stuff from the terminal"""
    print("\033[H\033[J", end="")

clear_terminal()

def combo_order():
    """This is how they order the plate size"""
    while True:
        combo = input("What plate size do you want?\n")
        if combo in menu["Plates"]:
            price = menu["Plates"][combo]
            if combo == "1 Entrees + Fried Rice or Chow Mein":
                return 1, price
            elif combo == "2 Entrees + Fried Rice or Chow Mein":
                return 2, price
            elif combo == "3 Entrees + Fried Rice or Chow Mein":
                return 3, price
        else:
            print("Dat don't exist. Maybe you typed it wrong.")

def entree_order(num_entrees):
    """this is how they order their entrees with the required number of entrees"""
    chosen_entrees = []
    while len(chosen_entrees) < num_entrees:
        choice = input(f"Pick entree #{len(chosen_entrees) + 1}:\n").strip().title()
        if choice in menu["Entrees"]:
            chosen_entrees.append(choice)
            print(f"Added {choice}!")
        else:
            print("Dat don't exist on the entree menu. Try again.")
    return chosen_entrees


menu = {
    "Plates": {
        "1 Entrees + Fried Rice or Chow Mein": 14,
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
        "Bo'ohw'o'wo'er": 2
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
print("\n")

entrees_needed, total_price = combo_order()
my_entrees = entree_order(entrees_needed)
print(f"\nYou ordered: {', '.join(my_entrees)}")
print(f"Current total: ${total_price}")
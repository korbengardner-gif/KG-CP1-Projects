#KG shopping list manager assignment


shopping_list = []

while True:
    action = input("What do you want to do? (add, remove, veiw list, or exit): ")
    if action == "add":
        new_item = input("What do you want to add? ")
        if new_item in shopping_list:
            print("That is already in your list!")
        else:
            shopping_list.append(new_item)
            print("Your list: ") 
            print(*shopping_list, sep=", ")
    elif action == "remove":
        item = input("what do you want to remove? ") 
        if item not in shopping_list:
            print("That's not in your list")
        else:
            shopping_list.remove(item)
            print("Your list: ") 
            print(*shopping_list, sep=", ")
    elif action == "veiw list":
        print("Your list: ") 
        print(*shopping_list, sep=", ")
    elif action == "exit":
        break
    else:
        print("That's not an option!")
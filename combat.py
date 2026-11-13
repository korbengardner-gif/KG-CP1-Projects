#KG combat assignment
import random as r
import time as t

energy = 5
enemy_health = 40
user_health = 25
block = False

def clear_terminal():
    """clears the extra stuff from the terminal"""
    print("\033[H\033[J", end="")

clear_terminal()

def user_turn():
    """This will ask the user what they want to do"""
    action = input("Pick an action\n\nAttack\n\nBlock\n\nHeal\n\nFlee\n\n").title()
    if action == "Attack":
        attack = input("Pick an attack\n\nPunch\n\nKick\n\nFireball\n\n").title()
        if attack == "Punch":
            return "damage5"
        elif attack == "Kick":
            return "damage10"
        elif attack == "Fireball":
            return "damage25"
        else:
            print("Not an option")
    elif action == "Block":
        return "block"
    elif action == "Heal":
        return "heal"
    elif action == "Flee":
        return "flee"
    else:
        print("Thats not an option")

def Enemy_turn():
    """This will pick wether the enemy attacks or heals"""
    action = r.randint(1,2)
    if action == 1:
        return action
    else:
        return action




intro = True #I want to have the intro in a seperate loop so they can choose to exit the battle but they are still in the game

while intro:
    t.sleep(1)
    print("Welcome to combat training!\nYou will fight my champion to test your skills.\nHeal to stay alive.\nYou can back out whenever you want.")
    t.sleep(5)
    print("Time to Fight!\n")
    t.sleep(1)
    fighting = True #starts the actual battle
    while fighting:
        if user_health <= 0:
            print("You lost. The enemy did too much damage.")#if you have taken too much damage, it stops you from going
            fighting = False 
            break
        user_action = user_turn()
        if user_action == "damage5": #punch action 
            print("You used Punch!")
            t.sleep(2)
            enemy_health -= 5
            print("The enemy took 5 damage")
            t.sleep(2)
        elif user_action == "damage10": #kick action
            print("You used Kick!")
            t.sleep(2)
            enemy_health -= 10
            print("The enemy took 10 damage")
            t.sleep(2)
        elif user_action == "damage25": #fire ball action
            print("You used Fireball!")
            t.sleep(2)
            enemy_health -= 25
            print("The enemy took 25 damage")
            t.sleep(2)
        elif user_action == "heal": #heal action
            print("You used Heal!")
            t.sleep(2)
            heal = r.randint(5,10)
            user_health += heal
            print(f"You heal {heal}!")
            t.sleep(2)
        elif user_action == "block": #block action
            block = True
        elif user_action == "flee": #flee action
            print("You flee the battle.")
            t.sleep(2)
            fighting = False
            break
        else:
            print("Thats not an option. Now the enemy has a chance to attack.") #if they input they wrong thing in the function, it just cancels their turn
            t.sleep(2)
        if enemy_health <= 0: #after you damage the enemy, this checks if he's dead
            print("You defeated him! I'm impressed. Thanks for playing, and Congratulations!")
            t.sleep(2)
            fighting = False 
            break
        enemy_action = Enemy_turn()
        if enemy_action == 1: #enemy attack
            print("The enemy Attacks")
            t.sleep(2)
            damage = r.randint(10,15)
            print(f"He does {damage} damage!")
            t.sleep(2)
            if block == True: #if you blocked it, it cancels itself
                damage = (damage - damage)
                print("You Blocked it!")
                block = False
            else:
                user_health -= damage
        else: #enemy heal
            print("The enemy Heals")
            t.sleep(2)
            enemyheal = r.randint(1,10)
            enemy_health += enemyheal
            print(f"He heals {enemyheal} health!")
            t.sleep(2)



    continue_playing = input("Do you want to play again? (Y/N)\n").capitalize()
    if continue_playing == "N":
        intro = False
        break
    elif continue_playing == "Y":
        continue
    else:
        print("please put just N or Y")
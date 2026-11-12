#KG combat assignment
import random as r

energy = 5
enemy_health = 40
user_health = 25
block = False
def user_turn():
    action = input("Pick an action\nAttack\nBlock\nHeal\nFlee\n").title()
    if action == "Attack":
        attack = input("Pick an attack\nPunch\nKick\nFire Ball").title()
        if attack == "Punch":
            damage = 5
            return damage
        elif attack == "Kick":
            damage = 10
            return damage
        elif attack == "Fire Ball":
            damage = 25
            return damage
        else:
            print("Not an option")
    elif action == "Block":
        block = True
        return block
    elif action == "Heal":
        healing = r.randint(5,10)
        user_health += healing
    elif action == "Flee":
        print("You flee the battle\nThanks for playing and come back soon!")
        fighting = False
    else:
        print("Thats not an option")

def Enemy_turn():
    action = r.randint(1,2)
    if action == 1:
        return action
    else:
        return action




intro = True

while intro:
    print("Welcome to combat training!\nYou will fight my champion to test your skills.\nCharge Energy to use more powerful attacks, and heal to stay alive.\nYou can back whenever you want.\nTime to fight!")
    fighting = True
    while fighting:
        user_turn()
        enemy_health -= damage
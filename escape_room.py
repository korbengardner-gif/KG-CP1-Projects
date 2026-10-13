#KG escape room assignment



playing = True


print("Welcome to my escape room: The Vault of The Vex!")
print("")
print("Your Fireteam has been tracking a strange spike in paracausal energy on Nessus. While exploring a network of caves, a shimmering, white-and-bronze geometric portal snaps open, pulling your team into a cold, hyper-advanced labyrinth. The mechanical clicks and radio-static clicks confirm it: you are inside a Vex Simulation Core.")
print("*Ghost* 'Be careful. One wrong move could have disastrous results")

while playing:
    # trial 1
    print("You stand in a triangular chamber. In the center, a towering glass pillar glows with pulsing white Radiolarian fluid. Three terminal consoles hum in front of it. Your Ghost identifies that you must enter a specific numerical sequence to proceed. Geometric symbols flicker above each console.")
    print("")
    print("Console A: 7-7-7")
    print("")
    print("Console B: 1-0-1")
    print("")
    print("Console C: 4-1-9")
    print("")

    choice = input("Which console do you choose (A, B, or C)\n").upper()
    if choice == "A":
        # Trial 2 choice A
        print("\n You advance to Trial 2.")
        print("")
        print(" You are teleported to a new room. A massive barrier of laser-like Vex Harpy wings blocks the exit. To short-circuit the grid, you must pull one of three elemental levers")
        print("")
        print("Lever A-1: Void Lever")
        print("Lever A-2: Solar Lever")
        print("Lever A-3: Arc Lever")
        print("")
        lever = input("Which lever do you pull(1, 2, or 3)\n")
        if lever == 1:
            # Trial 3 void lever
            print("")
            print("The grid drops. You sprint into a massive chasm. Floating in the air are two massive, shimmering portals. One glows with a Precursor Vex theme (Shining Gold and White), and the other glows with a Descendant Vex theme (Rusty, Ancient Metal).")
            print("")
            portal = input("Which Portal do you choose, Gold or Rusty\n").capitalize()
            print("")
            if portal == "Gold":
                print("")
                print("")
            elif portal == "Rusty":
                print("")
                print("")

        elif lever == 2:
            # Trial 3 solar lever
            print("")
            print("The grid drops. You sprint into a massive chasm. Floating in the air are two massive, shimmering portals. One glows with a Precursor Vex theme (Shining Gold and White), and the other glows with a Descendant Vex theme (Rusty, Ancient Metal).")
            print("")
            portal = input("Which Portal do you choose, Gold or Rusty\n")
            print("")
            if portal == "Gold":
                print("")
                print("")
            elif portal == "Rusty":
                print("")
                print("")

        elif lever == 3:
            # Trial 3 arc lever
            print("")
            print("The grid drops. You sprint into a massive chasm. Floating in the air are two massive, shimmering portals. One glows with a Precursor Vex theme (Shining Gold and White), and the other glows with a Descendant Vex theme (Rusty, Ancient Metal).")
            print("")
            portal = input("Which Portal do you choose, Gold or Rusty\n")
            print("")
            if portal == "Gold":
                print("")
                print("As you step through the portal, the Traveler's frequency you inputted back in Trial 1 overloads the Vex architecture. The simulation violently destabilizes, freezing your Fireteam mid-stride. You are locked into an infinite loop, transformed forever into living statues of stone and brass within the network.")
            elif portal == "Rusty":
                print("")
                print("As you step through the portal, the Traveler's frequency you inputted back in Trial 1 overloads the Vex architecture. The simulation violently destabilizes, freezing your Fireteam mid-stride. You are locked into an infinite loop, transformed forever into living statues of stone and brass within the network.")

        else:
            print("Invalid input. The Vex barrier  moves towards and cuts your body into millions of peices.")
            break


    elif choice == "B":
        # Trial 2 choice B
        print("\n You advance to Trial 2.")
        print("")
        print(" You are teleported to a new room. A massive barrier of laser-like Vex Harpy wings blocks the exit. To short-circuit the grid, you must pull one of three elemental levers")
        print("")
        print("Lever B-1: Void Lever")
        print("Lever B-2: Solar Lever")
        print("Lever B-3: Arc Lever")
        print("")
        lever = input("Which lever do you pull(1, 2, or 3)\n")

        if lever == 1:
            # Trial 3 void lever
            print("")
            print("The grid drops. You sprint into a massive chasm. Floating in the air are two massive, shimmering portals. One glows with a Precursor Vex theme (Shining Gold and White), and the other glows with a Descendant Vex theme (Rusty, Ancient Metal).")
            print("")
            portal = input("Which Portal do you choose, Gold or Rusty\n")
            print("")
            if portal == "Gold":
                print("")
                print("")
            elif portal == "Rusty":
                print("")
                print("")

        elif lever == 2:
            # Trial 3 solar lever
            print("")
            print("The grid drops. You sprint into a massive chasm. Floating in the air are two massive, shimmering portals. One glows with a Precursor Vex theme (Shining Gold and White), and the other glows with a Descendant Vex theme (Rusty, Ancient Metal).")
            print("")
            portal = input("Which Portal do you choose, Gold or Rusty\n")
            print("")
            if portal == "Gold":
                print("")
                print("")
            elif portal == "Rusty":
                print("")
                print("")

        elif lever == 3:
            # Trial 3 arc lever
            print("")
            print("The grid drops. You sprint into a massive chasm. Floating in the air are two massive, shimmering portals. One glows with a Precursor Vex theme (Shining Gold and White), and the other glows with a Descendant Vex theme (Rusty, Ancient Metal).")
            print("")
            portal = input("Which Portal do you choose, Gold or Rusty\n")
            print("")
            if portal == "Gold":
                print("")
                print("")
            elif portal == "Rusty":
                print("")
                print("")

        else:
            print("Invalid input. The Vex barrier  moves towards and cuts your body into millions of peices.")
            break


    elif choice == "C":
        # Trial 2 choice C
        print("\n You advance to Trial 2.")
        print("")
        print(" You are teleported to a new room. A massive barrier of laser-like Vex Harpy wings blocks the exit. To short-circuit the grid, you must pull one of three elemental levers")
        print("")
        print("Lever C-1: Void Lever")
        print("Lever C-2: Solar Lever")
        print("Lever C-3: Arc Lever")
        print("")
        lever = input("Which lever do you pull(1, 2, or 3)\n")

        if lever == 1:
            # Trial 3 void lever
            print("")
            print("The grid drops. You sprint into a massive chasm. Floating in the air are two massive, shimmering portals. One glows with a Precursor Vex theme (Shining Gold and White), and the other glows with a Descendant Vex theme (Rusty, Ancient Metal).")
            print("")
            portal = input("Which Portal do you choose, Gold or Rusty\n")
            print("")
            if portal == "Gold":
                print("")
                print("")
            elif portal == "Rusty":
                print("")
                print("")

        elif lever == 2:
            # Trial 3 solar lever
            print("")
            print("The grid drops. You sprint into a massive chasm. Floating in the air are two massive, shimmering portals. One glows with a Precursor Vex theme (Shining Gold and White), and the other glows with a Descendant Vex theme (Rusty, Ancient Metal).")
            print("")
            portal = input("Which Portal do you choose, Gold or Rusty\n")
            print("")
            if portal == "Gold":
                print("")
                print("")
            elif portal == "Rusty":
                print("")
                print("")

        elif lever == 3:
            # Trial 3 arc lever
            print("")
            print("The grid drops. You sprint into a massive chasm. Floating in the air are two massive, shimmering portals. One glows with a Precursor Vex theme (Shining Gold and White), and the other glows with a Descendant Vex theme (Rusty, Ancient Metal).")
            print("")
            portal = input("Which Portal do you choose, Gold or Rusty\n")
            print("")
            if portal == "Gold":
                print("")
                print("")
            elif portal == "Rusty":
                print("")
                print("")

        else:
            print("Invalid input. The Vex barrier  moves towards and cuts your body into millions of peices.")
            break

    else:
        print("Invalid input. You are now stuck here.")
        break
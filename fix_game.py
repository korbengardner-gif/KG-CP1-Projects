#KG fix the game assignment


import random

scores = []
rounds = 3

print("Welcome to Guess the Number! You'll play 3 rounds.")
print("Each round, try to guess the number in as few tries as possible.\n")

for round_num in range(1, rounds + 1):
    secret_number = random.randint(1, 20)
    guesses = 0
    found = False

    print(f"--- Round {round_num} ---")

    while found == False:
        guess = int(input("Guess a number between 1 and 20: "))
        guesses = guesses + 1

        if guess == secret_number:  #syntax error, added ":"
            print(f"Correct! It took you {guesses} guesses.")
            found = True
        elif guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")

    scores.append(guesses)

print("\n--- Game Over ---")
print("Your guesses per round:", *(f"round {i} = {s}" for i, s in enumerate(scores, start=1)), sep="\n") #syntax error, you have to unpack the list cause you can't just add a list to a str. I also made it print each item with its corresponding round to be user friendly

total = 0
for score in scores:
    #logic error, total = 0 is unnecessary
    total = total + score

average = round(total / rounds,1)
print("Your average guesses per round was " + str(average))

best_round = scores[0]
for i in range(1, rounds + 1):#logic error, the range was ignoring the second and third rounds, but now it includes them
    if scores[i] < best_round:
        best_round = scores[i]

print(f"Your best round took only {best_round} guesses!")
#KG crew shares assignment
import random

start_units = random.randint(5000000,5000000000)

while True:
    try:
        crew = int(input("How many pirates are there: "))
    except:
        print("Put a number!")
    else:
        break

units = start_units - crew * 3
print(f"There are {units} units!")

yondu_cut = round(units * 0.13, 2)
print(f"Yondu took {yondu_cut} units.")

after_yonducut = units - yondu_cut
print(f"There are now {after_yonducut} units.")


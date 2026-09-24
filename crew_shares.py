#KG crew shares assignment
import random

start_units = random.randint(50000,500000)

while True:
    try:
        crew = int(input("How many pirates are there: "))
    except:
        print("Put a number!")
    else:
        break

units = start_units - crew * 3

yondu_cut = round(units * 0.13, 2)

after_yonducut = units - yondu_cut

peter_cut = round(after_yonducut * 0.11)

after_petercut = after_yonducut - peter_cut

crew_share = round(after_petercut / (crew + 2))

yondu_total =  yondu_cut + crew_share
peter_total =  peter_cut + crew_share

print(f"There are {crew + 2} pirates.")
print(f"They have {units} units.")
print(f"Yondu gets {yondu_total} units!")
print(f"Peter gets {peter_total} units!")
print(f"The rest of the crew gets {crew_share + 3} units!")
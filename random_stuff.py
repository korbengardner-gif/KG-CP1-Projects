#Korben Gardner random code thingies
import turtle as t

"""
def typer_print(text: str, end = "\n"):"""

"""window = t.Screen()
window.bgcolor("black")
t.showturtle()

t.width(50)

for steps in range(100):
    for c in ('blue', 'red', 'green'):
        t.color(c)
        t.forward(steps)
        t.right(30)

t.exitonclick()"""

"""purple = 0
yellow = 0
tRue = True
true = True


while tRue:
    while true:
        print("E")
        purple += 1
        if purple == 9:
            true = False
            break
    print("A")
    yellow += 1
    if yellow == 9:
        tRue = False
        break"""

""""""

"""
"""


# collecton of key and value pairs

car = {
    #Key: Value
    "make": "Jeep",
    "model": "Wrangler",
    "color": "silver",
    "year": 2023
}


values = list(car.keys())

print(values)
print(len(car))
if "transmission" in car:
    print(car["transmission"])
else:
    car["transmission"] = "automatic"

car.pop("color")
print(car.items())
keys = list(car.keys())
for key in keys:
    print(f"{key} is {car[key]}")



avatar = {
    "Water": {
        "Katara": "Water bender.",
        "Sokka": "Leader. Boomerang guy. Idea guy. Sword master",
    },
    "Earth": {
        "Toph": "Earth bender. THE GOAT!",
        "Suki": "Warrior from Kyoshi Island.",
        "Cabbage Merchant": "MY CABBAGES!!!!!!!"
    },
    "Air": {
        "Aang": "Air bender, The Avatar."
    },
    "Fire": {
        "Zuko": "Fire bender, future fire lord.",
        "Iroh": "The actual GOAT. Fire bender, Dragon of the West.",
        "Azula": "Fire lord for 1 hour. Amazing fire bender."
    }
}

print(avatar["Fire"]["Iroh"])
print(avatar.get("Earth").get("Cabbage Merchant"))
print(avatar["Water"]["Sokka"])
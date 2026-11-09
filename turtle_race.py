#KG turtle race assignment

import turtle as t
import time
import random

def turtle_speed():
    # Returns a random integer from 1 to 5 for the turtle speed
    return random.randint(1, 5)


background = t.Screen()
background.bgcolor("black")

finish_line = t.Turtle()
greenturtle = t.Turtle()
blueturtle = t.Turtle()
redturtle = t.Turtle()
purpleturtle = t.Turtle()
cyanturtle = t.Turtle()

greenturtle.shape("turtle")
blueturtle.shape("turtle")
redturtle.shape("turtle")
purpleturtle.shape("turtle")
cyanturtle.shape("turtle")

greenturtle.up()
blueturtle.up()
redturtle.up()
purpleturtle.up()
cyanturtle.up()

greenturtle.goto(-500, 250)
greenturtle.color("green")
blueturtle.goto(-500, 125)
blueturtle.color("blue")
cyanturtle.goto(-500, 0)
cyanturtle.color("cyan")
redturtle.goto(-500, -125)
redturtle.color("red")
purpleturtle.goto(-500, -250)
purpleturtle.color("purple")

finish_line.up()
time.sleep(1)

finish_line.goto(400, 400)
finish_line.down()
finish_line.color("white")
finish_line.goto(400, -400)
finish_line.hideturtle()

greenturtle.down()
blueturtle.down()
redturtle.down()
purpleturtle.down()
cyanturtle.down()


race_in_progress = True

while race_in_progress:
    for c in (greenturtle, blueturtle, cyanturtle, redturtle, purpleturtle):
        distance = random.randint(1,5)
        c.fd(distance)






























t.exitonclick()
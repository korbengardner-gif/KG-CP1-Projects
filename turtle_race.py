#KG turtle race assignment

import turtle as t
import time
import random

def clear_terminal():
    #clears the extra stuff from the terminal
    print("\033[H\033[J", end="")

clear_terminal()

def turtle_speed():
    # Returns a random integer from 1 to 5 for the turtle speed
    return random.randint(1, 5)


background = t.Screen()
background.bgcolor("black") #set the background to black

finish_line = t.Turtle() #our racers! plus the finish line drawer
green = t.Turtle()
blue = t.Turtle()
red = t.Turtle()
orange = t.Turtle()
cyan = t.Turtle()

green.shape("turtle") #we want turtles not cursors
blue.shape("turtle")
red.shape("turtle")
orange.shape("turtle")
cyan.shape("turtle")

green.up() #we don't want them to draw yet
blue.up()
red.up()
orange.up()
cyan.up()

green.goto(-500, 250) # RACERS To Your Positions! 
green.color("green")
blue.goto(-500, 125)
blue.color("blue")
cyan.goto(-500, 0)
cyan.color("cyan")
red.goto(-500, -125)
red.color("red")
orange.goto(-500, -250)
orange.color("orange")

finish_line.up()
time.sleep(1)

finish_line.hideturtle() #Draw their finish line
finish_line.goto(400, 400)
finish_line.down()
finish_line.pensize(15)
finish_line.color("white")
finish_line.goto(400, -400)

green.down()
blue.down()
red.down()
orange.down()
cyan.down()

# this guy will anounce the winner
writer = t.Turtle()
writer.hideturtle()
writer.penup()
writer.goto(0, 250) # this moves him to the top center of the screen



race_in_progress = True # starts our race

racer = 1 #this helps us check for the winner

while race_in_progress:
    for c in (green, blue, cyan, red, orange):
        distance = random.randint(1,20)
        c.fd(distance)
        if c.xcor () >= 400: #checks each color to see who won

            # now we announce the winner
            winner_name = c.pencolor().capitalize() 
            message = f"{winner_name} Won the Race!"
            writer.color(c.pencolor()) 
            writer.write(message, align="center", font=("Arial", 36, "bold"))
            #end the race
            race_in_progress = False
            break






































t.exitonclick()
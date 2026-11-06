#Korben Gardner random code thingies
import turtle as t

"""def typer_print(text: str, end = "\n"):
                """


window = t.Screen()
window.bgcolor("black")
t.showturtle()

t.width(50)

for steps in range(100):
    for c in ('blue', 'red', 'green'):
        t.color(c)
        t.forward(steps)
        t.right(30)

t.exitonclick()
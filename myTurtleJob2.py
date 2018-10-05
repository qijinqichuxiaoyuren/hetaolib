import turtle
Tina = turtle.Pen()
turtle.bgcolor("black")
Tina.speed(0)
sides = 3
colors = ["red", "yellow", "blue", "orange", "green", "purple"]
for x in range(360):
    Tina.pencolor(colors[x%sides])
    Tina.forward(x * 3 / sides + x)
    Tina.left(360/sides + 1)
    Tina.width(x*sides/100)

import turtle
Tina = turtle.Pen()
Tina.speed(0)
Tina.shape('turtle')
colors = ["red", "yellow", "blue", "green"]
for x in range(200):
    Tina.pencolor( colors[ x % 4] )
    Tina.forward(2 * x)
    Tina.left(91)

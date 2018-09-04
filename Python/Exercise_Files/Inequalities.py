# Change the temperatureColor function so
# it returns "blue" for cold temperatures,
# "purple" for medium temperatures, and
# "red" for hot temperatures.
#
# You decide what is cold, medium, or hot!
#
# (It should never return "green".)

import turtle

def temperatureColor(temp):
    # Change this code!
    if temp < 30:
        return "blue"
    elif temp <= 80:
        return "purple"
    elif temp >= 81:
        return "red"
    else:
        return "green"

def drawTemperature(temp):
    t = turtle.Turtle()
    t.penup()
    t.back(100)
    t.width(20)
    t.pendown()
    for step in range(temp):
        t.color(temperatureColor(step))
        t.forward(1)

def drawThermBox():
    t = turtle.Turtle()
    t.speed(0)
    t.color("gray")
    t.penup()
    t.back(120)
    t.pendown()
    t.left(90)
    for side in [20, 240, 40, 240, 20]:
        t.forward(side)
        t.right(90)
    t.hideturtle()

drawThermBox()
drawTemperature(120)


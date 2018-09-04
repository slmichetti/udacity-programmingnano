import turtle
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

t = turtle.Turtle()
t.width(20)

for step in range(100):
    # Change this to use a random number.
    angle = random.randint(20, 180)

    # Change this to use a random color.
    c = random.choice(colors)

    t.color(c)
    t.right(angle)
    t.forward(10) 
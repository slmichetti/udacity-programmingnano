# You can use the 'fizz', 'buzz', and
# 'plain' functions to draw beads.
#
# Feel free to change them, too!
#
# Beneath them, write a loop from 0 to 15.
# For each number ...
# ... if it is a multiple of 3, call fizz.
# ... if it is a multiple of 5, call buzz.
# ... if it is both, call both functions.
# ... if it is neither, call plain.

import turtle

def fizz(tur):
    # A red square bead.
    tur.color("red")
    tur.left(90)
    for side in [10, 20, 20, 20, 10]:
        tur.forward(side)
        tur.right(90)

def buzz(tur):
    # A green hexagonal bead.
    # Fits inside the red bead.
    tur.color("green")
    tur.left(60)
    for side in range(6):
        tur.forward(10)
        tur.right(60)
    tur.right(60)

def plain(tur):
    # A gray octagonal bead.
    tur.color("gray")
    tur.left(90)
    for side in [4, 8, 8, 8, 8, 8, 8, 8, 4]:
        tur.forward(side)
        tur.right(45)
    tur.right(45)

# Set up the turtle to draw beads.
t = turtle.Turtle()
t.speed(0)
t.width(2)
t.penup()
t.back(180)  # Back up to make room!
t.pendown()

for num in range(16):
    if num % 15 == 0:
        fizz(t)
        buzz(t)
    elif num % 3 == 0:
        fizz(t)
    elif num % 5 == 0:
        buzz(t)
    else:
        plain(t)

    t.forward(22)
t.hideturtle()



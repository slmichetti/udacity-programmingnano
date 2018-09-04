
return to the code that calls that function

sides = range(4)
	for side in sides:
		t.forward(sq)

function: nearWall(t)
	it evaluates if t is near a wall
a function calls the variable (t)
returned value because the value of the function call expression


something = nearWall
(retuns value)

step = 5
fox x in range(200):
	if not nearWall(t):
		t.forward(step)
		t.right(90)
		step += 1



MY SOLUTION
import turtle
import random
import vacuumsetup

def vacuumTurtle():
    # Create a vacuum turtle.
    t = turtle.Turtle()
    t.width(30); t.speed(0)
    t.color("white")
    return t

def nearWall(t):
    # Is the turtle near a wall?
    x, y = t.pos()
    bounds = 100 - t.width() * 2/3
    return not (-bounds < x < bounds
            and -bounds < y < bounds)

def cleanRoom():
    t = vacuumTurtle()
    for step in [5, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]:
        if not nearWall(t):
            t.forward(step)
            t.left(90)


# Don't remove this function call!
cleanRoom()

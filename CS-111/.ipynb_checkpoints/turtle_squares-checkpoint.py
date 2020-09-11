"""Draws squares with turtle
"""

import turtle


bob = turtle.Turtle()

jill = turtle.Turtle()


def drawSquare(myTurtle, x, y, sideLength=100): 
    myTurtle.goto(x,y)
    for i in range(4):
        myTurtle.forward(sideLength)
        myTurtle.left(90)
        

        
drawSquare(jill, -50, 100)

drawSquare(bob, 70, -70, 200)

drawSquare(jill, 100, 200, 40)

drawSquare(bob,  -50, -100, 300)

turtle.done()                #warning, need this as last line of your script!
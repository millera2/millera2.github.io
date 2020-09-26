"""
This program acts as a functional abstraction since the finctions spread, zoom, and slide "black-blox" the problem and outpouts a solution for the given inputs (the steps are shortened and doesn't make the user have to understand the step to get a solution/output).
"""

import turtle

def drawSquare(tortoise, heading, x, y, length):
    tortoise.goto(x,y)
    tortoise.setheading(heading)
    tortoise.fillcolor()
    tortoise.begin_fill()
    for i in range(4):
        tortoise.forward(length)
        tortoise.left(90)
    tortoise.end_fill()
   
    
def drawTriangle(tortoise, heading, x, y, length):
    tortoise.goto(x,y)
    tortoise.setheading(heading)
    tortoise.fillcolor()
    tortoise.begin_fill()
    for i in range(3):
        tortoise.forward(length)
        tortoise.left(120)
    tortoise.end_fill()
    
def spread(tortoise, heading, x, y, length):
    if (shapeInput=="Square"):
        for squareDraw in range(5):
            drawSquare(tortoise, heading, x, y, length)
            heading = heading + 25
    elif (shapeInput=="Triangle"):
        for triangleDraw in range(5):
            drawTriangle(tortoise, heading, x, y, length)
            heading = heading + 25
    else :
        print("Sorry, please enter either Square or Triangle!")
    
    
def zoom(tortoise, heading, x, y, length):
    if (shapeInput=="Square"):
        for squareDraw in range(5):
            drawSquare(tortoise, heading, x, y, length)
            x = x - 30
            length = length + 60     
    elif (shapeInput=="Triangle"):
        for triangleDraw in range(5):
            drawTriangle(tortoise, heading, x, y, length)
            x = x - 30
            length = length + 60
    else :
        print("Sorry, please enter either Square or Triangle!")
    
def slide(tortoise, heading, x, y, length, color):
    if (shapeInput=="Square"):
        for squareDraw in range(5):
            drawSquare(tortoise, heading, x, y, length)
            x = x - 30     
    elif (shapeInput=="Triangle"):
        for triangleDraw in range(5):
            drawTriangle(tortoise, heading, x, y, length)
            x = x - 30
    else :
        print("Sorry, please enter either Square or Triangle!")
    


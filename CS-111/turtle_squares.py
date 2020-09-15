"""Draws squares with turtle module.
"""

import turtle


def drawSquare(myTurtle, x, y, sideLength=100):     # def for square function
    """This was my stupid docstring"""
    myTurtle.goto(x,y)                              # set startin place for turtle
    for i in range(4):                              # need to repeat 4 times
        myTurtle.forward(sideLength)
        myTurtle.left(90) 

def main():        
    bob = turtle.Turtle()           #making a new turle with Turtle() constructor
    jill = turtle.Turtle()          # making a second turtle
    defaultSideLength = 100         #if user doesn't specify, side length is this!
    drawSquare(jill, -50, 100)
    drawSquare(bob, 70, -70, 200)
    drawSquare(jill, 100, 200, 40)
    drawSquare(bob,  -50, -100, 300)
    turtle.done()                #warning, need this as last line of your script!  
    
main()

import turtle

bob = turtle.Turtle()     #Using the "constructor function"  Turtle().  
jill = turtle.Turtle()    # Creating a new turtle object.


    
def makeSquare(sidelength):
    for i in range(4):
        bob.forward(sidelength)
        bob.left(90)
    


makeSquare()

screen = bob.gets


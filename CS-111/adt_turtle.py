
import turtle

bob = turtle.Turtle()     #Using the "constructor function"  Turtle().  
jill = turtle.Turtle()    # Creating a new turtle object.


screen = bob.getscreen()

def makeSquare(sidelength):
    for i in range(4):
        bob.forward(sidelength)
        bob.left(90)
    
    
def moveToClick(x,y):
    bob.goto()
    
bob.onclick(moveToClick)
    


turtle.mainloop()


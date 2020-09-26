"""This code will allow you to make shapes(Triangles and squares) and spread, zoom or slide the shapes in turtle """

import turtle
nelly=turtle.Turtle()  ## square turtle
benny=turtle.Turtle()  ## triangle turtle
milly=turtle.Turtle()



"""This code defines a square
"""
def makeSquare(tortise, heading, x, y, length, fillColor):
    tortise.penup(),tortise.goto(x,y),tortise.pendown()
    tortise.fillcolor(fillColor)
    tortise.begin_fill()
    for i in range(4):
        tortise.forward(length)
        tortise.left(heading)
    tortise.end_fill()
    
makeSquare(nelly,90,0,200, 100, "orchid")



"""This code spreads the square achieved in the previous code
            angle= is the shifting angle for the shape
            n= the number of times to spread the angle
"""
makeSquare(nelly,90,0,200, 100, "orchid")

def spread(tortise,myshape,angle,n):
    for i in range(n):
        tortise.left(angle)
        makeSquare(nelly,90,0,200, 100, "orchid")
        
""" The user choose the angle of shift and the nymber of times the spreading code runs 
"""   
spread(nelly,makeSquare,10,3)




def makeTriangle(tortise, heading,x,y,length, fillColor):
    tortise.penup(),tortise.goto(x,y),tortise.pendown()
    tortise.fillcolor(fillColor)
    tortise.begin_fill()
    
    for i in range(3):
        tortise.forward(length)
        tortise.left(heading)
    tortise.end_fill()
    
    
    
makeTriangle(benny, 120, 0,0, 200, "lightgoldenrodyellow")

"""This code zooms in the triangle achieved in the previous code
        length=starting length/length of the bigger triangle
        n is the number of times to zoom the triangle.
"""
def zoom(myshape,length,n,differencelength,x=0):
     for i in range(n):
        Mylength=length-differencelength*i
        makeTriangle(benny,120,x+(length-Mylength)/2,0,Mylength,"lightgoldenrodyellow")
        
        
        
"""The user can choose the length of the triangle, the number of times the zoom function runs and the difference in length between each triangle
"""

zoom(makeTriangle,200,4,40)

"""This code slides the triangle in the previous code 
by changing the starting position of the shape along the same y-axis:
the user enters: an x value into the code
                 The y value is defaulted in the definition of the function because it does not need to change.
"""

makeTriangle(milly, 120, -20, -200,160, 'lightcoral')
def slide(myshape,tortise,n,increaseinx,y=-200,x=-20):
    for i in range(n):
        tortise.goto(x,y)
        x=x+increaseinx
        makeTriangle(milly,120,x,y,160,"lightcoral")
        
        
""" The user can choose the number of times n to run the slide code, the increase in x. x and y are defaulted in the code because they depend on the initial shape
"""   

slide(makeTriangle,milly,4,50,-200)



"""Functional abstraction is this program is apparent when defining the spread, zoom and slide functions. 
I predefined the shapes Triangle and Square and used their definitions to further define the actions To be performed 
"""
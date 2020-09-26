"""
Purpose: Draw Shape Patterns Based On The Input 
By: Paneri Patel
Date: September 25, 2020
CS 111, Fall 2020
"""

import turtle

def makeTriangle(tortise, heading, x, y, fillColor, sideLength): #Parameter can be ANYTHING as long as you use that name consistantly #x and y are the coordinates
    """ Draws an Equilateral Triangle based on the inputs.
    
    Parameters:
        tortise: a Turtle object with which to draw the triangle
        heading: set's the orientation of the turtle to an angle,(starting heading of the triangle).
        x: x-coordinate of the triangle     
        y: y-coordinate of the triangle 
        fillColor: a color string to use to fill the triangle 
        sideLength: the length of each segment of the triangle 
        
    Output: A defined equilateral triangle drawn in the turtle window.  
        
    """
    
    tortise.fillcolor(fillColor)
    tortise.up()    #it is used to draw out the tortise #Moves without drawing - tortise.up()    
    tortise.goto(x, y) #it is used to move curson at x and y position 
    tortise.setheading(heading)
    tortise.down()            #it is used to draw out the tortise #Moves without drawing - tortise.down() 
    tortise.begin_fill()    #beginfill--> indicate when to fill the triangle
    for i in range (4):              #myTurtle is the turle object passed by the function
        tortise.forward(sideLength)  #move cursor to the sidelength depending on the input
        tortise.left(120)            #Turns the cursor to 120 degree left()
    tortise.end_fill()     #endfill --> indicates when to end 

def makeSquare(tortise, heading, x, y, fillColor, sideLength):   #Parameter can be ANYTHING as long as you use that name consistantly #x and y are the coordinates
    """ Draws a Square based on the inputs. 
    
    Parameters:
        tortise: a Turtle object with which to draw the Square
        heading: set's the orientation of the turtle to an angle,(starting heading of the square). 
        x: x-coordinate of the square     
        y: y-coordinate of the square 
        fillColor: a color string to use to fill the Square 
        sideLength: the length of each segment of the Square 
        
    Output: A defined square drawn in the turtle window. 
    """
    tortise.fillcolor(fillColor)
    tortise.up()    #it is used to draw out the tortise #Moves without drawing - tortise.up()    
    tortise.goto(x, y) #it is used to move curson at x and y position 
    tortise.setheading(heading)
    tortise.down()            #it is used to draw out the tortise #Moves without drawing - tortise.down() 
    tortise.begin_fill()    #beginfill--> indicate when to fill the square
    for i in range (4):              #myTurtle is the turle object passed by the function
        tortise.forward(sideLength)  #move cursor to the sidelength depending on the input
        tortise.left(90)            #Turns the cursor to 120 degree left()
    tortise.end_fill()     #endfill --> indicates when to end 
        

def spread(option, tortoise, heading, x, y, fillColor, sideLength): #option parameter used as the given options aviable 
    ## A function that draws multiple shapes on top of each other, rotating by a certain angle.  
    
    ## Parameters: 
        #tortise: a Turtle object with which to draw the shape
       # heading: set's the orientation of the turtle to an angle,(starting heading of the shape). 
        # x: x-coordinate of the specified first shape    
       # y: y-coordinate of the specified first shape
        #fillColor: a color string to use to fill the shape
        #sideLength: the sidelength of the shape  
        
    #Output: A defined shape drawn in the turtle window, depending on the input. 
    
    
    if option == "square":
        for i in range (5):
            makeSquare(tortoise, heading+i*30, x, y, fillColor, sideLength)
    elif option == "triangle":
        for i in range (5):
            makeTriangle(tortoise, heading + i * 30, x, y, fillColor, sideLength)
            
def zoom(option, tortoise, heading, x, y, fillColor, sideLength): 
    ## Zooming in or out, this function draws a mupltiple shapes on top of each other.

    ## Parameters:
       # tortise: a Turtle object with which to draw the shape
       # heading: set's the orientation of the turtle to an angle,(starting heading of the shape). 
    # x: x-coordinate of the specified first shape    
        #y: y-coordinate of the specified first shape
        #fillColor: a color string to use to fill the shape
       # sideLength: the sidelength of the shape  
        
    # Output: A defined shape drawn in the turtle window, depending on the input. 

    
    if option == "square":
        for i in range (5):
            makeSquare(tortoise, heading, x+10*i, y, fillColor, sideLength - 2*i*10)        
    elif option == "triangle":
        for i in range (5):
            makeTriangle(tortoise, heading, x+10*i, y, fillColor, sideLength - 2*i*10)
            
def slide(option, tortoise, heading, x, y, fillColor, sideLength): 
    ## A function that draws a mupltiple shapes relocated by certain value in the heading direction.

   ## Parameters:
       # tortise: a Turtle object with which to draw the shape
       # heading: set's the orientation of the turtle to an angle,(starting heading of the shape). 
       #x: x-coordinate of the specified first shape    
    #y: y-coordinate of the specified first shape
        #fillColor: a color string to use to fill the shape
        #sideLength: the sidelength of the shape  
        
    ## Output: A defined shape drawn in the turtle window, depending on the input. 
    
    if option == "square":
        for i in range (5):
            tortoise.forward(10)
            makeSquare(tortoise, heading, x+i*10, y, fillColor, sideLength)        
    elif option == "triangle":
        for i in range (5):
            tortoise.forward(10)
            makeTriangle(tortoise, heading, x+i*10, y, fillColor, sideLength)

def main():
    """Draws a Shape Pattern based on the input of the users, the user decides what will the sideLength, color, coordinates, function. 
    """
    a = input("Triangle or square (type triangle or square): ") #Shape 
    b = int(input("what is the side length? ")) #sideLength parameter
    c = input("what is the color? ") #Color parameter
    d = int(input("What is the starting x coordinate? ")) #Starting x coordinate parameter
    e = int(input("What is the starting y coordinate? ")) #Starting y coordinate parameter
    f = input("What is your preference? (spread, zoom or slide) ") # Spread, Zoom or slide 

    gamma = turtle.Turtle() #Constructor     #creating a reference called gamma 

    if f == "spread":
        spread(a, gamma, 0, d, e, c, b)
    elif f == "zoom":
        zoom(a, gamma, 0, d, e, c, b)
    elif f == "slide":
        slide(a, gamma, 0, d, e, c, b)

main()
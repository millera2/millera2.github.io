"""
Purpose: Create shape patterns based on their input and how functional abstraction was used

How functional abstraction was used in this assignment:
By making a function for Squares and Triangles, this was an example of a functional abstraction because it's able to execute a shape without us having to understand how it was done. If the user inputs "Squares" as the shape, this function will run a loop to make the four sides of the square. If the user inputs "Triangles" as the shape, this function will run a loop to make the three sides of the triangle. It also makes it easier because you can have different inputs for the arguments passed (for x,y coordinates, length, and color) without manually repeating the whole chunk of code and entering new inputs inside the code. Instead, you can just call the function and enter your inputs or run the program if it has user input prompts. Essentially, it allows for easier modifiability, lowers risk of programming error, reduced clutter, and execte a function from a clear name. Based on the user input, functions can execute a spread of the user's shape from the right trigger words. From the if statements incorporated, it's able to return the desired shape movement. I was able to write some code and use it again in other places, such as the two shapes and three types of shape movements. Functional abstraction allows for there to be a square or triangle drawn from a single command and same with the type of movements and can be done repeatedly easily. 

Author: Julie Tran
Date: September 12, 2020
CS 111, Fall 2020
"""

import turtle                                                                ## Use turtle library

def drawSquare(tortise, x, y, length, heading, colorFill):                   ## Create function to draw squares passing arguments from user input
    """This function draws a square.
   
    Arguments: 
        tortise: is a turtle object
        x, y: are the lower-left coordinates of the square
        length: is the side length of the square
        heading: is the initial heading in degrees
        colorFill: is the color that will be filled inside the square
    
    Returns:
        None, but draws a square.
    """
    tortise.goto(x, y)                                                       ## Set starting place 
    tortise.fillcolor(colorFill)                                             ## Set the fill color inside the square; colorFill object
    tortise.begin_fill()                                                     ## Before square will be filled
    for i in range(4):                                                       ## Repeat four times for a square              
        tortise.forward(length)                                              ## Length object; distance tortise is headed
        tortise.left(90)                                                     ## Angle of square; 360/4
        tortise.heading()                                                    ## Return the turtle’s current heading
    tortise.end_fill()                                                       ## Fill the shape drawn after the last call
        

def drawTriangle(tortise, x, y, length, heading, colorFill):                 ## Create function to draw triangles passing arguments from user input
    """This function draws a triangle.
    
    Arguments: 
        tortise: is a turtle object
        x, y: are the lower-left coordinates of the triangle
        length: is the side length of the triangle
        heading: is the initial heading in degrees
        colorFill: is the color that will be filled inside the triangle
    
    Returns:
        None, but draws a triangle.
    """
    tortise.penup()                                                           ## No drawing when moving when setting starting place
    tortise.goto(x,y)                                                         ## Set starting place
    tortise.pendown()                                                         ## Drawing when moving
    tortise.fillcolor(colorFill)                                              ## Set the fill color inside the triangle; colorFill object
    tortise.begin_fill()                                                      ## Before triangle will be filled
    for i in range(3):                                                        ## Repeat three times for a triangle
        tortise.forward(length)                                               ## Length object; distance tortise is headed
        tortise.left(120)                                                     ## Angle of square; 360/4                   
        tortise.heading()                                                     ## Return the turtle’s current heading
    tortise.end_fill()                                                        ## Fill the shape drawn after the last call

def spread(tortise, x, y, length, heading, shape, colorFill):                 ## Create a function to make a spread with same arguments of shape
    """This function makes a “spread” of either squares or triangles, depending on user input. 
    
    Arguments:
        tortise: is a turtle object
        x, y: are the lower-left coordinates of the shape
        length: is the side length of the shape
        heading: is the initial heading in degrees
        colorFill: is the color that will be filled inside the shape
         
    Returns: 
        None, but spread the shapes.
    """
    for i in range(0, 75, 15):                                                ## Index starts at 0 and goes up to 75 by increments of 15
        if(shape == "Squares"):                                               ## Use if statement depending on user input from 2 shape choices 
            drawSquare(tortise, x, y, length, heading, colorFill)             ## Creates a square spread only if user enters so
        else:
            drawTriangle(tortise, x, y, length, heading, colorFill)           ## Otherwise, creates a triangle spread if user enters so
        tortise.setheading(15+i)                                              ## increases angle by 15 with each iteration for 5 spreads

def slide(tortise, x, y, length, heading, shape, colorFill):                  ## Create a function to make a slide with same arguments of shape
    """This function should make a "slide" of either shapes or triangles, depending on user input.
    
    Arguments:
        tortise: is a turtle object
        x, y: are the lower-left coordinates of the shape
        length: is the side length of the shape
        heading: is the initial heading in degrees
        colorFill: is the color that will be filled inside the shape
        
    Returns:
        None, but slide the shapes.
    """
    for i in range(5):                                                        ## Repeat for each slide; 5 slides evident 
        if(shape == "Triangles"):                                             ## Use if statement depending on user input from 2 shape choices
            drawTriangle(tortise, x, y, length, heading, colorFill)           ## Creates a triangle spread if user enters so
        else:                                                                  
            drawSquare(tortise, x, y, length, heading, colorFill)             ## Otherwise, creates a square spread only if user enters so
        x += 10                                                               ## Increment x to right by 10 each time iterates 5 times 

def zoom(tortise, x, y, length, heading, shape, colorFill):                   ## Create a function to make a zoom with same arguments of shape       
    """This function should make a "zoom" of either squares or triangles, depending on user input.
    
    Arguments:
        Arguments:
        tortise: is a turtle object
        x, y: are the lower-left coordinates of the shape
        length: is the side length of the shape
        heading: is the initial heading in degrees
        colorFill: is the color that will be filled inside the shape
        
    Returns:
        None, but zoom the shapes.
    """
    scale = length/4                                                          ## Create reference variable for a fourth of original length
    for i in range(4):                                                        ## Use if statement depending on user input from 2 shape choices
        if(shape == "Triangles"):
            drawTriangle(tortise, x, y, length, heading, colorFill)           ## Creates a triangle spread if user enters so
        else:
            drawSquare(tortise, x, y, length, heading, colorFill)             ## Otherwise, creates a square spread only if user enters so
        tortise.penup()                                                       ## Don't draw before shifting x
        x += scale/2                                                          ## Shifts shape evenly to the right                                       
        tortise.setpos(x, y)                                                  ## Move turtle position
        tortise.pendown()                                                     ## Draw after shifting x
        length -= scale                                                       ## Make line shorter each time

def main():                                                                   ## Create a function for defining and execution of new objects 
    """Draws either Squares or Triangles from user input, with a specified length, x, y coordinates, color, and shape movement of choosing. 
    """
    tortise = turtle.Turtle()                                                                  ## Create turtle object 
    length = int(input("Please enter a side length:"))                                         ## Create length object; turn user input to integer
    x = int(input("Please enter a x coordinate:"))                                             ## Create x coord object; turn user input to integer
    y = int(input("Please enter a y coordinate:"))                                             ## Create y coord object; turn user input to integer
    colorFill = input("Please enter the color string you want for your shape (ex. red):")      ## Create shapes color fill object based on user input
    heading = tortise.heading()                                                                ## Create heading object for argument 
    shape = input("Please enter 'Squares' or 'Triangles':")                                    ## Create shape object for user input
    movement = input("Please enter if you want the shape to 'Spread', 'Zoom', or 'Slide':")    ## Create movement object for user input
    if(shape == "Squares"):                                                  ## If statement to identify which movement to run for squares
        if(movement == 'Spread'):
            spread(tortise, x, y, length, heading, shape, colorFill)
        elif(movement == 'Zoom'):
            zoom(tortise, x, y, length, heading, shape, colorFill)
        elif(movement == 'Slide'):
            slide(tortise, x, y, length, heading, shape, colorFill)
        else:
            print("Please make sure you are typing in a correct Movement with the right format.")
    elif(shape == "Triangles"):                                              ## If statement to identify which movement to run for triangles
        if(movement == 'Spread'):
            spread(tortise, x, y, length, heading, shape, colorFill)
        elif(movement == 'Zoom'):
            zoom(tortise, x, y, length, heading, shape, colorFill)
        elif(movement == 'Slide'):
            slide(tortise, x, y, length, heading, shape, colorFill)
        else:
            print("Please make sure you are typing in a correct Movement with the right format.")
    else:
        print("Please make sure you are typing in a correct Shape with the right format.")
    turtle.done()                                                             ## Last statement in a turtle graphics program

main()                                                                        ## Call main function


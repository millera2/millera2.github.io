'''
Author: Duc Doan
Date: September 25th 2020
Class: CS111-03 

Docstrings questions:

In this program, I use 6 functional abstractions: drawSquare, drawTriangle, drawCircle, spread, zoom, and slide.
When asking the user to choose the shape they want to draw, I simply call back and run the drawSquare(), drawTriangle(), and drawCircle function.
When asking the user to choose the effect applied to the chosen shape, I call and run the zoom(), spread(), and slide() function to excecute according to the user's command.

In my following code, I have used the functional concept by calling back the function when ever the user want me to do. And of course with different shapes and sizes (almost no default values cause I want the user to freely do whatever he/she like), different effects also.

The main reason why we talk a lot about functional abstraction is because of it's applicable and useful. Let's say that if someone want to use my code, he does not have to really understand everything that happens in my code. He can just simply import to my code then call the function (definitely with parameters if required)

'''

import turtle

def drawSquare(tortoise, length,fcolor):
    '''Draw a Square
    Parameters: 
        tortoise: a Turtle object to draw a square
        length : the length of each side of the square
        fcolor: the color of the square
    Return value:
        None
    '''
    tortoise.fillcolor(fcolor)
    tortoise.begin_fill()
    for e in range(4):
        tortoise.forward(length)
        tortoise.left(90)
    tortoise.end_fill()

def drawTriangle(tortoise,length,fcolor):
    '''Draw a Triangle
    Parameters: 
        tortoise: a Turtle object to draw a triangle
        length : the length of each side of the triangle
        fcolor: the color of the triangle
    Return value:
        None
    '''
    tortoise.fillcolor(fcolor)
    tortoise.begin_fill()
    for a in range(3):
        tortoise.forward(length)
        tortoise.left(120)
    tortoise.end_fill()

def drawCircle(tortoise,radius,fcolor):
    '''Draw a Circle
    Parameters: 
        tortoise: a Turtle object to draw a triangle
        radius : the radius of the circle
        fcolor : the color of the circle
    Return value:
        None
    '''
    tortoise.fillcolor(fcolor)
    tortoise.begin_fill()
    tortoise.circle(radius)
    tortoise.end_fill()

def spread(tortoise):
    '''Create an effect called spread. This simply turn the Turtle 5 times, each time with 18 degree, then draw another choosen shape.
    Parameters: 
        tortoise: a Turtle object to execute this effect
    Return value:
        None
    '''
    tortoise.left(18)


def zoom(tortoise , shape, zoom_length, fcolor, distance):
    '''Create an effect called zoom. Zoom effect allows the original choosen shape to zoom in and draw another same shape but with smaller sides.
    Parameters: 
        tortoise: a Turtle object to execute this effect
        shape: the choosen shape
        zoom_length: how much the shape gonna zoom in
        fcolor: the color of the shape
    Return value:
        None
    '''
    if shape.upper() == 'SQUARE':
        for i in range(4):
            drawSquare(tortoise,zoom_length,fcolor)
            tortoise.forward(distance)         #the turtle go forward before drawing another circle (acutually zooming in)
            zoom_length -= 2*distance

    elif shape.upper() == 'TRIANGLE':
        for i in range(4):
            drawTriangle(tortoise,zoom_length,fcolor)
            tortoise.forward(distance)         #the turtle go forward before drawing another circle (acutually zooming in)
            zoom_length -= 2*distance

    elif shape.upper() == 'CIRCLE':
        
        tortoise.penup()
        for i in range(zoom_length, zoom_length-4*distance, -distance):
            tortoise.right(90)       
            tortoise.forward(i)    #from the center of the circle go forward with a distance = to the radius
            tortoise.right(270)    # turn 270 degree basically makes the turtle heading to the original position to actually draw a circle later
            tortoise.pendown()
            drawCircle(tortoise,i,fcolor)    #draw a Circle with radius i and color: fcolor
            tortoise.penup()
            tortoise.home()      #This is a cool method which allows the turtle go back to the center of a circle(you might notice that when you try!). Then due to the for loop , it can draw another smaller circle 



def slide(tortoise,distance=20):
    '''Create an effect called slide. This simply move Turtle to the right after drawing the 1st shape, then draw another choosen shape. 
    Parameters: 
        tortoise: a Turtle object to execute this effect
    Return value:
        None
    '''
    tortoise.forward(distance)

def main():
    '''Draw a shape based on the user's preference. Then excute the effect also based on the user's preference.

    '''
    bob = turtle.Turtle()
    jelly = turtle.Turtle()
    andy = turtle.Turtle()
   
    Switch = True  #just like a real switch to turn on and off
    
    while Switch:    #Here I start a big while loop to keep the program running until user don't want to use anymore
        
        switch = True    #just like a real switch to turn on and off
        while switch:    #turn on the switch a start a while loop to force the user type in the right commands before going ahead.
            ask = input("Hey! Which one you want me to draw 'square,triangle,or circle?': ")
            if ask.upper() == 'SQUARE':
                switch = False
            elif ask.upper() == 'TRIANGLE':
                switch = False
            elif ask.upper() == 'CIRCLE':
                switch = False
        else:
                switch = True
                
        ask4= input("Choose a color for your shape 'only in CSS color please!': ")
        
        ask2= int(input('Choose your side_length, or radius: '))

        switch = True
        while switch:       #turn on the switch a start a while loop to force the user type in the right commands before going ahead
            ask3 = input("Which effect 'spread, zoom , or slide?' ")
            if ask3.upper() == 'ZOOM':
                ask5 = int(input("How much you wanna zoom in? 'Warning: If you zoom in too much weird things will happen!!!':  "))
                switch = False
            elif ask3.upper() == 'SPREAD':
                switch = False
            elif ask3.upper() == 'SLIDE':
                switch = False
            else:
                switch = True

        x = int(input('Choose your x-coordinate to start drawing: '))
        y = int(input('Choose yout y-coordinate to start drawing: '))

        bob.speed(2)     #setup a speed for bob and jelly (they draw squares and triangles)
        jelly.speed(2)
        
        bob.penup()      #to actually pick up a pen and stop drawing
        bob.goto(x,y)    #turtle goes to a specific position 
        bob.pendown()    #put down the pen an continue drawing

        jelly.penup()
        jelly.goto(x,y)
        jelly.pendown()

        andy.penup()
        andy.goto(x,y)
        andy.pendown()

        if ask.upper() == 'SQUARE' and ask3.upper() == 'SPREAD':
            jelly.hideturtle()      #hide the turtles because it's not neccesary to be here
            andy.hideturtle()
            for time in range(5):
                drawSquare(bob,ask2,ask4)
                spread(bob)

        elif ask.upper() == "TRIANGLE" and ask3.upper() == 'SPREAD':
            bob.hideturtle()      #hide the turtles because it's not neccesary to be here
            andy.hideturtle()
            for time in range(5):
                drawTriangle(jelly,ask2,ask4)
                spread(jelly)

        elif ask.upper() == "CIRCLE" and ask3.upper() == 'SPREAD':
            bob.hideturtle()      #hide the turtles because it's not neccesary to be here
            jelly.hideturtle()
            for time in range(5):
                drawCircle(andy,ask2,ask4)
                spread(andy)

        if ask.upper() == 'SQUARE'and ask3.upper() == 'ZOOM':
            jelly.hideturtle()    #hide the turtles because it's not neccesary to be here
            andy.hideturtle()
            zoom(bob,'SQUARE',ask2,ask4,ask5)

        elif ask.upper() == 'TRIANGLE'and ask3.upper() == 'ZOOM':
            bob.hideturtle()     #hide the turtles because it's not neccesary to be here
            andy.hideturtle()
            zoom(jelly,'TRIANGLE',ask2,ask4,ask5)

        elif ask.upper() == 'CIRCLE'and ask3.upper() == 'ZOOM':
            jelly.hideturtle()    #hide the turtles because it's not neccesary to be here
            bob.hideturtle()
            zoom(andy,'CIRCLE',ask2,ask4,ask5)

        if ask.upper() == 'SQUARE' and ask3.upper() == 'SLIDE':
            jelly.hideturtle()    #hide the turtles because it's not neccesary to be here
            andy.hideturtle()
            for time in range(5):
                drawSquare(bob,ask2,ask4)
                slide(bob)
                
        elif ask.upper() == 'TRIANGLE' and ask3.upper() == 'SLIDE':
            bob.hideturtle()     #hide the turtles because it's not neccesary to be here
            andy.hideturtle()
            for time in range(5):
                drawTriangle(jelly,ask2,ask4)
                slide(jelly)
        elif ask.upper() == 'CIRCLE' and ask3.upper() =='SLIDE':
            bob.hideturtle()     #hide the turtles because it's not neccesary to be here
            jelly.hideturtle()
            for time in range(5):
                drawCircle(andy,ask2,ask4)
                slide(andy)
        switch = True
        while switch:     #turn on the switch a start a while loop to force the user type in the right commands before going ahead. And here, I just want to ask the user whether he/she wants to continue drawing anything!
            ask5 = input("Wait don't close the window yet! Still want to draw anything 'yes or no?' ")

            if ask5.upper() == 'YES':
                switch = False
            elif ask5.upper() == 'NO':
                switch = False
                Switch = False
                print('Thank you for trying my chunk of code :)))) ')
            else:
                pass
        
        turtle.clearscreen()     #clear the entire screen both the drawings and the turtles
        bob = turtle.Turtle()    # have to call them again to use (if the user likes) since I've deleted all the screen
        jelly = turtle.Turtle()
        andy = turtle.Turtle()

main()     
turtle.bye()    #Automatically close the Turtle window (only after the user don't want to play around anymore).

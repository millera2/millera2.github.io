## Question 1 Making a square
import turtle

tortise= turtle.Turtle()

length= input("Enter the length of the side of the square: ")    ## inputs for all the different variables
fill_col= input("Enter color name red:")
pen_col= input("Enter pen color blue:")
heading= input("Enter Initial heading:")
tortise.color(pen_col,fill_col)
tortise.begin_fill() 

def drawSquare(tortise, heading, x, y, length):
    tortise.goto(x,y)
    for i in range(4):         ## for loop which will create the square 
        tortise.forward(length)
        tortise.left(90)
tortise.end_fill()       
drawSquare(tortise, 40, 50, 100, 100)


## struggling to do the fillcolor function as it changes the color of the icon but not the actual shape, might be that my computer is not able to run it

## Question 2 Drawing a Triangle

import turtle
tortise= turtle.Turtle()

length= input("Enter the length of the side of the square: ")    ## inputs for all the different variables
fill_col= input("Enter color name red:")
pen_col= input("Enter pen color blue:")
heading= input("Enter Initial heading:")
tortise.color(pen_col,fill_col)

tortise.begin_fill() 
def drawTriangle(tortise, heading, x, y, length):       ## creating the for loop/ def for the triangle
    tortise.goto(x,y)
    for i in range(3):          ## range of 3 and angle of 120 for triangles 
        tortise.forward(length)
        tortise.left(120)
tortise.end_fill()       
drawTriangle(tortise, 170, -40, -20, 100)


## Creating a zoom of squares
import turtle
tortise = turtle.Turtle()

fill_col= input("Enter color name red:")   ## inputs for all the different variables
pen_col= input("Enter pen color blue:")
tortise.color(pen_col,fill_col)

tortise.begin_fill() 
def drawSquares(tortise,length, x, y, nSquares, distanceApart):
    if nSquares > 0:
        tortise.pu()
        tortise.setx(x)
        tortise.sety(y)
        tortise.pd()
        for i in range(4):
            tortise.forward(length)
            tortise.right(90)
        drawSquares(tortise, length - distanceApart*2, x+10, y-10, nSquares-1, distanceApart)  ## lengths of the sides are reduced each time from length-distance*2
tortise.end_fill()
drawSquares(tortise, 200, 60, 60, 4, 10)
 
    
## Question 4 main() function

import turtle 
tortise=turtle.Turtle

shape=input("Enter the shape (drawTriangles or drawSquares):")  ## inputs for all the different variables 
length=input("Enter the side length:")
pen_col=input("Enter the pen color:")
fill_col=input("Enter the fillcolor:")
x= input("Enter x-coordinate")
y=input("Enter y-coordinate")

tortise.color(pen_col,fill_col)
tortise.begin_fill()

def shape(tortise, length, x, y, nSquares, distanceApart):
    """
    Functional abstraction is used throughout this homework as it is defined by is how we 
    re-use our old solutions so that we can make something new ones. When I was doing this assignment
    I found that majority of times I was copying and pasting my previous code and altering it to fit
    what the question was asking. For example with the first two problems I just copied my code from the first problem 
    and changed the numeric values and wording. Functional abstraction is so important to computer scientists as it saves them
    alot of time as you do not want to constantly be righting things which we could simply copy from a previous question. 
    """
    if nSquares > 0:
        tortise.pu()
        tortise.setx(x)
        tortise.sety(y)
        tortise.pd()
        for i in range(4):
            tortise.forward(length)
            tortise.right(90)
            def main():
                print("python main function")  ## confused on how to use this function 
                if __name__ == '__main__':
                    main()
        drawSquares(tortise, length - distanceApart*2, x+10, y-10, nSquares-1, distanceApart)
tortise.end_fill()
       
drawSquares(tortise, length, x, y, nSquares, distanceApart)   



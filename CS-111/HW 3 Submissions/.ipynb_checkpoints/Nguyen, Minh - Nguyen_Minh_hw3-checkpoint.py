"""
1.It can be considered that there are two levels of functional abstraction. -	When using the functions of
“turtle” library, we are using “black-boxes” which create the graphic windows and movements that appear on our screen.
We don’t know exactly how such functions like setheading(), setposition() or turtle’s objects are implemented  but we
can use the compact representation to play with graphics. -	In the slide, zoom and spread functions,
I called makeSquare() and makeTriangle() to not have to implement the whole process of drawing a square or a triangle
again and also to make my code more compact and easier for other people to read

2.	Based on my learning, literally everything we are using right now is the product of layers of functional
abstractions. Turtle is just one of millions of APIs and libraries out there. The Windows operating system that I am
currently using contains huge number of layers of functional abstraction. Even one of the most simple arithmetic
operations, the addition, is built on extremely clever idea of two-stack algorithm and the “stack” data type itself
is another function abstraction. Function abstraction makes it a lot easier for users to use highly complicated tasks
and also to understand from top to bottom a program. For example, when I implement slide(), I call makeTriangle()
instead of writing a for loop and adding a comment which explains that for loop is for drawing a triangle. In this way,
a reader will understand my code much quicker, get rid of unnecessary details to focus on more complicated logic. If
at sometimes I need to draw a pool of turtles, all what I need is import the drawTurtle() and fit it into, might be,
drawPool(). """
import turtle
import math


def makeSquare(tortoise, heading=0, x=0, y=0, length=100, fillColor="black"):
    """ Draw a square in counter-clockwise direction
    :param tortoise: turtle object
    :param heading: the direction that you want your tortoise to head to (default 0)
    :param x: starting x-position (default 0)
    :param y: starting y-position (default 0)
    :param length: length of shape's side (default 100)
    :param fillColor: color of the shape (default "black")
    """
    tortoise.setposition(x, y)
    tortoise.setheading(heading)
    tortoise.begin_fill()
    tortoise.fillcolor(fillColor)
    for i in range(4):
        tortoise.forward(length)
        tortoise.left(90)
    tortoise.end_fill()


def makeTriangle(tortoise, heading=0, x=0, y=0, length=100, fillColor="black"):
    """ Draw a triangle in counter-clockwise direction
    :param tortoise: turtle object
    :param heading: the direction that you want your tortoise to head to (default 0)
    :param x: starting x-position (default 0)
    :param y: starting y-position (default 0)
    :param length: length of shape's side (default 100)
    :param fillColor: color of the shape (default "black")
    """
    tortoise.setposition(x, y)
    tortoise.setheading(heading)
    tortoise.begin_fill()
    tortoise.fillcolor(fillColor)
    for i in range(3):
        tortoise.forward(length)
        tortoise.left(120)
    tortoise.end_fill()


def spread(tortoise, heading, x, y, length, fillColor, numSlide, shape, angledif, direction):
    """ Draw a series of identical shapes which have in common starting point and each rotate by a constant degree from
    its adjacent to create the "spread" effect
    :param tortoise: turtle object
    :param heading: the direction that you want your tortoise to head to
    :param x: starting x-position
    :param y: starting y-position
    :param length: length of shape's side
    :param fillColor: color of the shape
    :param numSlide: number of slides
    :param shape: type of shape
    :param angledif: how much each slides rotate more than its previous one
    :param direction: spread in clockwise or counter-clockwise direction
    """
    if shape == "s":  # test if shape is square
        if direction == "y":  # test if user wants to draw clockwise
            for i in range(numSlide):
                # change "heading" to rotate the next slide
                makeSquare(tortoise, heading + - i * angledif, x, y, length, fillColor)
        else:
            for i in range(numSlide):
                makeSquare(tortoise, heading + i * angledif, x, y, length, fillColor)
    else:
        if direction == "y":
            for i in range(numSlide):
                makeTriangle(tortoise, heading - i * angledif, x, y, length, fillColor)
        else:
            for i in range(numSlide):
                makeTriangle(tortoise, heading + i * angledif, x, y, length, fillColor)


def zoom(tortoise, x, y, length, shape, fillColor, numZoom, distance, direction):
    """
    Draw a series of shapes in which the smaller shapes lies inside the bigger ones
    :param tortoise: turtle object
    :param x: starting x-position
    :param y: starting y-position
    :param length: length of the initial shape's side
    :param shape: type of shape
    :param fillColor: color of the shape
    :param numZoom: number of zoom
    :param distance: the distance turtle zooms each time
    :param direction: zoom in or out
    """
    if shape == "t":  # test if shape is triangle
        if direction == "o":  # if user chooses zoom out, calculate the outer lines, move starting point to draw it
            # and then zoom in
            x -= distance * numZoom
            length += distance * numZoom * 2
        if length / 2 - numZoom * distance <= 0:  # test if there is enough room to zoom in with given numSlide and
            # distance
            print("There is not enough room to zoom in, please provide bigger initial side length ")
        else:
            makeTriangle(tortoise, 0, x, y, length, fillColor)
            for i in range(numZoom):  # "zoom in" part
                x += distance
                length -= distance * 2
                tortoise.penup()
                tortoise.goto(x, y)
                for i1 in range(3):
                    tortoise.forward(length)
                    tortoise.left(120)
    else:  # shape is square
        if direction == "o":
            x -= distance * numZoom
            length += distance * numZoom * 2
        if length / 2 - numZoom * distance <= 0:
            print("There is not enough room to zoom in, please provide bigger initial side length ")
        else:
            makeSquare(tortoise, 0, x, y, length, fillColor)
            for i in range(numZoom):
                x += distance
                y += distance
                length -= distance * 2
                tortoise.penup()
                tortoise.goto(x, y)
                tortoise.pendown()
                for i1 in range(4):
                    tortoise.forward(length)
                    tortoise.left(90)


def slide(tortoise, heading, x, y, length, fillColor, numSlide, shape, distance):
    """
    Draw a series of identical shapes in which each shape has a side lies on the heading line.
    Each two adjacent shapes is separated by a constant distance to create the "slide" effect.
    :param tortoise: turtle object
    :param heading: the direction that you want your tortoise to head to
    :param x: starting x-position
    :param y: starting y-position
    :param length: length of the initial shape's side
    :param fillColor: color of the shape
    :param numSlide: number of slides
    :param shape: type of shape
    :param distance: distance between two adjacent slides
    """
    if shape == "s":  # test if shape is square
        for i in range(numSlide):
            makeSquare(tortoise, heading, x, y, length, fillColor)
            x += distance * math.cos(math.radians(heading))  # update the starting point to draw next slides
            y += distance * math.sin(math.radians(heading))
    else:
        for i in range(numSlide):
            makeTriangle(tortoise, heading, x, y, length, fillColor)
            x += distance * math.cos(math.radians(heading))
            y += distance * math.sin(math.radians(heading))


def drawTurtle(size=350, fillcolor="lightgreen"):
    """ Draw a turtle in the middle of the screen with given size and color
    :param fillcolor: color of the turtle
    :param size: the shape of this turtle lies inside a size x size square
    """
    length = size / (1.5 + 6 * math.sin(math.radians(60)))
    bob = turtle.Turtle()
    bob.speed(10)
    bob.penup()
    bob.goto(0, 4 * math.sin(math.radians(60)) * length)
    bob.pendown()
    bob.begin_fill()
    bob.fillcolor(fillcolor)
    for i in range(6):
        if i != 3:
            bob.left(90)
            bob.forward(length * 1.5)
            bob.right(90)
            bob.forward(length)
            bob.right(90)
            bob.forward(length * 1.5)
            bob.left(90)
        else:
            bob.forward(length)
        bob.right(30)
        bob.forward(math.sin(math.radians(60)) * 2 * length)
        bob.right(30)
    bob.end_fill()
    bob.penup()
    bob.goto(0, 0)
    bob.pendown()
    for i in range(6):
        for i1 in range(6):
            bob.forward(length)
            bob.right(60)
        bob.left(120)
        bob.forward(length)
        bob.left(180)


def main():
    shape = input("Type 'T' for Triangle or 'S' for Square: ").lower()
    length = int(input("Type the length of the sides: "))
    fillColor = input("Type the name of the color: ").lower()
    x, y = [int(i) for i in input("Type the starting coordinates, separated by ',': ").split(",")]
    funcType = input("Type the function that you want to use: Spread, Zoom or Slide? ").lower()
    if funcType == "spread":
        heading = int(input("Type the direction that you want to start (0-360): "))
        angelDif = int(input("How much do you want each slide to rotate more than its previous one (in degree) "))
        direction = input("Do you want to rotate in clockwise direction? Y/N ")
        numSlide = int(input("Type the number of slides you want to spread: "))
        bob = turtle.Turtle()
        spread(bob, heading, x, y, length, fillColor, numSlide, shape, angelDif, direction)
    elif funcType == "zoom":
        bob = turtle.Turtle()
        direction = input("Do you want to zoom in or out (I/O) ").lower()
        distance = int(input("What is the distance you want to zoom each time turtle zooms: "))
        numZoom = int(input("How many times you want to zoom? "))
        zoom(bob, x, y, length, shape, fillColor, numZoom, distance, direction)
    elif funcType == "slide":
        heading = int(input("Type the direction that you want go (0-360): "))
        distance = int(input("Type the distance between two adjacent slides:  "))
        numSlide = int(input("Type how many slides do you want: "))
        bob = turtle.Turtle()
        slide(bob, heading, x, y, length, fillColor, numSlide, shape, distance)
    else:
        print("Function not detected")
    check = turtle.textinput("WOW!", "We have been working with 'turtle' the whole time but there is no real tortoise "
                                     "at all. Do you want to see one? (Y/N) ").lower()
    if check == "y":
        turtle.clearscreen()
        drawTurtle()
    else:
        turtle.done()
    turtle.done()
    # bob = turtle.Turtle()
    # drawTurtle()
    # turtle.done()
    # zoom(bob,0,0,300,"s","red",5,20,"i")


main()

import turtle
import random as r
ann = turtle.Turtle()
ann.ht()
bob = turtle.Turtle()
bob.ht()
curtis = turtle.Turtle()
curtis.ht()
random_color = (r.uniform(0,1),r.uniform(0,1),r.uniform(0,1))

#makeSquare
def makesquare(tortise = ann, heading = 0, x = 0, y = 0, length = 100, fillColor = random_color): # function for drawing a square
    tortise.st()
    tortise.seth(heading)           # set initial heading in degrees
    tortise.goto(x,y)               # set the starting point
    tortise.fillcolor(fillColor)    # set the color that will be filled in the square
    tortise.begin_fill()
    for square_index in range(4):   # repeat 4 times
        tortise.fd(length)
        tortise.lt(90)
    tortise.end_fill()
    tortise.ht()

#makeTriangle
def maketriangle(tortise = ann, heading = 0, x = 0, y = 0, length = 100, fillColor = random_color): # function for drawing a triangle
    tortise.st()
    tortise.seth(heading)           # set initial heading in degrees
    tortise.goto(x,y)               # set the starting point
    tortise.fillcolor(fillColor)
    tortise.begin_fill()
    for triangle_index in range(3):
        tortise.fd(length)
        tortise.lt(120)
    tortise.end_fill()
    tortise.ht()

#spread
def spread(shape, tortise = ann, heading = 0, x = 0, y = 0, side_length = 100, fill_color = random_color, repeat_times = 5):
    tortise.fillcolor(fill_color)
    tortise.st()
    if shape == 'square' :
        for angle in range(repeat_times):
            tortise.seth(25 * angle)
            tortise.begin_fill()
            for square_index in range(4):
                tortise.fd(side_length)
                tortise.lt(90)
            tortise.end_fill()
    elif shape == 'triangle':
        for angle in range(repeat_times):
            tortise.seth(25 * angle)
            tortise.begin_fill()
            for triangle_index in range(3):
                tortise.fd(side_length)
                tortise.lt(120)
            tortise.end_fill()
    else:
        print('Oops, no corresponding shape yet :(')
    tortise.ht()

#zoom
def zoom(shape, tortise = ann, z_side_length = 400, fill_color = random_color, repeat_times = 5):
    tortise.st()
    tortise.fillcolor(fill_color)
    if shape == 'square' :
        for square_index in range(repeat_times):
            z_square_index = 4
            tortise.begin_fill()
            while z_square_index > 0:
                tortise.fd(z_side_length)
                tortise.lt(90)
                z_square_index = z_square_index - 1
            tortise.fd(20)
            z_side_length = z_side_length - 40
            tortise.end_fill()
    elif shape == 'triangle':
        for triangle_index in range(repeat_times):
            z_triangle_index = 3
            tortise.begin_fill()
            while z_triangle_index > 0:
                tortise.fd(z_side_length)
                tortise.lt(120)
                z_triangle_index = z_triangle_index - 1
            tortise.fd(20)
            z_side_length = z_side_length - 40
            tortise.end_fill()
    else:
        print('Oops, no corresponding shape yet :(')
    tortise.ht()

#slide
def slide(shape, tortise = ann, s_side_length = 200, fill_color = random_color, repeat_times = 5):
    tortise.st()
    tortise.fillcolor(fill_color)
    if shape == 'square' :
        for s_square_index in range(repeat_times):
            tortise.begin_fill()
            for square_index in range(4):
                tortise.fd(s_side_length)
                tortise.lt(90)
            tortise.end_fill()
            if s_square_index == repeat_times - 1:
                break
            else:
                tortise.fd(20)
    elif shape == 'triangle':
        for s_triangle_index in range(repeat_times):
            tortise.begin_fill()
            for triangle_index in range(3):
                tortise.fd(s_side_length)
                tortise.lt(120)
            tortise.end_fill()
            if s_triangle_index == repeat_times - 1:
                break
            else:
                tortise.fd(20)
    else:
        print('Oops, not corresponding shape yet :(')
    tortise.ht()

#main
def main():

    shape = input('Please enter the shape of the graphic:')
    if shape != 'square' and 'triangle' :
        print('Oops, no corresponding shape yet :(')
        return None
    else:
        pass
    side_length = int(input('Please enter the side length of the graphic:'))
    fill_color = input('Please enter the fill color of the graphic:')
    starting_coordinate = input('Please enter the starting coordinate (do not enter brackets):')
    coordinate = starting_coordinate.split(',')
    mode = input('Please enter the name of the function you would like to run:')
    if mode == 'makesquare':
        makesquare(shape, side_length, fill_color,int(coordinate[0]),int(coordinate[1]))
    

    else:
        pass
    turtle.done()

''' 1. In this assignment, I use some turtle functions. Using turtle functions can be roughly seen as
functional abstraction because we may not know how computer process these functions. I use codes to command turtles
to draw graphics, and I know how the results may look like. But I do not know how these functions works in the computer.
    2. We keep talking about it because we use functions very frequent. By using these functions, we can solve problems
    easier without spending much time to learn about it.'''

#extra
def spin(length = 200, tortise = ann):
    for spin_times in range(5):
        squareindex = 4
        tortise.begin_fill()
        while squareindex > 0:
            tortise.fd(length)
            tortise.lt(90)
            squareindex = squareindex - 1
        bob.end_fill()
        if spin_times == 4:
            break
        else:
            tortise.penup()
            tortise.rt(35)
            tortise.fd(0.246 * length) # the graphic spins
            tortise.lt(55)
            tortise.pendown()



main()
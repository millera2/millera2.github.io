import turtle

tortoise = turtle.Turtle()

shape = input("Are you drawing squares or triangles? ")
headingAng = int(input("enter heading angle: "))
x = int(input("enter x coordinates for lower-left point: "))
y = int(input("enter y coordinates for lower-left point: "))
length = int(input("enter side length: "))
design = str(input("Spread, zoom, or slide shape? "))
fillColor = str(input("enter color of shape: "))


""""Abstraction was implemented in this program to reduce the complexity of the code and it allows for the functions that were created to easily be looped or reused. For example, the makeSquare function is an abstraction because it uses a loop to simplify drawing each side and fill the color rather than writing it multiple times."""


def makeSquare(tortoise, headingAng, x, y, fillColor, shape, length):         #draws a square
    tortoise.penup()  #pen up so it doesnt draw a line to the coordinates being input   
    tortoise.setheading(headingAng)
    tortoise.goto(x,y)
    tortoise.fillcolor(fillColor)
    tortoise.begin_fill(fillColor)
    tortoise.pendown()
    for i in range(4):   
      tortoise.forward(length)
      tortoise.right(90)
      tortoise.end_fill(fillColor)
            
def makeTriangle(tortoise, headingAng, x, y, fillColor, shape, length):           # draws a triangle
    tortoise.penup()
    tortoise.fillcolor(fillColor)
    tortoise.begin_fill(fillColor)
    tortoise.pendown()
    for i2 in range(3):
      tortoise.right(60)
      tortoise.forward(length)
      tortoise.end_fill(fillColor)
        

def spread():       #draws shapes to turn at different angles
        tortoise.goto(x,y)
        tortoise.setheading(headingAng+15)
        if shape == "squares":
          for spr in range(6):
            makeSquare(tortoise, headingAng, x, y, fillColor, shape, length)
        elif shape == "triangles":
          for spr in range(6):
            makeTriangle(tortoise, headingAng, x, y, fillColor, shape, length)

    
def zoom():    #draws multiple of the same shape shape decreasing in size
  tortoise.goto(x,y)
  if shape == "squares":
    for zo in range(5):
      makeSquare(tortoise, shape, headingAng, x, y, fillColor, length*0.80)
  elif shape == "triangles":
    for zo in range(5):
      makeTriangle(tortoise, headingAng, x, y, fillColor, shape, length*0.8)

def slide():  #draws multiple of the same shape in front of each other
  tortoise.goto(x,y)
  if shape == "squares":
    for sl in range(5):
      makeSquare(tortoise, shape, headingAng, x+20, y, fillColor, length)
  elif shape == "triangles":
    makeTriangle(tortoise, headingAng, x+20, y, fillColor, shape, length)


if design == "spread":     #makes sure inputs run the correct function
  spread()
elif design == "zoom":
  zoom()
elif design == "slide":
  slide()

screen = tortoise.getscreen()
screen.exitonclick()
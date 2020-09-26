{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## HomeWORK 3"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Functional abstraction provides methods to do some work while hiding details of how this is done. this exercise is all about functional abstraction becuase we had to work on how all the differnt small and Minute details are needed to be successfuly used when it comes to seeing an image created before you. Abstraction is the process of filtering out – ignoring - the characteristics of patterns that we don't need in order to concentrate on those that we do. It is also the filtering out of specific details. By filtering out the different characteristics of patterns we dont need we are able to understand the ideas easier."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"Draws squares with turtle\n",
    "\"\"\"\n",
    "\n",
    "def makeSquare(Tortoise, x, y, SideLength = 100):\n",
    "    Tortoise.goto(x,y)\n",
    "    for i in range(4):\n",
    "        Tortoise.forward(sideLength)\n",
    "        Tortoise.left(90)\n",
    "\n",
    "def main():\n",
    "    bob = tortoise.Tortoise()                  #making a new turtle with Turtle() consturctor\n",
    "\n",
    "    jill = tortoise.Tortoise()                  #making a second turtle\n",
    "    defaultSideLength = 100                 # if user doesnt specify, sidelength is this!\n",
    "    makeSquare(jill, -50 ,100)\n",
    "    makeSquare(bob, 70, -70, 200)\n",
    "    makeSquare(jill, 100, 200, 40)\n",
    "    makeSquare(bob, -50, -100, 300)\n",
    "    Turtle.done()\n",
    "\n",
    "# myTurtle is the turtle object passed to the function. must make sure to know what is being defined\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# this section helps me gage on how to get a square will color filled inside of it!\n",
    "\n",
    "from turtle import *\n",
    "color('blue', 'green',)\n",
    "begin_fill()\n",
    "for i in range(4):\n",
    "    forward(100)\n",
    "    left(90)\n",
    "end_fill()\n",
    "done()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# in this funciton I was able to ge the squares to spread, but i wanted to make them into a spiral like formation for a spread because I thought it would look more fun.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "from turtle import *      # this funciton is my interpertation of the Spread while loop. It has similar properties of the spread\n",
    "color('blue','yellow')\n",
    "def makeSquare(sidelength):  \n",
    "    begin_fill()\n",
    "    for i in range(4): \n",
    "        forward(sidelength) \n",
    "        left(90)\n",
    "    end_fill()\n",
    "\n",
    "\n",
    "makeTurtle = ()\n",
    "hideTurtle = ()\n",
    "\n",
    "i = 0\n",
    "while True:\n",
    "    if i > 120:\n",
    "        break\n",
    "    square(i)\n",
    "    right(6)\n",
    "    i += 2              # the part i is incremented by 2\n",
    "print(i)\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# this funtion is here to show the slide function I could get different triangles into different sections and slide from each other, but they seemed to make a cool shape that I enjoyed with the center a specific color of your choice!\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-1-e0e82e0fef13>, line 2)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-1-e0e82e0fef13>\"\u001b[0;36m, line \u001b[0;32m2\u001b[0m\n\u001b[0;31m    def slide:\u001b[0m\n\u001b[0m             ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "\n",
    "from turtle import *\n",
    "\n",
    "makeTurtle = ()\n",
    "setPos = (-200, 30)\n",
    "right = (30)\n",
    "fillToHorizontal = (0)\n",
    "setPenColor = (\"red\")\n",
    "color('purple','blue')    # the specific color you can change and put in!\n",
    "nr = 1\n",
    "while nr <= 10:\n",
    "    begin_fill()\n",
    "    if nr > 3 and nr < 8:\n",
    "        forward(100)\n",
    "        left(120)\n",
    "        forward(100)\n",
    "        left(120)\n",
    "        for i in range(3):    # the second start of another triangle that is shifted larger\n",
    "            forward(200)\n",
    "            left(120)\n",
    "            forward(200)\n",
    "            left(120)\n",
    "    \n",
    "    else:\n",
    "        forward(90)     # the rest that dont fit the nr\n",
    "        left(120)\n",
    "        forward(90)\n",
    "        left(120)\n",
    "        for i in range(3):   # another set of triangles that are to make the shapes different\n",
    "            forward(120)\n",
    "            left(120)\n",
    "            forward(120)\n",
    "            left(120)\n",
    "    end_fill()\n",
    "    nr += 1\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# here is a function that I created for showing a zoom with squares. They seemed to overlap into a cool shape that I really enjoyed and then the coloring on the inside was a bit weird and I dont know why it turned out to be a picaso painting on at the end but It does look cool!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from turtle import *\n",
    "\n",
    "makeTurtle = ()\n",
    "setPos = (-200, 30)                     # setting the position of where to start\n",
    "right = (30)\n",
    "fillToHorizontal = (0)\n",
    "setPenColor = ('red')\n",
    "nr = 1\n",
    "begin_fill()\n",
    "while nr <= 10:\n",
    "    if nr > 3 and nr < 8:\n",
    "        forward(100)\n",
    "        left(90)\n",
    "    for i in range(4):\n",
    "        forward(150)\n",
    "        left(90)\n",
    "        \n",
    "    else:\n",
    "        forward(200)\n",
    "        left(90)\n",
    "    for i in range(4):\n",
    "        forward(70)\n",
    "        left(90)\n",
    "    nr += 1\n",
    "end_fill()\n",
    "color = ('blue')\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# here is a better function to show the zoom theory with a circle and I like this fucntion beucase its simple but looks nice.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import turtle\n",
    "n=10\n",
    "while n <= 40:\n",
    "    turtle.circle(n) \n",
    "    n = n+10             # after each segement it will increase by 10 to create the \"nesting doll\" idea\n",
    "    \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " # this function is used for fun where I was able to learn on how to move a square around and to make it move across the screen. I really was interested in how this concept could be used and I really like the cool idea that you can make a box move across a screen. This gave me so much respect for game designers!!\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import turtle\n",
    "\n",
    "screen = turtle.Screen()\n",
    "screen.setup(500,500)\n",
    "screen.tracer(0)            # tell screen to not show automatically\n",
    "\n",
    "bob = turtle.Turtle()\n",
    "bob.speed(0)\n",
    "bob.width(3)\n",
    "bob.hideturtle()            # hide bob, we only want to see the drawing\n",
    "\n",
    "def draw_square() :\n",
    "    for side in range(4) :\n",
    "        bob.forward(100)\n",
    "        bob.left(90)\n",
    "\n",
    "bob.penup()                # pick up the pen\n",
    "bob.goto(-350, 0)\n",
    "bob.pendown()              # set the pen back down\n",
    "\n",
    "while True :\n",
    "    bob.clear()\n",
    "    draw_square()\n",
    "    screen.update()         # only now show the screen, as one of the frames\n",
    "    bob.forward(0.2)        # the speed that the square will be moving in the end"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

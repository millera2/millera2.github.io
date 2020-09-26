{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Triangle or Square? Please enter 3 or 4: 4\n",
      "Please enter initial heading: 45\n",
      "Please enter intial x-coordinate value: 30\n",
      "Please enter initial y-coordinate value: 30\n",
      "Please enter side length: 100\n",
      "Please enter color to fill: red\n"
     ]
    }
   ],
   "source": [
    "import turtle\n",
    "\n",
    "#inputs of turtle needed\n",
    "s = int(input('Triangle or Square? Please enter 3 or 4:'))\n",
    "h = float(input('Please enter initial heading:'))\n",
    "x = int(input('Please enter intial x-coordinate value:'))\n",
    "y = int(input('Please enter initial y-coordinate value:'))\n",
    "l = int(input('Please enter side length:'))\n",
    "color = input('Please enter color to fill:')\n",
    "\n",
    "#creating a turtle pen\n",
    "t = turtle.Turtle()\n",
    "\n",
    "#define a turtlr\n",
    "def tortise():\n",
    "\n",
    "    #initial settings for the turtle\n",
    "    t.penup()\n",
    "    t.goto(x,y)\n",
    "    t.setheading(h)\n",
    "    t.pendown()\n",
    "    t.fillcolor(color)\n",
    "    t.begin_fill()\n",
    "\n",
    "    #draw the turtle\n",
    "    for i in range (s):\n",
    "        t.forward(l)\n",
    "        t.left(360/s)\n",
    "\n",
    "    #stop filling color\n",
    "    t.end_fill()\n",
    "\n",
    "#output    \n",
    "tortise()"
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

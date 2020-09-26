{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# CS Homework Week 3"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 1. Make Square"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import turtle\n",
    "\n",
    "tortise = turtle.Turtle()\n",
    "\n",
    "def makeSquare(tortise, heading, x, y, sidelength, fillColor):\n",
    "    \"\"\"In this function makeSquare, it is filled in with a color and all of our arguments. Our arguments\n",
    "    tell us what the makeSquare function will create.\n",
    "    \"\"\"\n",
    "    tortise.setheading(heading)\n",
    "    tortise.goto(x,y)\n",
    "    tortise.fillcolor(fillColor)\n",
    "    tortise.begin_fill()\n",
    "    for i in range(4):\n",
    "        tortise.forward(sidelength)\n",
    "        tortise.left(90)\n",
    "    tortise.end_fill()\n",
    "        \n",
    "makeSquare(tortise, 0, 1, 1, 100, 'purple')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 2. Make Triangle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import turtle\n",
    "\n",
    "tortise = turtle.Turtle()\n",
    "\n",
    "def makeTriangle(tortise, heading, x, y, sidelength, fillColor):\n",
    "    \"\"\"In this function makeTriangle, it is filled in with a color and all of our arguments. Our arguments\n",
    "    tell us what the makeTriangle function will create.\n",
    "    \"\"\"\n",
    "    tortise.setheading(heading)\n",
    "    tortise.goto(x,y)\n",
    "    tortise.fillcolor(fillColor)\n",
    "    tortise.begin_fill()\n",
    "    for i in range(3):\n",
    "        tortise.forward(sidelength)\n",
    "        tortise.left(120) # our angle for the triangle is 120 and not 60 because the arrow was pointing outside of the triangle and not inside which would be 60\n",
    "    tortise.end_fill()\n",
    "        \n",
    "makeTriangle(tortise, 0, 1, 1, 100, 'blue')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 3. Spread"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Spread Square"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import turtle\n",
    "\n",
    "tortise = turtle.Turtle()\n",
    "\n",
    "def spreadSquare(tortise, heading, x, y, sidelength, fillColor):\n",
    "    \"\"\"In this function spreadSquare, it is filled in with a color plus all of our arguments. Our arguments\n",
    "    tell us what the spreadSquare function will create. This function will show many squares that are spread\n",
    "    out but still overlaping.\n",
    "    \"\"\"\n",
    "    for i in range (5): #need to repeat 5 times\n",
    "        tortise.setheading(heading+i*20)\n",
    "        tortise.goto(x,y)\n",
    "        tortise.fillcolor(fillColor)\n",
    "        tortise.begin_fill()\n",
    "        for i in range(4):\n",
    "            tortise.forward(sidelength)\n",
    "            tortise.left(90)\n",
    "        tortise.end_fill()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Spread Triangle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "Terminator",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTerminator\u001b[0m                                Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-3-d58414f4850e>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mturtle\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0mtortise\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mturtle\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mTurtle\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mspreadTriangle\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtortise\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mheading\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mx\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0my\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0msidelength\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mfillColor\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/turtle.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, shape, undobuffersize, visible)\u001b[0m\n\u001b[1;32m   3811\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mTurtle\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_screen\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   3812\u001b[0m             \u001b[0mTurtle\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_screen\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mScreen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 3813\u001b[0;31m         RawTurtle.__init__(self, Turtle._screen,\n\u001b[0m\u001b[1;32m   3814\u001b[0m                            \u001b[0mshape\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mshape\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   3815\u001b[0m                            \u001b[0mundobuffersize\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mundobuffersize\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/turtle.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, canvas, shape, undobuffersize, visible)\u001b[0m\n\u001b[1;32m   2555\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_undobuffersize\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mundobuffersize\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2556\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mundobuffer\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mTbuffer\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mundobuffersize\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 2557\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_update\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   2558\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2559\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mreset\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/turtle.py\u001b[0m in \u001b[0;36m_update\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m   2658\u001b[0m             \u001b[0;32mreturn\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2659\u001b[0m         \u001b[0;32melif\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_tracing\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 2660\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_update_data\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   2661\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_drawturtle\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2662\u001b[0m             \u001b[0mscreen\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_update\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m                  \u001b[0;31m# TurtleScreenBase\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/turtle.py\u001b[0m in \u001b[0;36m_update_data\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m   2644\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2645\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m_update_data\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 2646\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mscreen\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_incrementudc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   2647\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mscreen\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_updatecounter\u001b[0m \u001b[0;34m!=\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2648\u001b[0m             \u001b[0;32mreturn\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/turtle.py\u001b[0m in \u001b[0;36m_incrementudc\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m   1290\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0mTurtleScreen\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_RUNNING\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1291\u001b[0m             \u001b[0mTurtleScreen\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_RUNNING\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1292\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mTerminator\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1293\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_tracing\u001b[0m \u001b[0;34m>\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1294\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_updatecounter\u001b[0m \u001b[0;34m+=\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mTerminator\u001b[0m: "
     ]
    }
   ],
   "source": [
    "import turtle\n",
    "\n",
    "tortise = turtle.Turtle()\n",
    "\n",
    "def spreadTriangle(tortise, heading, x, y, sidelength, fillColor):\n",
    "    \"\"\"In this function spreadTriangle, it is filled in with a color plus all of our arguments. Our arguments\n",
    "    tell us what the spreadTriangle function will create. This function will show 4 triangles that are spread\n",
    "    out but still overlaping.\n",
    "    \"\"\"\n",
    "    for i in range (5):\n",
    "        tortise.setheading(heading+i*20)\n",
    "        tortise.goto(x,y)\n",
    "        tortise.fillcolor(fillColor)\n",
    "        tortise.begin_fill()\n",
    "        for i in range(3): # we are now working w triangles and the range would be 3 since there are only 3 sides\n",
    "            tortise.forward(sidelength)\n",
    "            tortise.left(120)\n",
    "        tortise.end_fill()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4. Zoom"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Zoom Square"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "import turtle\n",
    "\n",
    "tortise = turtle.Turtle()\n",
    "\n",
    "def zoomSquare(tortise, heading, x, y, sidelength, fillColor):\n",
    "    \"\"\"In this function zoomSquare, it is filled in with a color plus all of our arguments. Our arguments\n",
    "    tell us what the zoomSquare function will create. This function will show many squares on top of each other\n",
    "    as if they are zooming in to the smallest one.\n",
    "    \"\"\"\n",
    "    for k in range (5):\n",
    "        tortise.setheading(heading)\n",
    "        tortise.goto(x,y)\n",
    "        tortise.fillcolor(fillColor)\n",
    "        tortise.begin_fill()\n",
    "        for i in range(4):\n",
    "            tortise.forward(sidelength/(k+1))\n",
    "            tortise.left(90)\n",
    "        tortise.end_fill()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Zoom Triangle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "import turtle\n",
    "\n",
    "tortise = turtle.Turtle()\n",
    "\n",
    "def zoomTriangle(tortise, heading, x, y, sidelength, fillColor):\n",
    "    \"\"\"In this function zoomTriangle, it is filled in with a color plus all of our arguments. Our arguments\n",
    "    tell us what the zoomTriangle function will create. This function will show four Triangles on top of each other\n",
    "    as if they are zooming in to the smallest one.\n",
    "    \"\"\"\n",
    "    for k in range (4):\n",
    "        tortise.setheading(heading)\n",
    "        tortise.goto(x,y)\n",
    "        tortise.fillcolor(fillColor)\n",
    "        tortise.begin_fill()\n",
    "        for i in range(3):\n",
    "            tortise.forward(sidelength/(k+1))\n",
    "            tortise.left(120)\n",
    "        tortise.end_fill()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 5. Slide"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Slide Square"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "import turtle\n",
    "\n",
    "tortise = turtle.Turtle()\n",
    "\n",
    "def slideSquare(tortise, heading, x, y, sidelength, fillColor):\n",
    "    \"\"\"In this function slideSquare, it is filled in with a color plus all of our arguments. Our arguments\n",
    "    tell us what the slideSquare function will create. This function will show many squares sliding to the right\n",
    "    but still overlapping its a slight shift in the shape.\n",
    "    \"\"\"\n",
    "    for k in range (5):\n",
    "        tortise.setheading(heading)\n",
    "        tortise.goto(x+(k*10),y)\n",
    "        tortise.fillcolor(fillColor)\n",
    "        tortise.begin_fill()\n",
    "        for i in range(4):\n",
    "            tortise.forward(sidelength)\n",
    "            tortise.left(90)\n",
    "        tortise.end_fill()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Slide Triangle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "import turtle\n",
    "\n",
    "tortise = turtle.Turtle()\n",
    "\n",
    "def slideTriangle(tortise, heading, x, y, sidelength, fillColor):\n",
    "    \"\"\"In this function slideTriangle, it is filled in with a color plus all of our arguments. Our arguments\n",
    "    tell us what the slideTriangle function will create. This function will show many trianlge sliding to the right\n",
    "    but still overlapping its a slight shift in the shape.\n",
    "    \"\"\"\n",
    "    for k in range (4):\n",
    "        tortise.setheading(heading)\n",
    "        tortise.goto(x+(k*10),y)\n",
    "        tortise.fillcolor(fillColor)\n",
    "        tortise.begin_fill()\n",
    "        for i in range(3):\n",
    "            tortise.forward(sidelength)\n",
    "            tortise.left(120)\n",
    "        tortise.end_fill()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 6. Main Function"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "def main():\n",
    "    TrianglesOrSquares = input(\"Please input Triangles or Squares\")\n",
    "    Sidelength = input(\"Please input Side length\")\n",
    "    Color = input(\"Please input Color\")\n",
    "    StartingCoordinatesX = input(\"Please input Starting X Coordinates\")\n",
    "    StartingCoordinatesY = input(\"Please input Starting Y Coordinates\")\n",
    "    SpreadZoomOrSlide = input(\"Please input Spread, Zoom, or Slide\")\n",
    "    if TrianglesOrSquares == \"Squares\":\n",
    "        if SpreadZoomOrSlide == \"Zoom\":\n",
    "            zoomSquare(tortise, 0,int(StartingCoordinatesX), int(StartingCoordinatesY), int(Sidelength), Color)\n",
    "        if SpreadZoomOrSlide == \"Slide\":\n",
    "            slideSquare(tortise, 0,int(StartingCoordinatesX), int(StartingCoordinatesY), int(Sidelength), Color)\n",
    "        if SpreadZoomOrSlide == \"Spread\":\n",
    "            spreadSquare(tortise, 0,int(StartingCoordinatesX), int(StartingCoordinatesY), int(Sidelength), Color)\n",
    "    if TrianglesOrSquares == \"Triangles\":\n",
    "        if SpreadZoomOrSlide == \"Zoom\":\n",
    "            zoomTriangle(tortise, 0,int(StartingCoordinatesX), int(StartingCoordinatesY), int(Sidelength), Color)\n",
    "        if SpreadZoomOrSlide == \"Slide\":\n",
    "            slideTriangle(tortise, 0,int(StartingCoordinatesX), int(StartingCoordinatesY), int(Sidelength), Color)\n",
    "        if SpreadZoomOrSlide == \"Spread\":\n",
    "            spreadTriangle(tortise, 0,int(StartingCoordinatesX), int(StartingCoordinatesY), int(Sidelength), Color)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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

#!/usr/bin/env python
# coding: utf-8

# In[34]:


#MAKESQUARE function, return heading, x,y, length, fill color

import turtle

wn=turtle.Turtle
tortoise=turtle.Turtle()

length=int(100)

tortoise.pencolor((0,0,0))
tortoise.fillcolor((1.0,1.0,0))
tortoise.begin_fill()

for segment in range (1):
    tortoise.forward(length)
    tortoise.left(90)
    tortoise.forward(length)
    tortoise.left(90)
    tortoise.forward(length)
    tortoise.left(90)
    tortoise.forward(length)
    tortoise.left(90)
tortoise.end_fill()

tortoise.heading


# In[35]:


#MAKETRIANGLE function, return heading, x,y, length, fill color

import turtle

wn=turtle.Turtle
tortoise=turtle.Turtle()

length=int(100)

tortoise.pencolor((0,0,0))
tortoise.fillcolor((1.0,1.0,0))
tortoise.begin_fill()

for segment in range (1):
    tortoise.forward(length)
    tortoise.left(120)
    tortoise.forward(length)
    tortoise.left(120)
    tortoise.forward(length)
    tortoise.left(120)
tortoise.end_fill()

tortoise.heading


# In[39]:


#SLIDE with triangle


import turtle

wn=turtle.Turtle
tortoise=turtle.Turtle()

length=int(100)

tortoise.pencolor((0,0,0))
tortoise.fillcolor((1.0,1.0,0))
tortoise.begin_fill()

for segment in range (1):
    tortoise.forward(length)
    tortoise.left(120)
    tortoise.forward(length)
    tortoise.left(120)
    tortoise.forward(length)
    tortoise.left(120)
tortoise.end_fill()

tortoise.penup()
tortoise.forward(50)
tortoise.pendown()

for segment in range (1):
    tortoise.forward(length)
    tortoise.left(120)
    tortoise.forward(length)
    tortoise.left(120)
    tortoise.forward(length)
    tortoise.left(120)
tortoise.end_fill()

tortoise.penup()
tortoise.forward(50)
tortoise.pendown()

for segment in range (1):
    tortoise.forward(length)
    tortoise.left(120)
    tortoise.forward(length)
    tortoise.left(120)
    tortoise.forward(length)
    tortoise.left(120)
tortoise.end_fill()

tortoise.penup()
tortoise.forward(50)
tortoise.pendown()

for segment in range (1):
    tortoise.forward(length)
    tortoise.left(120)
    tortoise.forward(length)
    tortoise.left(120)
    tortoise.forward(length)
    tortoise.left(120)
tortoise.end_fill()

tortoise.heading


# In[40]:


#ZOOM(III) with square

import turtle

wn=turtle.Turtle
tortoise=turtle.Turtle()

length=int(100)

tortoise.pencolor((0,0,0))
tortoise.fillcolor((1.0,1.0,0))
tortoise.begin_fill()

for segment in range (1):
    tortoise.forward(length)
    tortoise.left(90)
    tortoise.forward(length)
    tortoise.left(90)
    tortoise.forward(length)
    tortoise.left(90)
    tortoise.forward(length)
    tortoise.left(90)
tortoise.end_fill()

length=int(75) 

for segment in range (1):
    tortoise.forward(length)
    tortoise.left(90)
    tortoise.forward(length)
    tortoise.left(90)
    tortoise.forward(length)
    tortoise.left(90)
    tortoise.forward(length)
    tortoise.left(90)
tortoise.end_fill()

length=int(50) 

for segment in range (1):
    tortoise.forward(length)
    tortoise.left(90)
    tortoise.forward(length)
    tortoise.left(90)
    tortoise.forward(length)
    tortoise.left(90)
    tortoise.forward(length)
    tortoise.left(90)
tortoise.end_fill()

tortoise.heading


# In[ ]:


#MAKESQUARE with osc function
import turtle 
   
wn=turtle.Screen()   
tortoise=turtle.Turtle()   
  
length=int(100)
    
def square(x,y):  
    tortoise.penup() 
    tortoise.goto(x,y)
    tortoise.pendown() 
    for i in range(4):  
        tortoise.forward(length) 
        tortoise.left(90) 
        tortoise.forward(length) 
          
turtle.onscreenclick(square,1) 
  
turtle.listen() 
   
turtle.done()


# In[ ]:


#MAKETRIANGLE with osc function
import turtle 
   
wn=turtle.Screen()   
tortoise=turtle.Turtle()   
  
length=int(100)    
  
def triangle(x,y):  
    tortoise.penup() 
    tortoise.goto(x,y)  
    tortoise.pendown() 
    for i in range(3):  
        tortoise.forward(length) 
        tortoise.left(120) 
        tortoise.forward(length) 
          
turtle.onscreenclick(triangle,1) 
  
turtle.listen() 
   
turtle.done()


# In[ ]:


#functional abstraction is important to programming, but only because it's important that we, as programmers, understand what it means when we call on a specific function
#functional abstraction is relevant to this assignment because the class "turtle" already exists in phython language. it is most important that we understand what each function in this class actually does.


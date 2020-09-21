import random
import math

def monteCarlo(n):
    x = 0
    y = 0
    for i in range(n):
        rando = random.random()
        if rando < .25:
            x +=1
        elif rando>=.25 and rando<.5:
            y +=1
        elif rando>=.5 and rando <.75:
            x -=1
        else:
            y -=1
    return(math.sqrt(x**2+y**2))

def avgMonteCarloDist(steps, n):
    distances = 0
    for i in range(n):
            distances += monteCarlo(steps)
    return(distances/n)
    
for i in range(5000):
    avgMonteCarloDist(i, 1000)

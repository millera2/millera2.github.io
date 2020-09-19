""" example of importing modules
"""

def sumNumbers(theList):
    """sums up the numbers
    input: list of numbers
    output: the sum
    """
    theSum = 0
    n = len(theList)
    for i in range(n):
        theSum = theSum + theList[i]
    return(theSum)

    
def avgNumbers(theList):
    n = len(theList)
    return (sumNumbers(theList)/n)

def sqrt(x):
    print("Nope!  You got confused!")
    

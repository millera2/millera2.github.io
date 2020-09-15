"""Just an example of module namespaces
"""

def sumNumbers(list):
    """Adds numbers in the list
    input: list
    outpu: sum
    """
    sum = 0
    n = len(list)
    for i in range(n):
        sum += list[i]
    return sum

def sqrt(a):
    print("nope, fake!")
# helpers.py

def skipN(array, n, acc = None):
    if array is None:
        array = []
    if acc is None:
        acc = 0
    if len(array) == 0:
        return []
    if acc == 0:
        # TODO: if acc == 0 include number, and put 'n' in 'acc'
        return [array[0]] + skipN(array[1:], n, n)
    else:
        # else skip number and decrease 'acc'
        return skipN(array[1:], n, acc - 1)

def divide_array(speedArray):
    newList = []
    for i in range(len(speedArray)):
        newList.append(speedArray[i] / 10)
    return newList

def average(speedArray):
    """Calculate average speed for 10sec"""
    # result = sum(speedArray) / 1.67sec?
    return []


"""
Assess what information you are given. Use this method if you know:
two or more different speeds; and
that those speeds were traveled for the same amount of time.
For example, if Ben drives 40 mph for 2 hours, and 60 mph for another 2 hours, what is his average speed for the entire trip?
S = a+b/time
S = 40+60/2
"""
"""
[0.5, 0.4, 0.4, 0.4, 0.5, 0.6]
What i have 5 m/s for 1.67sec long 4 m/s for 1.67sec long and so on.
"""

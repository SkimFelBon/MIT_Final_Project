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

def average(speedArray):
    """Calculate average speed for 10sec"""
    result = (sum(speedArray) / len(speedArray)) / 10
    return round(result, 2)


"""
Assess what information you are given. Use this method if you know:
two or more different speeds; and
that those speeds were traveled for the same amount of time.
For example, if Ben drives 40 mph for 2 hours, and 60 mph for another 2 hours, what is his average speed for the entire trip?
S = a+b/time
S = 40+60/2
OR
If Ben traveled 50 mph for 3 hours, 60 mph for 2 hours,
and 70 mph for 1 hour, what was his average speed for the entire trip?
S = (s1t1 + s2t2 + s3t3) / t1 + t2 + t3
S = (50*3+60*2+70*1) / (3+2+1)
S = 340/6
S = 56.67mph
"""

"""
[0.5, 0.4, 0.4, 0.4, 0.5, 0.6]
[5, 4, 4, 4, 5, 6]
What i have is 0.5 m/s for 1.67sec long 0.4 m/s for 1.67sec long and so on.
TODO: Let's assume we have 5m/s, 4m/s and so on. How to convert this speed to km/h?

"""

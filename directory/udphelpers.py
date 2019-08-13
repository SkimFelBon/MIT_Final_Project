# udphelpers.py

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

def skipSpace(text, acc = None):
    if acc is None:
        acc = 0
    speedList = []
    """ this function skip's space and append's integers to list"""
    for i in text:
        #if acc >= 6:
        #    break
        if i.isspace():
            continue
        speedList.append(int(i))
        #acc+=1
    return speedList

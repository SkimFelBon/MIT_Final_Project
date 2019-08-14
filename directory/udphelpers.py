# udphelpers.py

def findSpeed(text):
    """ Produce array of speeds, from line in winter.log file"""
    import re
    speedRegex = re.compile('''\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\n?
                            ''',re.VERBOSE)
    speedList = []
    group = speedRegex.findall(text)
    for i in range(len(group[0])):
        speedList.append(int(group[0][i]))
    return speedList



def skipN(array, n, acc = None):
    """Skip elements in array with step n"""
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
    """ this function skip's space and append's integers to list"""
    if acc is None:
        acc = 0
    speedList = []
    for i in text:
        #if acc >= 6:
        #    break
        if i.isspace():
            continue
        speedList.append(int(i))
        #acc+=1
    return speedList

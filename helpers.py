# helpers.py

def helperFunc(data):
    myList = []
    for i in reversed(data):
        if i > 7:
            break
        myList.append(i)
    return myList
"""
>>> data[8:10]
b'\x05\x00'
>>> data[10:12]
b'\x04\x00'
>>> data[12:14]
b'\x04\x00'
>>> data[14:16]
b'\x04\x00'
>>> data[16:18]
b'\x05\x00'
>>> data[18:20]
b'\x06\x00'
"""

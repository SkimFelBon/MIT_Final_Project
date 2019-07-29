# tempoStorm.py

# filepath = 'sample.log'
# with open(filepath) as fp:
#    for cnt, line in enumerate(fp):
#        print("Line {}: {}".format(cnt, line))

# fileObj = open("sample.log",'r')
# while True:
#     line = fileObje.readline()
#     print(line)
# fileObj.close()

filepath = 'sample.log'
with open(filepath) as fp:
   for i, line in enumerate(fp):
       print(str.encode(f"Line {i}: {line}"))

# fileObj = open('sample.log','r')
# bytesToSend = fileObj.readline()
# print(str.encode(bytesToSend))
#bytesToSend = str.encode(f"Line {i}: {line}")

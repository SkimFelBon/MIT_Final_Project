# udpServerV4.py
import socket, json
import binascii
from helpers import skipN, divide_array
import time
"""This example doesn't send reply to client"""

# msg = function(arg1, arg2, arg3)
# f = open('/tmp/output', 'w')
# f.write(msg)
# f.close()

with open('config.json') as json_data_file:
        data = json.load(json_data_file)
localIP = data['myServer']['local_local']
localPort = int(data['myServer']['localPort'])
bufferSize = 1024

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

# Listen for incoming datagrams
i = 0
speedArray = []
try:
    while i < 9:
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        readableTime = time.localtime()
        OpTime = time.asctime()
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]
        print("Message from Client:{}".format(message))
        print("Client IP Address:{}".format(address))
        # DONE: parse response
        listByte = list(message[-12:-1])
        speedArray = divide_array(skipN(listByte, 1))
        print(speedArray)
        # TODO: calc everage speed per 10 sec
        # REWORK LATER increment here, just for simplicity during tests
        i+=1
finally:
    UDPServerSocket.close()

# Message from Client:b'SNDT\x00\x00\x00\t\x05\x00\x04\x00\x04\x00\x04\x00\x05\x00\x06\x00'
# Client IP Address:('127.0.0.1', 52493)
# [5, 4, 4, 4, 5, 6]

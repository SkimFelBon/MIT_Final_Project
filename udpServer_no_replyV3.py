# udpServerV4.py
import socket, json
import binascii
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

msgFromServer = "Hello UDP Client"
bytesToSend = str.encode(msgFromServer)

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

# Listen for incoming datagrams
i = 0
try:
    while i < 9:
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]
        clientMsg = "Message from Client:{}".format(message)
        clientIP = "Client IP Address:{}".format(address)
        print(clientMsg)
        print(clientIP)
        i+=1
        # Sending a reply to client
        #UDPServerSocket.sendto(bytesToSend, address)
finally:
    UDPServerSocket.close()

# Output:
# Message from Client:b'Line 8: 2019:02:26->> 14:16:15:    0:01:30   29   25   22   28   35   32\n'
# Client IP Address:('91.204.85.6', 63099)
# Message from Client:b'SNDT\x00\x00\x00\t\x05\x00\x04\x00\x04\x00\x04\x00\x05\x00\x06\x00'
# Client IP Address:('91.204.85.19', 14000)

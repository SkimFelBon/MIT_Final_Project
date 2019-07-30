# udpServerV4.py
import socket, json
import binascii
"""This example doesn't send reply to client"""

# msg = function(arg1, arg2, arg3)
# f = open('/tmp/output', 'w')
# f.write(msg)
# f.close()

def writeToFile(response):
    fileObj = open('response.txt','wb')
    fileObj.write(response)
    fileObj.close()
    with open('response.txt','wb') as txt_data_file:
        txt_data_file.write(response)
    with open('responseByte','wb') as byte_data_file:
        byte_data_file.write(response)
    return None

with open('config.json') as json_data_file:
        data = json.load(json_data_file)
localIP = data['myServer']['PPPoeIP']
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
try:
    while True:
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]
        #clientMsg = "Message from Client:{}".format(message)
        clientMsg = binascii.hexlify(message)
        clientIP = "Client IP Address:{}".format(address)
        print(clientMsg)
        print(clientIP)
        print()
        print()
        # Sending a reply to client
        #UDPServerSocket.sendto(bytesToSend, address)
finally:
    UDPServerSocket.close()

# Output:
# UDP server up and listening
#
# Message from Client:b"Hello UDP Server"
#
# Client IP Address:("127.0.0.1", 51696)

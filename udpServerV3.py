# udpServerV3.py
import socket, json

"""This example send reply to client"""

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
        clientMsg = "Message from Client:{}".format(message)
        clientIP = "Client IP Address:{}".format(address)
        print(clientMsg)
        print(clientIP)
        # Sending a reply to client
        UDPServerSocket.sendto(bytesToSend, address)
finally:
    UDPServerSocket.close()

# Output:
# UDP server up and listening
#
# Message from Client:b"Hello UDP Server"
#
# Client IP Address:("127.0.0.1", 51696)

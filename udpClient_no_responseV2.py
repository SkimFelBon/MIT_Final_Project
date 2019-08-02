# udpClient_no_responseV2.py
import socket, json
"""This client doesn't await reply from server"""

with open('config.json') as json_data_file:
        data = json.load(json_data_file)
myIP = data['myServer']['local_local']
myPort = int(data['myServer']['localPort'])

serverAddressPort = (myIP, myPort)
bufferSize = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Send to server using created UDP socket


with open("test.dat", "rb") as binary_file:
    data = binary_file.read()
    UDPClientSocket.sendto(data, serverAddressPort)

       #msgFromServer = UDPClientSocket.recvfrom(bufferSize)

       #msg = "Message from server {}".format(msgFromServer[0])

       #print(msg)

# Output:
# Message from Server b"Hello UDP Client"

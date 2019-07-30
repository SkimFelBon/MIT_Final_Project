import socket

# msgFromClient = "Hello UDP Server"
# bytesToSend = str.encode(msgFromClient)
serverAddressPort = ("127.0.0.1", 8000)
bufferSize = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Send to server using created UDP socket

filepath = 'sample.log'
with open(filepath) as fp:
   for i, line in enumerate(fp):
       msgFromClient = f"Line {i}: {line}"
       bytesToSend = str.encode(msgFromClient)
       UDPClientSocket.sendto(bytesToSend, serverAddressPort)

       msgFromServer = UDPClientSocket.recvfrom(bufferSize)

       msg = "Message from server {}".format(msgFromServer[0])

       print(msg)

# Output:
# Message from Server b"Hello UDP Client"
# client_server_system.py
""" TODO: Doesn't work for some reason"""
import socket
import sys
from _thread import *
host = ''
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def threaded_client(conn):
    conn.send(str.encode('Welcome, type your info\n'))

    while True:
        data = conn.recv(1024)
        reply = 'Server output: '+ data.decode('utf-8')
        if not data:
            break
        conn.sendall(str.encode(reply))
    conn.close()

try:
    s.bind((host,port))
except socket.error as e:
    print(str(e))

s.listen(5)
print('Waiting for a connection.')


while True:
    conn, addr = s.accept()
    print('connected to: ' + addr[0]+':'+str(addr[1]))

    start_new_thread(threaded_client, (conn,))

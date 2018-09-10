#!/usr/bin/env python

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('192.168.110.52', 9004)
print('starting up on {} port {}'.format(*server_address))
sock.connect(('192.168.110.52',9004))
print("connected!")
sock.send(b'LON')

response = sock.recv(8192)

print("respuesta : ",response)

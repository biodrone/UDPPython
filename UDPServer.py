#!/usr/bin/python

import threading
import Queue
import socket

hash = ""
pos = 0

UDP_IP_S = "127.0.0.1"
UDP_PORT_S = 13337
MESSAGE = "Hello, World!"
message = ''

print "UDP target IP: ", UDP_IP
print "UDP target port: ", UDP_PORT
print "Message: ", MESSAGE

while message != 3:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(MESSAGE, (UDP_IP_S, UDP_PORT_S))

if message == 1:
    print 'message = 1'
elif message == 2:
    print 'message = 2'
elif message == 3:
    print 'message = 3'


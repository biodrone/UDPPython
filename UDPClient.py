#!/usr/bin/python

import socket

UDP_IP_R = "127.0.0.1"
UDP_PORT_R = 13337

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP_R, UDP_PORT_R))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", data


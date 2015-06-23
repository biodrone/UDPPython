#!/usr/bin/pythonS

import threading
import Queue
import socket
import time
import logging

UDP_IP_S = "127.0.0.1"
UDP_PORT_S = 13337
UDP_IP_R = "127.0.0.1"
UDP_PORT_R = 13338
MESSAGE = "Hello, World!"

def sender():
    print 'Sending...'
    i = 0
    while i < 20:
        sockS = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sockS.sendto(MESSAGE, (UDP_IP_S, UDP_PORT_S))
        time.sleep(1)
        print i
        i += 1
    return
def listener():
    print 'Listening...'
    j = 0
    sockR = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sockR.bind((UDP_IP_R, UDP_PORT_R))


    data, addr = sockR.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", data

    if data == 1:
        print 'message = 1'
    elif data == 2:
        print 'message = 2'
    elif data == 3:
        print 'message = 3'
    return

s = threading.Thread(name='Sender', target=sender)
l = threading.Thread(name='Listener', target=listener)

s.start()
l.start()
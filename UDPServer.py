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
MESSAGE = socket.gethostname()
workers = 0
exit = 0

def sender():
    global exit
    print 'Sending...'
    while exit == 0:
        sockS = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sockS.sendto(MESSAGE, (UDP_IP_S, UDP_PORT_S))
        time.sleep(1)
    return
def listener():
    global workers
    global exit
    while workers <= 3:
        print 'Listening...'
        sockR = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sockR.bind((UDP_IP_R, UDP_PORT_R))

        data, addr = sockR.recvfrom(1024) # buffer size is 1024 bytes
        print "New Worker:", data
        workers += 1

        if data == 1:
            print 'message = 1'
        elif data == 2:
            print 'message = 2'
        elif data == 3:
            print 'message = 3'
    exit = 1
    return

s = threading.Thread(name='Sender', target=sender)
l = threading.Thread(name='Listener', target=listener)

s.start()
l.start()
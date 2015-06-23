#!/usr/bin/python

import socket
import threading
import time
import logging

UDP_IP_R = "127.0.0.1"
UDP_PORT_R = 13337
UDP_IP_S = "127.0.0.1"
UDP_PORT_S = 13338
MESSAGE = socket.gethostname()

def sender(): # client sender only sends once, on WAN might need more
    print 'Sending...'
    sockS = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sockS.sendto(MESSAGE, (UDP_IP_S, UDP_PORT_S))
    return
def listener():
	print 'Listening...'
	try:
		sockR = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sockR.bind((UDP_IP_R, UDP_PORT_R))
		sockR.settimeout(5) # sets timeout in case server is off

	  	data, addr = sockR.recvfrom(1024) # buffer size is 1024 bytes
	   	print "Connected to Controller:", data
   	except socket.timeout:
   		print 'timeout: client exiting'
   		sockR.close()

s = threading.Thread(name='Sender', target=sender)
l = threading.Thread(name='Listener', target=listener)

s.start()
l.start()
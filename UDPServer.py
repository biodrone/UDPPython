#!/usr/bin/python

import threading
import Queue
import socket
import time
import logging
from bs4 import BeautifulSoup
import urllib2

UDP_IP_S = "127.0.0.1"
UDP_PORT_S = 13337
UDP_IP_R = "127.0.0.1"
UDP_PORT_R = 13338
MESSAGE = 0
workers = 0
exit = 0
cmd = 1

def sender(): # sends until something changes exit to 1
    global exit
    print 'Sending...'
    ## TODO: Make this get a command from the parser
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
        sockR.close()
        print "New Worker:", data
        workers += 1
    exit = 1
    return
def checker(): ## TODO: Accept a URL as input maybe?
    while exit == 0:
        print 'Parsing...'
        global cmd
        url = "http://176.31.191.50/index.html"
        response = urllib2.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html)

        cmd = len(soup.a.string) # gets the length of the first name
        print 'Parsing result is', cmd
        time.sleep(10)
    return
s = threading.Thread(name='Sender', target=sender)
l = threading.Thread(name='Listener', target=listener)
c = threading.Thread(name='Checker', target=checker)

c.start()
time.sleep(2) # give the parser a hot second
s.start()
l.start()
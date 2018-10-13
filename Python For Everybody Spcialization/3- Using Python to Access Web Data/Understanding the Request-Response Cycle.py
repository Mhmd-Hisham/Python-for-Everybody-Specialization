#!/usr/bin/env python3
# Instructor: Dr. Chuck Severance
# Course: Using Python to Access Web Data, University of Michigan, Coursera.

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("data.pr4e.org", 80))
s.send("GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n".decode())
	
while True:
    data += s.recv(512)
    if len(data) < 1:
        break
	
    data = data.decode()
	
    print(data)

s.close()    

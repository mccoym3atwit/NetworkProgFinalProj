#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 18:38:24 2020

@author: matt
"""


import socket

host = socket.gethostname()
port = 1234
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

c.connect((host, port))

print('Server: ' + c.recv(1024).decode())
    
message = input( )

while message.lower().strip() != 'end':
        c.send(message.encode())
        print('Server: ' + c.recv(1024).decode())
        
        message = input()
c.send(message.encode())
c.close()
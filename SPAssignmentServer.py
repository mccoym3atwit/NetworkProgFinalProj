#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 18:38:20 2020

@author: matt
"""


import socket

host = socket.gethostname()
port = 1234
WELCOME_MESSAGE = "Hello! This is a chat server."
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))

s.listen(1)


conn, address = s.accept()

conn.send(WELCOME_MESSAGE.encode())
data = conn.recv(1024).decode()
while data.lower().strip() != 'end':
    print("Client: " + str(data))
    
    data = input( )
    conn.send(data.encode())
    data = conn.recv(1024).decode()
print("The session has ended.")   
s.close()

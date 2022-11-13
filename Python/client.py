"""
Dev: Prajwal Nautiyal
Last Update: 11 November 2022
A client that connects to a server and sends data.
"""

import socket  # Import socket module

so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      # Create a socket object
port = 1234                                                 # Reserve a port for your service.
server = '127.0.0.1'

so.connect((server, port))                                  # Connect to the server
so.send('Hello server!'.encode())                           # Send data to the server
print(so.recv(1234).decode())                               # Print the data received from the server
so.close()                                                  # Close the connection
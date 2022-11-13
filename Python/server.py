"""
Dev: Prajwal Nautiyal
Last Update: 11 November 2022
A server that listens for incoming connections and prints the data received and stores the transmission info in a file.
"""

import csv                  # Importing the csv module to wrtite the data to a csv file
import re                   # Importing the re module to extract the data from the connection string
import socket               # Import socket module
import pandas as pd         # Write the formatted transmission info to a file


def serverConec():
    host = '127.0.0.1'                                  # Using the loopback address
    port = 1234                                         # Reserve a port for the service.
    server = socket.create_server((host, port), family=socket.AF_INET)                                                     # Create a socket object                         # Bind to the port
    server.listen(10)                                   # Now wait for client connection.
    cli, addr = server.accept()                         # Establish connection with client.
    protocol = cli.proto                                # Extracting the protocol property from the connection object
    connection = str(cli)                               # Converting the connection object to a string
    src = re.findall("raddr=\('(\d{3}\.\d\.\d\.\d)\',\s(\d+)", connection)                                                  # Extracting the source IP and port from the connection string
    dest = re.findall("laddr=\('(\d{3}\.\d\.\d\.\d)\',\s(\d+)", connection)                                                 # Extracting the destination IP and port from the connection string
    print(f'Got connection from {addr[0]} onto port {addr[1]}\nThe protocol is {protocol}')                                 # Print the address of the client
    
    try:
        print(cli.recv(1234).decode())                  # Print the data received from the client
    except:
        pass
    cli.send('Thank you for connecting'.encode())       # Send a thank you message to the client.
    cli.close()                                         # Close the connection
    with open('transmission.csv', mode='a') as fl:      # Open the file in write mode
        writer = csv.writer(fl, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)                                    # Create a csv writer object
        writer.writerow([src[0][0], dest[0][0], src[0][1], dest[0][1], protocol])                                           # Write the data to the file
    df = pd.read_csv('transmission.csv')                # Read the data from the file
    df.to_csv('transmission.csv', index=False)          # Write the data to the file without the index column
    
if __name__ == '__main__':
    with open('transmission.csv', mode='w+') as fl:     # Open the file in write mode
        writer = csv.writer(fl, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Source IP', 'Destination IP', 'Source Port', 'Destination Port', 'Protocol'])                     # Write the headers to the file
    fl.close()                                          # Close the file
    while True:
        serverConec()
        
"""
Citations
1: https://docs.python.org/3/library/socket.html
2: https://docs.python.org/3/library/csv.html
3: https://www.tutorialspoint.com/python/python_files_io.htm
4: https://www.geeksforgeeks.org/python-script-to-monitor-network-connection-and-saving-into-log-file/
5: https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client
6: https://realpython.com/python-csv/
"""
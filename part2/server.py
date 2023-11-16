#import the neede librarires.
import socket
import time

# Create a UDP socket.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific address and port.
server_address = ('', 8855)
server_socket.bind(server_address)

# Dictionary to store the last received message from each client.
client_messages = {}

#This message to know the user that server start working.
print('\nServer is listening on port 8855...\n')

#Server name.
print('Server Razan Odeh.')

index = 0
while True:
    # Receive a message and the client address.
    data, client_address = server_socket.recvfrom(1024)
    message = data.decode()

    # Get the client name from the message.
    client_name = message.split(",")[0]

    # Update the last received message from the client.
    client_messages[client_address] = message

    
    index += 1

    # Print the last received message from each client.
    for address, msg in client_messages.items():
        name = msg.split(",")[0]
        last_received = time.strftime('%H:%M:%S')
        print(f"{index} - {name}: Last received message at {last_received}")
    print("======================================")

# Close the socket.
server_socket.close()




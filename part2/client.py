#Import the needed libraries.
import socket
import time

# Create a UDP socket.
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enable broadcasting.
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Set the broadcast address and port.
broadcast_address = ("192.168.1.15", 8855) 

while True:
    client_name = "Maisam Alaa"
    # Construct the message to be sent.
    message = f"{client_name},{socket.gethostbyname(socket.gethostname())}"

    # Send the message to the broadcast address.
    client_socket.sendto(message.encode(), broadcast_address)
    
    # Print the sent message and current time when the message has sent.
    print(f"Sent message: {message} at {time.strftime('%H:%M:%S')}")

    # Wait for 2 seconds before sending the next message.
    time.sleep(2)





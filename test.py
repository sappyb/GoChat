import os
import socket
# The address of the file, which will be a bridge for communication between PHP and Python
SERVER_PATH = '/tmp/echo.sock'

# If the file already exists, it is necessary to remove
if os.path.exists(SERVER_PATH):

    os.remove(SERVER_PATH)

# Create a new UNIX server
server_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server_socket.bind(SERVER_PATH)
server_socket.listen()

while True:

    client, address = server_socket.accept()
    message = client.recv(1024)
    # Print the incoming message
    print('received:', message.decode("utf-8"))
    # Send response
    client.send('This is my Response!'.encode())

client.close()
server_socket.close()
print('UNIX server closed!')

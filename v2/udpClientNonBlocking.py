from socket import *

serverPort = 10000

# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
serverAddress = ('localhost', 10000)

# Make it a non blocking socket
clientSocket.setblocking(0)

# Sockets from which we expect to read
inputs = [ clientSocket ]

# Sockets to which we expect to write
outputs = [ ]

# Outgoing message queues (socket:Queue)
message_queues = {}

message = 'This is the message.  It will be repeated.'

try:

    # Send data, message needs to be encoded as bytes
    print ('Sending... %s' % message)
    sent = clientSocket.sendto(message.encode(), serverAddress)

    # Receive response
    print('waiting to receive...')
    data, remoteSocket = clientSocket.recvfrom(4096)
    print('Received... %s \nFrom %s ' % (data.decode(),remoteSocket))

finally:
    print('Closing socket')
    clientSocket.close()

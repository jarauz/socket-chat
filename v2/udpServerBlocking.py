from socket import *
import time

serverPort = 10000
# Create a UDP socket
serverSocket=socket(AF_INET, SOCK_DGRAM)

# Bind the socket to the port
serverAddress = ("localhost", 10000)
print ('starting up on %s port %s' % serverAddress)
serverSocket.bind(serverAddress)


while True:
    print("Waiting to receive message")
    data, remoteSocket = serverSocket.recvfrom(4096)
    print ("Received %s bytes from remote socket %s" % (len(data), remoteSocket))
    # data comes back as bytes, needs to be decoded to appear as string
    print (data.decode())
    print ("Delaying sending back data to show effect of blocking...")
    time.sleep(3.0)
    if data:
        sent = serverSocket.sendto(data.upper(), remoteSocket)
        print ("Sent %s bytes back to %s" % (sent, remoteSocket))

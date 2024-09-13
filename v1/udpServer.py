from socket import *
serverPort = 10000

# Internet and UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
f1=open("rxfile.txt", "w")
serverSocket.bind(("localhost", serverPort)) 
print ("Server socket ready... listening to port %d." % serverPort)
while True:
     data, addr = serverSocket.recvfrom(1024) # buffer size is 1024 bytes
     print ("received message: %s" %data)
     f1.write(data.decode("utf-8")+"\n")

from socket import *
serverIP = "localhost"
serverPort = 10000

# Internet and UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input("Input lowercase sentence:") 
clientSocket.sendto(message.encode(), (serverIP, serverPort))
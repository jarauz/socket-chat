from socket import *
serverIP = 'localhost'
serverPort = 10000

# Internet and UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input("Please input lowercase sentence:")
clientSocket.sendto(message.encode(), (serverIP, serverPort))
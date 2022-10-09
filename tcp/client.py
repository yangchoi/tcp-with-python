from socket import *

serverName = "localhost"
serverPort = 4321

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

sentence = input("input lowercase sentece: ")
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print("from server: ", modifiedSentence.decode())
clientSocket.close()

from socket import *

serverPort = 4321
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))

# 서버가 클라이언트로부터 TCP 연결 요청을 듣도록 한다.
# 파라미터는 큐가 연결되는 연결의 최대수를 나타낸다.
serverSocket.listen(1)

print("the server is ready to receive")
while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    captializedSentence = sentence.upper()
    connectionSocket.send(captializedSentence.encode())
    connectionSocket.close()

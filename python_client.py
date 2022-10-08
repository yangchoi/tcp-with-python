from socket import *

ip = "127.0.0.1"
port = 1234

# 소켓 생성
clientSocket = socket(AF_INET, SOCK_STREAM)
#서버와 연결
clientSocket.connect((ip, port))

print("연결 확인")
# 데이터 송신
clientSocket.send("I'm a client".encode("utf-8"))

print("메세지 전송")
# 데이터 수신
data = clientSocket.recv(1024)

print("받은 데이터: ", data.decode("utf-8"))
# 연결종료
clientSocket.close()

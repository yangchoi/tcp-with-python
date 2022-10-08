from socket import *

host = "127.0.0.1"
port = 1234

# 소켓생성
serverSocket = socket(AF_INET, SOCK_STREAM) 
# 생성한 소켓 설정에 필요한 Host와 Port 맵핑
serverSocket.bind((host, port))
# 맵핑된 소켓을 연결 요청 대기 상태로 전환
serverSocket.listen(1)
print("대기중")


# 실제 소켓 연결 시 반환되는 실제 통신용으로 연결된 소켓과 연결주소 할당
connectionSocket, addr = serverSocket.accept()

# 연결
print(str(addr), "에서 접속되었습니다. ")

# 데이터 수신, 최대 1024
data = connectionSocket.recv(1024)
print("받은 데이터: ", data.decode("utf-8"))

# 데이터 송신
connectionSocket.send("I'm a server".encode("utf-8"))
print("send message")

# 서버 닫기
serverSocket.close()
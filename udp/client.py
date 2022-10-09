from socket import *

# socket 모듈: 파이썬에서 모든 네트워크 통신의 기본 구성
# 아래의 아린을 포함함으로써 프로그램내 소켓 생성가능
serverName = "127.0.0.1"
serverPort = 1234

# 클라이언트 소켓 생성 (주소군, UDP 소켓)
clientSocket = socket(AF_INET, SOCK_DGRAM)
# 소켓 생성 시 클라이언트 소켓의 포트 번호 명시 필요 없음, 운영체제가 대신 함

message = input("input lowercase sentence: ")
# raw_input : 클라이언트 쪽의 사용자아게 괄호의 프롬프트 나타남

clientSocket.sendto(message.encode(), (serverName, serverPort))
# 소켓을 바이트 형태로 보이기 위해 encode() 메소드 사용해 문자열 타입의 메시지를 바이트 타입으로 변환
# sendto(): 메소드를 목적지 주소(serverName, serverPort)를 메시지에 붙이고 해당 패킷을 프로세스의 소켓인 clientSocket으로 보냄

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
# 패킷이 클라이언트의 소켓에 인터넷으로부터 도착하면 패킷 데이터는 변수 modifiedMessage에 할당됨
# 패킷 소스 주소 변수는 변수 serverAddress에 할당됨
# 변수 serverAddress는 서버의 IP주소와 서버의 포트번호를 포함함
# UDPClient 프로그램은 처음부터 서버 주소 알고 있어서 실제로 이 서버 주소 정보를 필요로 하지 않음

print(modifiedMessage.decode())

# 소켓 닫음
clientSocket.close()

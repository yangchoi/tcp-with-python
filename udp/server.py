from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverPort = 1234

# 위 라인 포트번호를 서버 소켓에 할당(bind)
# UDPServer의 코드는 명시적으로 포트번호를 소켓에 할당함
# 서버 IP 주소의 1234 포트로 패킷을 보내면 해당 소켓으로 패킷이 전달됨(directed)
serverSocket.bind(("", serverPort))

print("The server is ready to receive")

# 클라이언트로부터 계속해서 패킷을 수신하고 처리할 수 있도록 루프
while True:
    # UDPServer 패킷 도착하길 기다림
    # 패킷 데이터는 변수 message에 할당되고 패킷의 소스 주소는 변수 clientAddress에 할당됨
    # 변수 clientAddress 클라이언트 IP주소와 클라이언트의 포트 번호를 포함
    message, clientAddress = serverSocket.recvfrom(2048)
    # UDPServer는 일반 우편에서의 반송주소와 마찬가지로 반송주소 제공해야할 때 본 주소 정보 사용함
    # 클라이언트로부터 받은 메시지를 대문자로 변환해서 반송
    modifiedmessage = message.decode().upper()

    # 클라이언트 주소를 대문자로 변환된 메시지에 붙이고 그 결과로 만들어진 패킷을 서버의 소켓으로 보냄
    serverSocket.sendto(modifiedmessage.encode(), clientAddress)

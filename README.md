# tcp-with-python

### 순서

1. 서버세엇 리스닝 소켓 생성
2. 서버와 클라이언트 연결
3. 클라이언트가 데이터 전송, 서버가 데이터 수신
4. 서버가 데이터 전송, 클라이언트가 데이터 수신
5. 클라이언트가 연결 종료 메시지 전송

### Server socket

- socket(AT_INET, SOCK_STREAM): 소켓 객체 생성
- socket.bind(address): 생성한 소켓을 서버 IP 및 포트를 튜플형태로 맵핑
- socket.listen(): 연결 요청 대기 상태 설정
- socket.accept(): 연결 승낙 후 실제 통신 소켓 반환
- socket.send(byte) or socket.sendall(byte): 데이터 송신
- socket.recv(bufsize): 데이터 수신, bufsize는 한번에 수신되는 데이터 크기
- socket.close(): 연결 종료

### Client socket

- socket.connect(address): 서버 소켓에 연결요청. 인자로 address를 튜플형태로 받음
- socket.send(byte) or socket.sendall(byte): 데이터 송신
- socket.recv(bufsize): 데이터 수신. bufsize는 한번에 수신되는 데이터 크기

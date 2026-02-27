from socket import socket, AF_INET, SOCK_STREAM

server_socket=socket(AF_INET,SOCK_STREAM)
ip='127.0.0.1'
port=8888
server_socket.bind((ip,port))

server_socket.listen(5)
print('服务器已启动')

client_socket,client_addr=server_socket.accept()

data=client_socket.recv(1024)
print('客户端发送过来的数据为：',data.decode('utf-8'))

server_socket.close()

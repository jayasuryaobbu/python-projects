import socket

tcp_ip = '<ip4 address>'
tcp_port = 55000
buffer_size = 1024
message = b'hello! Test'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((tcp_ip, tcp_port))
s.send(message)
data = s.recv(buffer_size)
s.close()

print(data)


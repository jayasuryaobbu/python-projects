import socket

tcp_ip = '<ip4 address>'
tcp_port = 55000
buffer_size = 20

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((tcp_ip, tcp_port))
s.listen(1)

conn, addr = s.accept()

print(addr)

while 1:
    data = conn.recv(buffer_size)
    if not data: break
    print(data)
    conn.send(data)
conn.close()

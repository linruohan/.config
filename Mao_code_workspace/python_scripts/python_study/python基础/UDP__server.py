import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',8888))
print('Bind  UDP on 8888...')
while True:
    #接受数据
    data,addr=s.recvfrom(1024)
    print('Received from %s:%s' %(data,addr))
    s.sendto(b'hello,%s.'%data,addr)

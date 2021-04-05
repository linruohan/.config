import socket
import threading,time
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',9999))
s.listen(5)
print('waiting for connecting...')


def tcplink(sock,addr):
    print('accept new connecting from %s:%s...' %(sock,addr))
    sock.send(b'Welcome!')
    while True:
        data=sock.recv(1024)
        time.sleep(4)
        if not data or data.decode('utf-8')=='exit':
            break
        sock.send(('hello,%s.'%data.decode('utf-8')).encode('utf_8'))
    sock.close()
    print('connecting from %s closed.' %(addr))

while True:
    sock,addr=s.accept()
    t=threading.Thread(target=tcplink,args=(sock,addr))
    t.start()

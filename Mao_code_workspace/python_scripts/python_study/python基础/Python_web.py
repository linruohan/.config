import socket

def run(host='',post=3000):#主机和端口
    #c创建一个socket对象
    #s=socket.socket()
    with socket.socket() as s:
        s.bind(host,port)#绑定主机和端口
        while True:
            #监听客户端浏览器的请求，每3秒
            s.listen(3)
            connection=s.accept()#接收

import  hashlib

md5=hashlib.md5()
md51=hashlib.md5()
md5.update('how to use md5 in python hashlib'.encode('utf-8'))
md51.update('hi ?how to use md5 in python hashlib'.encode('utf-8'))
print(md5.hexdigest())
print(md51.hexdigest())


sha1=hashlib.sha1()
sha1.update('how to use md5 in python hashlib'.encode('utf-8'))
print(sha1.hexdigest())

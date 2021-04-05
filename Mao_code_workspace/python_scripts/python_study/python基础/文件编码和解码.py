#coding=utf-8
#编码
s=str('hello world').encode('utf-8')
f=open('1.txt','w')
f.write(s)
f.close()
#解码
f=open('1.txt','r')
r=f.read().decode('utf-8')
f.close()
print('asd')

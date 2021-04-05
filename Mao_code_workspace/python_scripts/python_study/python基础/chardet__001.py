import chardet

s=chardet.detect(b'Hello,World!')
print(s)
data='离离原上草，一岁一哭荣'.encode('utf-8')

print(chardet.detect(data))

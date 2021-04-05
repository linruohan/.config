#-*- coding:utf8 -*-
from PIL import Image
import os
im = Image.open(os.path.dirname(__file__)+"/captcha.gif")
#(将图片转换为8位像素模式)
im.convert("P")
im2=Image.new("P",im.size,255)
his=im.histogram()
values={}

# for i in range(256):
#     values[i]=his[i]
# for j,k in sorted(values.items(),key=lambda x:x[1],reverse=True)[:10]:
#     print( j,k)

# #打印颜色直方图
# print (im.histogram())
for x in range(im.size[1]):
    for y in range(im.size[0]):
        pix=im.getpixel((y,x))
        if pix==220 or pix==227:
            im2.putpixel((y,x),0)#添加到新的图片上
# im2.show()

# 提取单个字符图片
inletter=False
foundletter=False
start=0
end=0

letters=[]
#进行纵向切割
for y in range(im2.size[0]):
    for x in range(im2.size[1]):
        pix=im2.getpixel((y,x))
        if pix!=255:
            inletter=True
    if foundletter==False and inletter==True:
        foundletter=True
        start=y
    if foundletter==True and inletter==False:
        foundletter=False
        end=y
        letters.append((start,end))
    inletter=False
# print(letters)#得到每个字符开始和结束的列序号


# 对图片进行切割，得到每个字符所在的那部分图片
import hashlib
import time
count=0
for letter in letters:
    m=hashlib.md5()
    im3=im2.crop((letter[0],0,letter[1],im2.size[1]))
    m.update(("%s%s"%(time.time(),count)).encode())
    im3.save(os.path.dirname(__file__)+"/%s.gif"%(m.hexdigest()))
    count+=1

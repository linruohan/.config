# -- coding: utf-8 --
from PIL import Image
import argparse

WIDTH = 90
HEIGHT = 45
#我的电脑是15寸,分辨率1920*1080,记事本全屏状态下比较合适的初始宽度和高度,可以根据自己的屏幕自行调整

ascii_char = list("@#&$*ox!i;.")#用于输出字符画的字符串,已经大致按灰度从高到低排好,原文采用70个字符,但是灰度排序度差,效果不好

# 将256灰度映射到字符上
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '#透明度为0则没有图片
    length = len(ascii_char)
    gray = int(0.299 * r + 0.578 * g + 0.114 * b)#计算灰度值的公式

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]#按灰度值映射到字符串中的字符

if __name__ == '__main__':

    im = Image.open(os.path.dirname(__file__)+'/wm.png')#读入图片
    scale = int(max(im.size[0] / WIDTH, im.size[1] / HEIGHT))#用于缩放的比例
    WIDTH = int(im.size[0] / scale * 2)#因为字符的宽和高是不相等的,所以用两倍宽,大致与高相等了
    HEIGHT = int(im.size[1] / scale)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)#将原图的尺寸按比例缩放

    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))#读取(j,i)像素点的r,g,b,alpha值用于计算灰度
        txt += '\n'#打印完一行后换行

    #字符画输出到文件
    with open(os.path.dirname(__file__)+"output.txt",'w') as f:
        f.write(txt)

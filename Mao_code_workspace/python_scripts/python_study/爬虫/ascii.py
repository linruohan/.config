from PIL import Image
'''failed'''
# import argparse#用来管理命令行参数输入
#命令行输入参数处理：
# parser=argparse.ArgumentParser()

# parser.add_argument('file')#输入文件
# parser.add_argument('-o','--output')#输出文件
# parser.add_argument('--width',type=int,default=80)#设置输出自负画的宽度
# parser.add_argument('--height',type=int,default=80)#设置字符画高
#
# #获取参数
args=parser.parse_args()
IMG=args.file
WIDTH=args.width
HEIGHT=args.height
OUTPUT=args.output

#字符画使用的字符集，一共70个
ascii_char=list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
# RGB值转字符的函数，将256灰度映射到70个字符上
def get_char(r,g,b,alpha=256):
    """
    Docstring for get_char
    """
    if alpha==0:
        return ' '
    length=len(ascii_char)
    gray=int(0.2126*r+0.7152*g+b)
    # print('gray-=',gray)
    unit=(256.0+1)/length
    # print('unit-=',unit)
    s=ascii_char[int(gray/unit)]
    # print("chushu==",int(gray/unit))
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    # im=Image.open(IMG)
    # im=im.resize((WIDTH,HEIGHT),Image.NEAREST)
    # txt=""
    im=Image.open('D:\\atom\\test\\ascii_test\\wm.png')
    im=im.resize((80,80),Image.NEAREST)
    # print(im.size)
    # print(im)
    txt=""
    print(get_char(*im.getpixel((10,10))))
    # for i in range(80):
    #     for j in range(80):
    #         txt+=get_char(*im.getpixel((j,i)))
    #     txt+='\n'
    print(txt)

    #字符画输出到文件
    if OUTPUT:
        with open("output.txt",'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)

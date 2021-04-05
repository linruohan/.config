import os,sys
from PIL import Image
class character():
    def __init__(self,file1,width,height,output):
        self.IMG = file1
        self.WIDTH = width
        self.HEIGHT = height
        self.OUTPUT = output
        # 不同字符代表不同色块，字符最好不要重复
        self.ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
        self.txt = ''

        # 将256灰度映射到70个字符上
        # 图片格式为RGB的*im.getpixel((j,i)后会得到三个参数r（red），g（green），b（blue）；RGBA得到四个参数r，g，b，alpha(透明度，0表示完全透明)
        # im.getpixel((j,i))得到一个由r, g, b, alpha(如果有的话)构成的元祖，加上*号即表示拆分元祖分别赋值引用
    def get_char(self, r, g, b, alpha = 256):
        # 如果是透明的，则输出空格
        if alpha == 0:
                return ' '
        length = len(self.ascii_char)
        # r,g,b转换为灰度值，白色是255，黑色是0
        gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
        # 单元字符的灰度值大小
        unit = (256.0 + 1)/length
        # 字符从小到大表示灰度值，已知灰度值大小，一个字符表示的灰度值大小，求该灰度值由第几个字符表示，ascii_char[i]
        return self.ascii_char[int(gray/unit)]

    def convert(self):
        im = Image.open(self.IMG)
        # im.resize(size,filter)
        # 变量filter为NEAREST、BILINEAR、BICUBIC或者ANTIALIAS之一
        # 如果忽略，或者图像模式为“1”或者“P”，该变量设置为NEAREST，速度快
        # ANTIALIAS 抗锯齿，质量最高；BICUBIC 三次样条插；BILINEAR 线性插值法
        im = im.resize((self.WIDTH,self.HEIGHT), Image.NEAREST)
        for i in range(self.HEIGHT):
            for j in range(self.WIDTH):
                self.txt += self.get_char(*im.getpixel((j,i)))
            self.txt += '\n'
    def save(self):
        if self.OUTPUT:
            with open(self.OUTPUT,'w') as f:
                f.write(self.txt)
        else:
            with open("output.txt",'w') as f:
                f.write(self.txt)
    def start(self):
        self.convert();
        self.save();

if __name__ == '__main__':
    path=os.path.dirname(__file__)
    file1=path+'/wm.png'
    width=300
    height=100
    output=path+'/out.txt'
    # (file1,width,height,output)
    c = character(file1,width,height,output)
    c.start()

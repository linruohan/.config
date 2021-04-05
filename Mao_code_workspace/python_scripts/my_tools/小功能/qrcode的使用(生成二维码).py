from PIL import Image
import qrcode
# 最小尺寸 1 会生成 21 * 21 的二维码，version 每增加 1，生成的二维码就会添加 4 尺寸
# 参数 error_correction 指定二维码的容错系数，分别有以下4个系数：
#ERROR_CORRECT_L: 7%的字码可被容错
#ERROR_CORRECT_M: 15%的字码可被容错
#ERROR_CORRECT_Q: 25%的字码可被容错
#ERROR_CORRECT_H: 30%的字码可被容错
# 参数 box_size 表示二维码里每个格子的像素大小
# 参数 border 表示边框的格子厚度是多少（默认是4）
qr = qrcode.QRCode(version=3, box_size=10, border=0,
                   error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data('这里是二维码的内容')
qr.make(fit=True)
img = qr.make_image()
img = img.convert('RGBA')
icon = Image.open('1.jpg')
icon = icon.convert('RGBA')
w, h = img.size
factor = 4
size_w = int(w/factor)
size_h = int(h/factor)
icon_w, icon_h = icon.size
if icon_w > size_w:
    icon_w = size_w
if icon_h > size_h:
    icon_h = size_h
icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
w = int((w-icon_w)/2)
h = int((h-icon_h)/2)
img.paste(icon, (w, h), icon)
img.save(u'二维码.PNG', quality=100)

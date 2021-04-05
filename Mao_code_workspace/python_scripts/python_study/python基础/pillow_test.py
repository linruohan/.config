from PIL import Image,ImageFilter#模糊


im=Image.open('1.jpg')
#获得图像尺寸
w,h=im.size
print('original image size:%s%s'%(w,h))
im.thumbnail((w//2,h//2))
print('Resize image to:%s%s'%(w//2,h//2))
#保存缩放后的图像用jpeg保存
im.save('111.jpg','jpeg')
im2=im.filter(ImageFilter.BLUR)
im.save('blur222.jpg','jpeg')

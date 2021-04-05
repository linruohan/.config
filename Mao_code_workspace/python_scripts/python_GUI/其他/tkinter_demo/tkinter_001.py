from  tkinter  import *



from PIL import Image,ImageTk
import tkinter as tk

# 简单插入显示
def show_jpg():
    root = tk.Tk()
    im=Image.open("1.jpg")
    img=ImageTk.PhotoImage(im)
    imLabel=tk.Label(root,image=img).pack()
    root.mainloop()

if __name__ == '__main__':
    # show_jpg()
    root=Tk()

    photo = ImageTk.PhotoImage(file="1.bmp")
    textLabel=Label(
        root,# 将内容绑定在  root 初始框上面
        text='你是一个大笨蛋！',
        image=photo,
        compound=CENTER,
        font=('楷体',20),
        fg='white',
        justify=LEFT,# 用于 指明文本的 位置
        # padx=10,#   限制 文本的 位置 , padx 是 x轴的意思
        )
    textLabel.pack(side=LEFT)# 定义 textlabel 在初识框 中的位置
    # imglabel=Label(root,image=photo)
    # imglabel.pack(side=RIGHT)

    mainloop()

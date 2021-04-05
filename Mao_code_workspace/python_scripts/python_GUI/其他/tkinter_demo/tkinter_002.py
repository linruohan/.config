from tkinter import *
from PIL import Image,ImageTk
import easygui
def callback():
    easygui.msgbox('你这样让我很不爽',title='你说呢?')
    var.set('what are you looking?')

root=Tk()
#
frame1=Frame(root)
frame2=Frame(root)

var=StringVar()
# var.set('现在看到的内容为错误信息，\n您确认继续查看吗？')
# textlable=Label(frame1,textvariable=var,justify=LEFT).pack(side=LEFT)
#
# photo=ImageTk.PhotoImage(file='1.jpg')
# imagelabel=Label(frame1,image=photo).pack(side=RIGHT)
#
Button(frame2,text='确定了！',command=callback).grid(row=4,column=1)

#
root.title('皇上翻牌子啦!')    # 添加 初识框的标题 .
# GIRLS = ['西施','貂蝉','王昭君']         #  列表内容 .
# v = []  # 用于存放变量
#
# for girl in GIRLS:
#     v.append(IntVar())
#     print(IntVar())
#     b = Checkbutton(frame2,text=girl,variable=v[-1],padx=80,font=('楷体',22))
#     l = Label(root,textvariable=v[-1])
#     l.pack(anchor=N)
#     b.pack(anchor=W)      # 文本的位置 . (东西南北的首拼 (英文))
# b = Checkbutton(root,text='杨玉环',variable=v[1],padx=80,font=('楷体',22))
# l = Label(root,textvariable=v[1])
# l.pack(anchor=N)
# b.pack(anchor=W)
# v = IntVar()
#
# Radiobutton(frame1,text='One',variable=v,value=1).pack(anchor=W)
# Radiobutton(frame1,text='Two',variable=v,value=2).pack(anchor=W)
# Radiobutton(frame1,text='Three',variable=v,value=3).pack(anchor=W)  # value 的值不同  . 相同的值 在其中一个被选中之后剩余的也会自动选中 .
#
#
# group=LabelFrame(frame1,text='最好的编程语言是？').pack(padx=50)
# v.set(1)
# Language = [('Python',1),
#     ('ruby',2),
#     ('C++',3),
#     ('java',2)
#      ]
# for lang,num in Language:
#     b = Radiobutton(root,text=lang,variable=v,value=num,indicatoron=False,padx=30,pady=3)
#     l = Label(root,textvariable=v)
#     #l.pack()
#     b.pack(anchor=W,fill=X)
#
Button(frame2,text='just it',command=callback).grid(row=4,column=0)



Label(frame1,text='账号：').grid(row=0,column=0)
Label(frame1,text='密码：').grid(row=1,column=0)
v1=StringVar()
v2=StringVar()

e1=Entry(frame1,textvariable=v1)
e2=Entry(frame1,textvariable=v2,show='*')
e1.grid(row=0,column=1,padx=10,pady=5)
e2.grid(row=1,column=1,padx=10,pady=5)
def show():
    print('user:%s' % e1.get())
    print('user:%s' % e2.get())

Button(frame1,text='芝麻开门',width=10,command=show).grid(row=3,column=0,sticky=W,padx=10,pady=5)
Button(frame1,text='退出',width=10,command=root.quit()).grid(row=3,column=1,sticky=E,padx=10,pady=5)

























frame1.pack(padx=10,pady=10)
frame2.pack(padx=20,pady=10)


mainloop()

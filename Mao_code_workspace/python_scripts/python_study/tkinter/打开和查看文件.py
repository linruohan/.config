# coding=utf-8
from tkinter import *
from tkinter import messagebox as tkMessageBox
from tkinter import filedialog as tkFiledialog
import os
import fnmatch  # fnmatch是一种函数，功能是指定的模式来匹配文件名或字符串。定义和用法语法 fnmatch(pattern,string,flags) 参数 描述 pattern 必需。


def search():
    text = entry_1.get()  # 取值
    if not text:
        tkMessageBox.showinfo('Error', '请输入关键字！')
        return
    fn = tkFiledialog.askdirectory()  # 选择文件夹
    fnlist = os.walk(fn)  # 列出目录
    # 对于os.walk的使用，产生一个可迭代的对象， 通常使用root,dirs,files来接收
    # root:文件路径   dirs：子文件夹名称   files:文件名
    for root, dirs, files in fnlist:
        for i in fnmatch.filter(files, entry_2.get()):
            filename = '%s/%s' % (root, i)
            listbox.insert(END, filename)


def click(event):
    index = listbox.curselection()
    path = listbox.get(index)
    if not path:
        return
    window = Tk()
    window.title('查看文件')
    text = Text(window, width=100)  # 多行文本框
    text.grid()
    fn_text = open(path, encoding='utf-8').read()
    text.insert(END, fn_text)


root = Tk()
root.title('第一个可视化窗口')
# root.geometry('300x200+1000+200') #可以使用缺省内容的方式，使窗口自动调节
root.geometry()
Label(root, text='关键字：').grid()
entry_1 = Entry(root)
entry_1.grid(row=0, column=1)
Label(root, text='文件类型：').grid(row=0, column=2)
entry_2 = Entry(root)
entry_2.grid(row=0, column=3)

button = Button(root, text='选择文件', command=search)
button.grid(row=0, column=4)

listbox = Listbox(root, width=80)
listbox.bind('<Double-Button-1>', click)
listbox.grid(row=1, column=0, columnspan=5)
root.mainloop()

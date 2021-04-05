#coding=utf-8
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import urllib.request
import requests

def upload():
    filename = filedialog.askopenfilename(title='选择文件')  # 选择文件
    r = requests.post('http://127.0.0.1:5000/upload', files={'file': open(filename, 'rb')})
    print(r.content.decode('utf-8'))
    settext = r.content.decode('utf-8')
    print(settext.__class__)
    entry.delete(0, END)
    entry.insert(0, filename)


def download():
    link = entry.get()
    files = requests.get(link)
    files.raise_for_status()
    path = filedialog.asksaveasfilename()
    print(files.content)
    with open(path, 'wb') as f:
        f.write(files.content)

root=Tk()#创建窗口
root.title('文件分享')
root.geometry('400x500+500+300')#窗口的大小+位置（x，y）


entry=Entry(root,width=40)#创建输入框
entry.grid(row=0,column=0)#显示窗口/布局



b1=Button(root,text='上传',command=upload).grid(row=1,column=0,pady=5)

b2=Button(root,text='下载',command=download).grid(row=2,column=0,pady=5)

mainloop()#显示窗口

# 举个栗子，添加输入框，将验证码图片打印出来
# coding= utf-8
from PIL import ImageTk
from tkinter import StringVar
import PIL
import tkinter as tk
import os
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


class GetCode(object):

    def __init__(self):

        self.data = {}  # 存放返回值
        self.root = tk.Tk()
        self.root.geometry('408x430')
        self.root.resizable(width=False, height=False)   # 固定长宽不可拉伸

        self.textLabel = tk.Label(self.root, text="请输入验证码：").pack()  # 标签

        self.textStr = StringVar()
        self.textEntry = tk.Entry(self.root, textvariable=self.textStr)

        self.textStr.set("")
        self.textEntry.pack()  # 输入框

        im = PIL.Image.open(os.path.dirname(__file__)+"/1.jpg")
        img = ImageTk.PhotoImage(im)
        imLabel = tk.Label(self.root, image=img).pack()  # 显示图片
        self.but = tk.Button(self.root, text="确认",
                             command=self.return_code).pack(fill="x")  # 按键
        self.root.mainloop()

    def return_code(self):
        # 返回输入框内容
        self.data["code"] = self.textStr.get()
        self.root.destroy()           # 关闭窗体
        # os.remove("1.jpg")         # 删除图片
        print("输入框内容：%s" % self.data["code"])


if __name__ == '__main__':
    GetCode()

import tkinter as tk
from tkinter import *


class Mywindow(tk.Frame):
    def __init__(self):
        self.on_hit = False  # 默认初始状态为 False
        self.window = tk.Tk()
        self.window.title('kais')
        # self.window.geometry('200x100')
        self.window.geometry()
        l = tk.Label(self.window,
                     text='OMG! this is TK!',  # 标签的文字
                     bg='green',  # 背景颜色
                     font=('Arial', 12),  # 字体和字体大小
                     width=15, height=2  # 标签长宽
                     )
        l.pack()  # 固定窗口位置
        self.var = tk.StringVar()  # 这时文字变量储存器
        l2 = tk.Label(self.window,
                      textvariable=self.var,  # 使用 textvariable 替换 text, 因为这个可以变化
                      bg='yellow', font=('Arial', 12), width=15, height=2)
        l2.pack()
        b = tk.Button(self.window, bg='red',
                      text='hit me',  # 显示在按钮上的文字
                      width=15, height=2,
                      command=self.hit_me)  # 点击按钮式执行的命令
        b.pack()  # 按钮位置
        b1 = tk.Button(self.window, text="insert point", width=4, height=2, command=self.insert_point)
        b1.pack()
        b2 = tk.Button(self.window, text="insert end", command=self.insert_end)
        b2.pack()
        self.e = tk.Entry(self.window, show='*')
        self.e.pack()  # 输入任何内容都为*

        self.t = tk.Text(self.window, height=2)
        self.t.pack()  # 文本框用于显示

    def hit_me(self):
        if self.on_hit == False:  # 从 False 状态变成 True 状态
            self.on_hit = True
            self.var.set('you hit me')  # 设置标签的文字为 'you hit me'
        else:  # 从 True 状态变成 False 状态
            self.on_hit = False
            self.var.set('')  # 设置 文字为空

    def insert_point(self):
        var = self.e.get()
        self.t.insert('insert', var)

    def insert_end(self):
        var = self.e.get()
        self.t.insert('end', var)


if __name__ == '__main__':
    s = Mywindow()
    s.window.mainloop()

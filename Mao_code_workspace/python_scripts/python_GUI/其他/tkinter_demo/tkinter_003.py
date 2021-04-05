from tkinter import *
import easygui,os,io,sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
root=Tk()

def test():
    if e1.get()=='小甲鱼':
        print('正确')
        return True
    else:
        print('错误')
        e1.delete(0,END)
        return False

v=StringVar()
e1=Entry(root,textvariable=v,validate='focusout',validatecommand=test) # validate 用于指定什么时候检测 . validatecommand 用于指定检测的标准
e2=Entry(root)
e1.pack(padx=20,pady=10)
e2.pack(padx=20,pady=10)

mainloop()

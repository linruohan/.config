from tkinter import *
import easygui,os,io,sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

'''滚动条'''
root=Tk()
root.title('开始')

#
# sb=Scrollbar(root)
# sb.pack(side=RIGHT,fill=Y)#需要先 将滚动条放置 到一个合适的位置 , 然后开始填充
# lb=Listbox(root,yscrollcommand=sb.set)# 内容 控制滚动条
# for i in range(1,2):
#     lb.insert(END,i)

# lb.pack(side=LEFT,fill=BOTH)
# sb.config(command=lb.yview)# 滑轮控制内容 .
# tickinterval 是设置的 标尺 多少长度有一个可读 ,
# resolution设置的是 一次跳跃的 长度 . length 是设置长度 .
s1=Scale(root,from_=0,to=100,tickinterval=5,resolution=2,length=100)
s1.pack()
# roient 默认的是 x 轴  , 让roient = HORIZONTAL 设置Y 轴 尺度 .

s2 = Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=5,length=400,resolution=2)
s2.pack()


def locate():
    print('X轴速度'+str(s1.get()))
    print('Y轴速度'+str(s2.get()))
Button(root,text='获取位置',command=locate).pack()













mainloop()

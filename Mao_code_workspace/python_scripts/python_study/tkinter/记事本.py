# coding=utf-8
from tkinter import *
import tkinter.filedialog as filedialog

class Mynotebook:
    def __init__(self):
        # 窗口
        self.root = Tk()
        self.root.title('未命名 - 记事本')
        # print(self.root.wm_title())#窗口标题
        self.root.geometry('800x600+500+300')
        self.root.iconbitmap('3.ico')
        # 菜单
        me = self.mainMenu()
        filemenu = self.fileMenu(me)  # 二级菜单
        me.add_cascade(label='文件', menu=filemenu)  # 一级菜单
        me.add_cascade(label='编辑', menu=filemenu)  # 一级菜单
        me.add_cascade(label='格式', menu=filemenu)  # 一级菜单
        me.add_cascade(label='查看', menu=filemenu)  # 一级菜单
        me.add_cascade(label='帮助', menu=filemenu)  # 一级菜单

        # 编辑区
        self.text = Text(bg='#C1FFC1',font=('Consolas',16))
        self.text.pack(expand=YES, fill=BOTH)
        #激活窗口
        self.root.mainloop()
    def mainMenu(self):
        me = Menu()
        self.root.config(menu=me)
        return me
    def fileMenu(self,mainMenu):
        filemenu = Menu(mainMenu)  # 二级菜单
        filemenu.add_command(label='新建', accelerator='Ctrl + N', command=self.createfile)
        filemenu.add_command(label='打开', accelerator='Ctrl + O', command=self.openfile)
        filemenu.add_command(label='保存', accelerator='Ctrl + S', command=self.savefile)
        filemenu.add_command(label='另存为', accelerator='Ctrl + Shift + N', command=self.saveas)
        filemenu.add_separator()  # 分割线
        filemenu.add_command(label='页面设置', accelerator='Ctrl + Shift + T', command=self.pagesetting)
        filemenu.add_command(label='打印', accelerator='Ctrl + Shift + P', command=self.fileprint)
        filemenu.add_command(label='退出', accelerator='Ctrl + Q', command=self.root.quit)
        return filemenu
    def createfile(self):
        txt=self.text.get(1.0,END)
        if not txt:return
        self.savefile()
    def openfile(self):
        filename = filedialog.askopenfilename(title='打开文件', filetypes=[('文本文档', '*txt'), ('python文件', '*.py')])
        if not filename: return
        txt = open(filename, encoding='utf-8').read()
        self.text.insert(1.0, txt)
        self.root.title(u'%s - 记事本' % filename.split('/')[-1])
    def savefile(self):
        filename = filedialog.asksaveasfilename(title='保存为...', initialfile='未命名.txt',
                                                filetypes=[('文本文档', '*txt'), ('python文件', '*.py')],
                                                defaultextension='.txt')
        # print(filename)
        if not filename: return
        f = open(filename, 'w', encoding='utf-8')
        f.write(self.text.get(1.0, END))
        f.close()
        self.text.delete(1.0, END)
        self.root.title(u'%s - 记事本' % filename.split('/')[-1])
    def saveas(self):
        initialfile=(self.root.wm_title()).split(' - 记事本')[0]#默认保存文件名字
        filename = filedialog.asksaveasfilename(title='另存为...', initialfile=initialfile,
                                                filetypes=[('文本文档', '*txt'), ('python文件', '*.py')],
                                                defaultextension='.txt')
        # print(filename)
        if not filename: return
        f = open(filename, 'w', encoding='utf-8')
        f.write(self.text.get(1.0, END))
        f.close()
        self.text.delete(1.0, END)
        self.root.title(u'%s - 记事本' % filename.split('/')[-1])

    def pagesetting(self):
        pass
    def fileprint(self):
        pass

if __name__ == '__main__':
    Mynotebook()
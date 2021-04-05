# coding:utf-8
import easygui as g
import io
import sys
import os

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


class EasyGuiDemo:
    """easy gui demo"""
    def __init__(self):
        pass

    def title(self):
        title = g.msgbox(msg='提示信息', title='标题部分', ok_button="OK")

    def msg(self):
        msg = g.msgbox('Hello Easy GUI', '标题')  # 返回ok
        # print ('返回值：' + msg)

    def ccbox(self):
        # 确认和取消，返回true或者false
        ccbox = g.ccbox("here isccbox Continue | Cancel Box!")
        print('返回值：' + str(ccbox))

    def ynbox(self):
        ynbox = g.ynbox("Yes Or No Button Box!")  # 是和否，返回true或者false
        print('返回值： ' + str(ynbox))

    def choice(self):
        # 2、choice,多选框
        choice = g.buttonbox("这里是提示的语句信息：\n", title='三选一',
                             choices=['one', 'two', 'three', 'sd'])
        g.msgbox('您选择了：' + str(choice))

    def indexbox(self):
        g.indexbox(msg='Shall I continue?', title=' ',
                   choices=('Yes', 'No'), image=None)
        # 区别就是当用户选择第一个按钮的时候返回序号 0， 选择第二个按钮的时候返回序号 1。

        # 当你调用一个 buttonbox 函数（例如 msgbox(), ynbox(), indexbox() 等等）的时候，
        # 你还可以为关键字参数 image 赋值，这是设置一个 .gif 格式的图像（注意仅支持 GIF 格式哦）：

    def boolbox(self):
        # 3、choices 内只能有两个参数 ，选择哪一个将返回1，否则返回0
        bool = g.boolbox('msg提示信息', title='标题部分', choices=['是', '否'])
        g.msgbox(bool)

    def image(self):
        # 4/image
        image = os.path.dirname(__file__) + '/000.jpg'
        msg = 'Here is my photo,a python fan also'
        choices = ['Yes', 'No', "Not Sure"]
        title = 'Am I handsome?'
        g.buttonbox(msg, title, image=image, choices=choices)

    def list(self):
        # 5/list
        msg = '选择此列表项中你喜欢的一个吧'
        title = '必须选择一个哦'
        choices = ['1', '2', '3', '4', '5', '6', '7']
        answer = g.choicebox(msg, title, choices)
        print('你选择了 ：' + str(answer))

    def enterbox(self):
        # 6/enterbox
        st = g.enterbox("请输入一段文字：\n")
        print("您输入了：  " + str(st))

    def multilchoicebox(self):
        # 7/ mutilchoicebox多选框
        msg = '选择此列表项中你喜欢的一个吧'
        title = '必须选择一个哦'
        choices = (1, 2, 3, 4, 5, 6, 7, 8, 9)
        answer1 = g.multchoicebox(msg, title, choices)
        print(answer1)
        for item in answer1:
            print(item)

    def limit_box(self):
        # 8 输入限制条件的数字
        msg = '请输入一个数字，范围在0-100'
        title = '限制为数字类型'
        lowerbound = 0
        upperbound = 100
        default = '12'
        image = os.path.dirname(__file__) + '/001.gif'
        result = g.integerbox(msg, title, default,
                              lowerbound, upperbound, image)
        print(result)

    def multenterbox(self):
        # g.multenterbox(msg='Fill in values for the fields.', title=' ', fields=([list]), values=())
        list1 = ['用户名:', '密码:']
        g.multpasswordbox(msg='请输入用户名和密码', title='登录', fields=(list1))
        # multenterbox()
        # 为用户提供多个简单的输入框，要注意以下几点：
        # 如果用户输入的值比选项少的话，则返回列表中的值用空字符串填充用户为输入的选项。
        # 如果用户输入的值比选项多的话，则返回的列表中的值将截断为选项的数量。
        # 如果用户取消操作，则返回域中的列表的值或者None值。
        g.passwordbox(msg='Enter your password.', title=' ',
                      default='', image=None, root=None)
        # passwordbox() 跟 enterbox() 样式一样，不同的是用户输入的内容用"*"显示出来，返回用户输入的字符串：

    def textbox(self):
        # 9 textbox,codebox,大文本
        g.textbox(msg='', title=' ', text='', codebox=0)
        g.textbox(text=open('E:\\新建文本文档.txt', 'r'))
        # testbox() 函数默认会以比例字体（参数 codebox=1 设置为等宽字体）来显示文本内容（会自动换行哦），这个函数适合用于显示一般的书面文字。
        # 注：text 参数（第三个参数）可以是字符串类型，列表类型，或者元祖类型。
        g.textbox(text=open('E:\\新建文本文档.txt', 'r'))

    def codenpx(self):
        msg = '大文本的支持'
        title = 'Text Code'
        text = 'abcdefghijklmnopqrstuvwxyzABCDEFGHJIKLMNOPQRSTUVWXYZ0123456789-/'
        textContent = g.textbox(msg, title, text)
        codeContent = g.codebox(msg, title, )
        print(textContent)
        print(codeContent)

    def diropenbox(self):
        # 单个打开文件  选择Cancel的话返回值默认为None
        msg = '选择一个文件，将会返回该文件的完整的目录哦'
        title = ' 文件选择对话框'
        default = r'F:\flappy-bird'
        full_file_path = g.diropenbox(msg, title, default)
        print('选择的文件的完整的路径为：' + str(full_file_path))

    def fileopenbox(self):
        # 打开多个*。py类型的文件
        msg = '返回选择的文件的完整的路径，选择Cancel则返回None'
        title = '文件选择器'
        default = 'E:/Code/Python/MyTestSet/easygui/*.py'
        g.fileopenbox(msg=None, title=None, default='*', filetypes=None)
        # 关于 filetypes 参数的设置方法：
        # 可以是包含文件掩码的字符串列表，例如：filetypes = ["*.txt"]
        # 可以是字符串列表，列表的最后一项字符串是文件类型的描述，例如：
        # filetypes = ["*.css", ["*.htm", "*.html", "HTML files"]]
        opened_files = g.fileopenbox(msg, title, default, multiple=True)
        for item in opened_files:
            print(item)

    def filesavebox(self):
        msg = 'Save your file'
        title = "to Save File"
        default = 'E:/Code/Python/MyTestSet/easygui/newFile.*'
        savedfile = g.filesavebox(msg, title, default)
        print(savedfile)
        print('当然了，这里仅仅是一个完整的路径加上文件名而已，并不会真的保存成一个文件，保存文件需要用到其他的库')

    def exceptionbox(self):
        try:
            int('Exception')
        except:
            g.exceptionbox('int类型数据转换错误！请检查您的数据类型！')
        #   会弹出一个界面，内容信息可以自己定义，如上面。下面的内容就是追踪到的出错信息
        # Traceback (most recent call last):
        #   File "E:/Code/Python/MyTestSet/easygui_/exceptionbox.py", line 10, in <module>
        #     int('Exception')
        # ValueError: invalid literal for int() with base 10: 'Exception'

    def remeberSettings(self):
        # 15. 记住用户的设置
        # 15.1 EgStore
        # GUI 编程中一个常见的场景就是要求用户设置一下参数，然后保存下来，以便下次用户使用你的程序的时候可以记住他的设置。
        # 为了实现对用户的设置进行存储和恢复这一过程，EasyGui 提供了一个叫做 EgStore 的类。为了记住某些设置，你的应用程序必须定义一个类（暂时称之为"设置"类，尽管你随意地使用你想要的名称设置它）继承自 EgStore 类。
        # 然后你的应用程序必须创建一个该类的对象（暂时称之为"设置"对象）。
        # 设置类的构造函数（__init__ 方法）必须初始化所有的你想要它所记住的那些值。
        # 一旦你这样做了，你就可以在"设置"对象中通过设定值去实例化变量，从而很简单地记住设置。之后使用 settings.store() 方法在硬盘上持久化设置对象。
        # 下面是创建一个"设置"类的例子：
        class Settings(g.EgStore):
            def __init__(self, filename):
                self.userId = ""
                self.targetServer = ""
                self.filename = filename  # this is required
                self.restore()

        settingsFilename = os.path.dirname(
            __file__) + "/settings.txt"  # Windows example
        settings = Settings(settingsFilename)
        settings.userId = "奥巴马"
        settings.targetServer = "白宫"
        settings.store()  # persist the settings
        settings.userId = "小甲鱼"
        settings.store()
        print(settings.targetServer)

# 如何使用Python自动控制windows桌面
import win32gui
import win32api
import win32com
import win32con


class Ctrl_desktop:
    def __init__(self):
        self.operations = ["edit", "explore", "open", "find", "print", "NULL"]

    def operator(self, action='open'):
        win32api.ShellExecute(1, action, r'C:Program Files (x86)GoogleChromeApplicationchrome.exe', '', '', 1)
        win32api.ShellExecute(1, action, r'C:UsersJayDesktopEnvironment Guider.docx', '', '', 1)
        ret = win32api.ShellExecute(
            HWND=None,  # 指定父窗口句柄
            Operation=None,  # 指定动作， 譬如"edit",“explore”,“open”,“find”,“print”,“NULL”
            FileName=None,  # 指定要打开的文件或程序
            Parameters=None,  # 指定打开程序所需参数
            Directory=None,  # 缺省目录
            ShowCmd=None,  # 打开选项，可选值:
            SW_HIDE=0,  # ; {隐藏窗口，活动状态给令一个窗口}
            SW_SHOWNORMAL=1,  # ; {用最近的大小和位置显示窗口, 同时令其进入活动状态}
            SW_NORMAL=1,  # ; {用当前的大小和位置显示一个窗口，不改变活动窗口}
            SW_SHOWMINIMIZED=2,  # ; {最小化窗口，并将其激活}
            SW_SHOWMAXIMIZED=3,  # ; {最大化窗口，并将其激活}
            SW_MAXIMIZE=3,  # ; {同 SW_SHOWMAXIMIZED}
            SW_SHOWNOACTIVATE=4,  # ; {用最近的大小和位置显示一个窗口，不改变活动窗口}
            SW_SHOW=5,  # ; {用当前的大小和位置显示一个窗口，令其进入活动状态}
            SW_MINIMIZE=6,  # ; {最小化窗口, 不激活}
            SW_SHOWMINNOACTIVE=7,  # ; {同 SW_MINIMIZE}
            SW_SHOWNA=8,  # ; {用当前的大小和位置显示一个窗口，不改变活动窗口}
            SW_RESTORE=9,  # ; {同 SW_SHOWNORMAL}
            SW_SHOWDEFAULT=10,  # ; {同 SW_SHOWNORMAL}
            SW_MAX=10,  # ; {同 SW_SHOWNORMAL}
        )
        if ret <= 32:
            print("执行错误")
        elif ret == 0:
            print("0—— {内存不足}")
        elif ret == 2:
            print("2—— {文件名错误}")
        elif ret == 3:
            print("3—— {路径名错误}")
        elif ret == 11:
            print("11—— {EXE文件无效}")
        elif ret == 26:
            print("26—— {发生共享错误}")
        elif ret == 26:
            print("27—— {文件名不完全或无效}")
        elif ret == 28:
            print("28—— {超时}")
        elif ret == 29:
            print("29—— {DDE事务失败}")
        elif ret == 30:
            print("30—— {正在处理其他DDE事务而不能完成该DDE事务}")
        elif ret == 31:
            print("31—— {没有相关联的应用程序}")
        else:
            pass
        if ret > 32:     return ret

    def get_whd(self, name):
        # 2、查找窗体的句柄
        # 句柄是一个32位整数，在windows中用于标记对象。比如查找Snipping Tool和New  Text Document.txt的句柄，如下所示：
        para_hld = win32gui.FindWindow(None, "Snipping Tool")  # 1836416
        para_hld = win32gui.FindWindow(None, "New Text Document.txt - Notepad")  # 591410
        # win32gui.FindWindow()自顶层窗口（也就是桌面）开始搜索条件匹配的窗体，并返回这个窗体的句柄。该函数仅能查找主窗口，因此无法搜索子窗口，也不区分大小写，未找到则返回0。
        # 的参数主要包括(lpClassName=None, lpWindowName=None):
        # lpClassName：字符型，窗体的类名，可以在Spy + +里找到
        # lpWindowName：字符型，窗口名，也就是标题栏上能看见的那个标题。

    def get_title_name(self):
        # 3、查找句柄的类名和标题
        title = win32gui.GetWindowText(1836416)
        classname = win32gui.GetClassName(1836416)
        print("windows handler:{0}; title:{1}; classname:{2}".format(1836416, title, classname))
        # handler: 1836416;
        # title: SnippingTool;
        # classname: Microsoft - Windows - Tablet - SnipperToolbar
        title = win32gui.GetWindowText(591410)
        classname = win32gui.GetClassName(591410)
        print(
            "windows handler:{0}; title:{1}; classname:{2}".format(591410, title, classname))

    def getallwhd(self):
        # 4、调用win32gui.EnumWindows()枚举所有窗口句柄,直到最后一个顶层窗口被枚举则停止枚举过程。如下所示：
        hWndList = []
        win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWndList)
        print(hWndList)
        for hwnd in hWndList:
            title = win32gui.GetWindowText(hwnd)
            print(title)
            # [852802L, 65946L, 65928L, 65930L, 65900L, 65920L, 65924L, 65922L, 65944L, 65892L, 65886L, 6817870L, 65960L, 6031410L, …… 66052L, 65734L]

    def setFOreground(self, para_hld):
        # 5、win32gui.SetForegroundWindow()函数将指定窗体设置到最顶层，并且激活该窗口
        # 构造函数为：win32gui.SetWindowPos（HWNhWnd，HWNDhWndlnsertAfter, intX，intY, intcx，intcy, UNIT．Flags）
        # 关于win32gui.SetForegroundWindow(para_hld)
        # 因此调用SetForegroundWindow()时需要查看当前运行的条件是否符合上述要求，
        win32api.keybd_event(13, 0, 0, 0)  #
        win32gui.SetForegroundWindow(para_hld)

    def keyboard(self):
        # 6、win32api.keybd_event()
        # win32api.keybd_event(bVk, bScan, dwFlags, dwExtraInfo)
        # bVk：虚拟键码（键盘键码对照表见附录）；
        # bScan：硬件扫描码，一般设置为0即可；
        # dwFlags：函数操作的一个标志位，如果值为KEYEVENTF_EXTENDEDKEY则该键被按下，也可设置为0即可，如果值为KEYEVENTF_KEYUP则该按键被释放；
        # dwExtraInfo：定义与击键相关的附加的32位值，一般设置为0即可。
        # 按下enter键后抬起的例程如下所示：
        win32api.keybd_event(13, 0, 0, 0)  # enter
        win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键

    def mouse(self):
        # 7、模拟鼠标输入
        import time
        print(win32api.GetCursorPos())  # 获取鼠标当前位置的坐标
        win32api.SetCursorPos((100, 100))  # 将鼠标移动到坐标处
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 100, 100, 0, 0)  # 左点击
        time.sleep(2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 100, 100, 0, 0)

    def mouse_pyuserInput(self):pass
        # 8、关于鼠标键盘的操作还可以使用PyUserInput库
        # PyUserInput是一个使用python的跨平台的操作鼠标和键盘的模块，使用非常方便。支持的平台及依赖如下：
        # from pymouse import PyMouse
        # from pykeyboard import PyKeyboard
        # m = PyMouse()
        # k = PyKeyboard()
        # 操作鼠标和键盘，如下所示：
        # m.click(190, 70, 1)  # 移动并且在xy位置点击
        # time.sleep(2)
        # m.click(190, 200, 1)  # 移动并且在xy位置点击
        # time.sleep(2)
        # k.tap_key(k.function_keys[5])  # –点击功能键F5

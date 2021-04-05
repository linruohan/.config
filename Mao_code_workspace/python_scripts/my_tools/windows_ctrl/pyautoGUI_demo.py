import pyautogui

# PyAutoGUI模块控制鼠标和键盘实现自动化任务详解
# Python移动鼠标、点击键盘非常快，有可以导致其他应用出现问题。如果出现了问题，而鼠标还一直瞎晃，在这种情况下，你很难点击窗口退出程序。
# 1 pyautogui的暂停和Fail-Safe
# 2 fail - safe：当鼠标移动到屏幕的左上角时触法PyAutoGUI的FailSafeException异常。你可以使用try
# except语句处理异常，或直接让脚本异常退出。如果你想终止程序，只要你快速的把鼠标移动到屏幕左上角就可以了。
pyautogui.PAUSE = 1.5
pyautogui.FAILSAFE = True
import math


class PyautoGUi_demo:
    def __init__(self): pass

    def move(self, x, y):
        # 绝对移动
        width, height = pyautogui.size()  # 屏幕分辨率
        if x <= width and y <= height:
            pyautogui.moveTo(x, y, duration=0.25)

    def moverel(self, x, y):
        # 相对当前坐标移动
        pyautogui.moveRel(100, 0, duration=0.25)
        x, y = pyautogui.position()
    def drag(self,cur_x,cur_y):

        # 函数发送虚拟鼠标点击，默认情况下在鼠标所在的位置点击左键。函数原型：
        pyautogui.click(x=cur_x, y=cur_y, button='left')
        # x，y是要点击的位置，默认是鼠标当前位置
        # button是要点击的按键，有三个可选值：‘left', ‘middle',  ‘right'。
        # 点击右键
        pyautogui.click(button='right')
        # 点击左键：
        pyautogui.click(100, 100)
        pyautogui.mouseDown(100, 100)
        pyautogui.mouseUp(100, 100)
        # click函数完成了一次鼠标点击。一次完整的点击包括两部分，按下mouseDown() 和弹起mouseUp()。
        pyautogui.doubleClick()#：鼠标双击，其实就是执行两次click()
        pyautogui.rightClick()#：右击
        pyautogui.middleClick()#：中击
        # 鼠标拖拽
        pyautogui.dragTo(x,y)#：拖到
        pyautogui.dragRel()#：拖到

        # 拖拽的意思是：按下鼠标键并拖动鼠标。PyAutoGUI提供了两个函数：dragTo()和dragRel()
        # 注意：duration时间不能太短，拖动太快有些系统会吃不消。

        # 滚轮
        pyautogui.scroll()#：滚轮
        # 使用函数scroll()，它只接受一个整数。如果值为正往上滚，值为负往下滚。

        # 截屏：
        im = pyautogui.screenshot()#使用pyautogui截屏
        im.getpixel((50, 200))# 获得某个坐标的像素 # (30, 132, 153)
        pyautogui.pixelMatchesColor(50, 200, (30, 132, 153))# 判断屏幕坐标的像素是不是等于某个值

        pyautogui.locateOnScreen('button.png')# (643, 745, 70, 29)
        # locateOnScreen其实就是简单的颜色对比，如果有一个像素不匹配，它就会返回None。这个函数返回了匹配图形的坐标，找到中间点：

        x, y = pyautogui.center((643, 745, 70, 29))  # 获得中心点
        pyautogui.click(x, y)
        pyautogui.locateAllOnScreen()#：找到所有匹配的位置坐标。

    # 键盘按键
    def key(self):
        pyautogui.click(100, 100)
        pyautogui.typewrite('Hello world!')
        pyautogui.typewrite('Hello world!', 0.25)# 延时输入
        """
        PyAutoGUI键盘表：
        
        ‘enter' (或‘return'或 ‘\n')	回车
        ‘esc'	ESC键
        'shiftleft', ‘shiftright'左右SHIFT键
        ‘altleft', ‘altright'左右ALT键
        ‘ctrlleft', ‘ctrlright'左右CTRL键
        ‘tab' (‘\t')    TAB键
        ‘backspace', ‘delete'BACKSPACE 、DELETE键
        ‘pageup', ‘pagedown'PAGEUPPAGEDOWN键
        ‘home', ‘end'HOME和END键
        ‘up', ‘down', ‘left', ‘right'箭头键
        ‘f1', ‘f2', ‘f3'….	F1…….F12键
        ‘volumemute', ‘volumedown', ‘volumeup'	有些键盘没有
        ‘pause'	PAUSE键
        ‘capslock', ‘numlock', ‘scrolllock'	CAPS LOCK, NUM LOCK, 和 SCROLL LOCK 键
        ‘insert'	INS或INSERT键
        ‘printscreen'	PRTSC 或 PRINT SCREEN键
        ‘winleft', ‘winright'
        Win键‘command'	Mac OS X command键
        """

        pyautogui.click(100, 100)
        pyautogui.typewrite('Hello world!', 0.25)
        pyautogui.typewrite(['enter', 'a', 'b', 'left', 'left', 'X', 'Y'], '0.25')

        # 按键的按下和释放
        pyautogui.keyDown()#：按下某个键
        pyautogui.keyUp() #：松开某个键
        pyautogui.press() #：一次完整的击键，前面两个函数的组合。
        pyautogui.keyDown('altleft')
        pyautogui.press('f4')
        pyautogui.keyUp('altleft')
        pyautogui.hotkey('altleft', 'f4')

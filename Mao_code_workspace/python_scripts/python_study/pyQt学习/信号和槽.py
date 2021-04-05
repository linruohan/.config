import sys
from PyQt5.QtWidgets import (QWidget,QLabel,QLineEdit,QTextEdit, QPushButton,
    QHBoxLayout, QVBoxLayout,QLCDNumber,QMainWindow, QApplication,QGridLayout,QSlider)
from PyQt5.QtCore import Qt
'''PyQt5有着一套独特的信号和槽机制来处理事件.信号和槽用于在对象之间通信.
一个信号是在某特定事件发生时被发送的.一个槽可以是任何的Python调用.
一个槽当它连接的信号被发送的时候被调用.'''
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        lcd=QLCDNumber(self)#lcd数字显示框
        sld=QSlider(Qt.Horizontal,self)#水平滑动条

        #垂直布局
        vbox=QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        #整体布局
        self.setLayout(vbox)
        #连接滑动器上的valueChanged信号到lcd数字的display槽
        sld.valueChanged.connect(lcd.display)


        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()


    # 重载了keyPressEvent()事件处理器.
    # 按esc键退出
    def keyPressEvent(self,e):
        if e.key()==Qt.Key_Escape:
            self.close()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

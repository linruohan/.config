import sys
from PyQt5.QtWidgets import (QWidget,QLabel,QLineEdit,QTextEdit, QPushButton,
    QHBoxLayout, QVBoxLayout,QLCDNumber,QMainWindow, QApplication,QGridLayout,QSlider)
from PyQt5.QtCore import Qt
'''PyQt5有着一套独特的信号和槽机制来处理事件.信号和槽用于在对象之间通信.
一个信号是在某特定事件发生时被发送的.一个槽可以是任何的Python调用.
一个槽当它连接的信号被发送的时候被调用.'''
class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        btn1=QPushButton('button1',self)
        btn1.move(150,150)
        btn2=QPushButton('button2',self)
        btn2.move(100,10)
        #连接到相同的槽
        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()


        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()
    def buttonClicked(self):
        sender=self.sender()
        self.statusBar().showMessage(sender.text()+' was pressed.')

    # 重载了keyPressEvent()事件处理器.
    # 按esc键退出
    def keyPressEvent(self,e):
        if e.key()==Qt.Key_Escape:
            self.close()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

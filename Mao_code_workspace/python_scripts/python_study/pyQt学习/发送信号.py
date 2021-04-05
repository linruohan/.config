import sys
from PyQt5.QtWidgets import (QWidget,QLabel,QLineEdit,QTextEdit, QPushButton,
    QHBoxLayout, QVBoxLayout,QLCDNumber,QMainWindow, QApplication,QGridLayout,QSlider)
from PyQt5.QtCore import Qt,pyqtSignal,QObject


class Communicate(QObject):
    #创建信号，这个信号在鼠标被点击的时候被发送.
    #一个信号被创建,pyqtSignal()作为Communicate类的外部属性
    closeApp=pyqtSignal()


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        # 信号连接到QMainWindow的close()槽.
        self.c=Communicate()
        self.c.closeApp.connect(self.close)


        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Emit signal')
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

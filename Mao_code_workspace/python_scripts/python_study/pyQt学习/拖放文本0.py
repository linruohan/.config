import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Button(QPushButton):

    def __init__(self, title,parent):
        super().__init__(title,parent)
        self.setAcceptDrops(True)#让部件允许鼠标松开事件
    def dragEnterEvent(self,e):
        if e.mimeData().hasFormat('text/plain'):#告之我们所接受的数据类型.在这里是纯文本
            e.accept()
        else:
            e.ignore()

    def dropEvent(self,e):
        self.setText(e.mimeData().text())


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        edit=QLineEdit('',self)
        edit.setDragEnabled(True)
        edit.move(30,65)

        button=Button('anniu',self)
        button.move(190,65)


        self.setGeometry(200,300,300,150)
        self.setWindowTitle('drag and drop')
        self.show()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())

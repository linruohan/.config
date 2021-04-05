import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        #水平框
        hbox=QHBoxLayout(self)

        #图片框
        pixmap=QPixmap('1.jpg')
        #标签框
        lb1=QLabel(self)
        lb1.setPixmap(pixmap)#加载图片框

        hbox.addWidget(lb1)#加载标签框
        self.setLayout(hbox)#加载水平框



        self.setGeometry(200,300,300,150)
        self.setWindowTitle('QCheckBox')
        self.show()




if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())

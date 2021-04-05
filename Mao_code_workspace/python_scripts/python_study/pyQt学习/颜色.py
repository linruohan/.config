#coding=utf-8


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Font dialog')
        self.show()
    # 绘画事件
    def paintEvent(self,event):
        qp=QPainter()
        qp.begin(self)
        self.drawRectangle(qp)
    def drawRectangle(self,qp):
        col=QColor(0,0,0)
        col.setNamedColor('#d4d4dd')
        qp.setPen(col)

        qp.setBrush(QColor(200,0,0))
        qp.drawRect(10,15,90,60)

        qp.setBrush(QColor(255,80,0,160))
        qp.drawRect(130,15,90,60)

        qp.setBrush(QColor(25,0,90,200))
        qp.drawRect(250,15,90,60)








if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor,QPixmap
from PyQt5.QtCore import Qt

import sys
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 水平滑块
        sld=QSlider(Qt.Horizontal,self)
        sld.setFocusPolicy(Qt.NoFocus)#设置初始位置
        sld.setGeometry(30,40,100,30)
        sld.valueChanged[int].connect(self.changeValue)#绑定信号

        # 标签--设置初始图片
        self.label=QLabel(self)
        self.label.setPixmap(QPixmap('1.bmp'))
        self.label.setGeometry(560,540,80,30)



        self.setGeometry(300,300,380,370)
        self.setWindowTitle('toggle button')
        self.show()

    def setColor(self,pressed):
        source=self.sender()
        if pressed:
            print(source.text())
            val=255
        else:val=0
        if source.text()=='red':
            self.col.setRed(val)
        elif source.text()=='green':
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)

        self.square.setStyleSheet("QFrame{ background-color:%s}"%self.col.name())
    def changeValue(self,value):
        if value==0:
            self.label.setPixmap(QPixmap('07.bmp'))
        elif value>0 and value <=30:
            self.label.setPixmap(QPixmap('06.bmp'))
        elif value>30 and value <=80:
            self.label.setPixmap(QPixmap('05.bmp'))
        else:
            self.label.setPixmap(QPixmap('04.bmp'))

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())

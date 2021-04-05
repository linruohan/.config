from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor
import sys
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.col=QColor(0,0,0)

        redbtn=QPushButton('red',self)
        redbtn.setCheckable(True)#状态可检测
        redbtn.move(10,10)
        redbtn.clicked[bool].connect(self.setColor)

        bluebtn=QPushButton('blue',self)
        bluebtn.setCheckable(True)#状态可检测
        bluebtn.move(10,60)
        bluebtn.clicked[bool].connect(self.setColor)

        greenbtn=QPushButton('green',self)
        greenbtn.setCheckable(True)#状态可检测
        greenbtn.move(10,120)
        greenbtn.clicked[bool].connect(self.setColor)

        self.square=QFrame(self)
        self.square.setGeometry(150,20,100,100)
        self.square.setStyleSheet("QWidget { background-color:%s}"%self.col.name())

        self.setGeometry(300,300,280,170)
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

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())

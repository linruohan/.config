#coding=utf-8


import sys
from PyQt5.QtWidgets import QFrame,QColorDialog,QWidget,QPushButton,QLineEdit,QInputDialog,QApplication
from PyQt5.QtGui import QColor
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        col=QColor(120,10,20)

        self.btn=QPushButton('输入窗体名称',self)
        self.btn.move(10,10)
        self.btn.clicked.connect(self.showDialog)

        self.le=QLineEdit(self)
        self.le.move(90,10)

        self.btn1=QPushButton('设置背景颜色',self)
        self.btn1.move(10,40)
        self.btn1.clicked.connect(self.showColor)

        self.frm=QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color:%s}" %col.name())
        self.frm.setGeometry(90,40,133,20)

        #x,y,w,h
        self.setGeometry(300,300,800,600)
        self.setWindowTitle('Input dialog')
        self.setStyleSheet("background-color:purple")
        self.show()

    def showDialog(self):
        text,ok=QInputDialog.getText(self,'请输入','Enter your name:')
        if ok:
            self.le.setText(str(text))
            self.setWindowTitle(str(text))
    def showColor(self):
        col=QColorDialog.getColor()

        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color:%s}" %col.name())
            self.setStyleSheet("background-color:%s"%col.name())
if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())

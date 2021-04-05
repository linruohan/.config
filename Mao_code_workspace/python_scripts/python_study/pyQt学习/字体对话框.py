#coding=utf-8


import sys
from PyQt5.QtWidgets import (QFrame,QColorDialog,QWidget,
    QPushButton,QLineEdit,QInputDialog,QApplication,QVBoxLayout,QSizePolicy,QFontDialog,QLabel)
from PyQt5.QtGui import QColor
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox=QVBoxLayout()

        btn=QPushButton('font Dialog',self)
        btn.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        btn.move(10,20)

        vbox.addWidget(btn)
        btn.clicked.connect(self.showFontDialog)

        self.lb1=QLabel('Knowledge only matters',self)
        self.lb1.move(130,20)

        vbox.addWidget(self.lb1)
        self.setLayout(vbox)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Font dialog')
        self.show()
    def showFontDialog(self):
        font,ok =QFontDialog.getFont()
        if ok:
            self.lb1.setFont(font)

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

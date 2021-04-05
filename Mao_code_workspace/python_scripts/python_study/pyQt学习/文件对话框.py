#coding=utf-8

import sys
from PyQt5.QtWidgets import (QFrame,QColorDialog,QWidget,QMainWindow,QTextEdit,QAction,QFileDialog,
    QPushButton,QLineEdit,QInputDialog,QApplication,QVBoxLayout,QSizePolicy,QFontDialog,QLabel)
from PyQt5.QtGui import QColor,QIcon
class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textEdit=QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openfile=QAction(QIcon('open.bmp'),'open',self)
        openfile.setShortcut('Ctrl+O')
        openfile.setStatusTip('open the file')
        openfile.triggered.connect(self.showFileDialog)

        menubar=self.menuBar()
        filemenu=menubar.addMenu('&File')
        filemenu.addAction(openfile)
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Font dialog')
        self.show()

    def showFileDialog(self):
        fname=QFileDialog.getOpenFileName(self,'open file','/home')
        print(fname)
        if fname[0]:
            with open(fname[0], 'r',encoding='utf-8',errors='ignore') as f:

                data=f.read()
                self.textEdit.setText(data)




    # def showFontDialog(self):
    #     font,ok =QFontDialog.getFont()
    #     if ok:
    #         self.lb1.setFont(font)
    #
    # def showDialog(self):
    #     text,ok=QInputDialog.getText(self,'请输入','Enter your name:')
    #     if ok:
    #         self.le.setText(str(text))
    #         self.setWindowTitle(str(text))
    # def showColor(self):
    #     col=QColorDialog.getColor()
    #
    #     if col.isValid():
    #         self.frm.setStyleSheet("QWidget { background-color:%s}" %col.name())
    #         self.setStyleSheet("background-color:%s"%col.name())
if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())

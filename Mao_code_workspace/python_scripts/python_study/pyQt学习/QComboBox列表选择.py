import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.lb1=QLabel('Ubuntu',self)
        combo=QComboBox(self)
        combo.addItem('Ubuntu')
        combo.addItem('Mandriva')
        combo.addItem('Fedora')
        combo.addItem('Arch')
        combo.addItem('Gentoo')

        combo.move(50,50)
        self.lb1.move(50,150)
        # 基于选择,我们调用onActivated()方法.
        combo.activated[str].connect(self.onActived)

        self.setGeometry(200,300,300,150)
        self.setWindowTitle('QCheckBox')
        self.show()

    def onActived(self,text):
        self.lb1.setText(text)
        self.lb1.adjustSize()#调整标签的长度到文本的长度

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        # 水平布局
        hbox=QHBoxLayout(self)

        #上左
        topleft=QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)
        #上右
        topright=QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)
        # 底部
        bottom=QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)

        # 分割器1
        splitter1=QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)
        #分割器2
        splitter2=QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)

        self.setGeometry(200,300,300,150)
        self.setWindowTitle('QCheckBox')
        self.show()

    def onChanged(self,text):
        self.lb1.setText(text)
        self.lb1.adjustSize()#调整标签的长度到文本的长度

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())

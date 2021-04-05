import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 标签框
        self.lb1 = QLabel(self)
        qle = QLineEdit(self)
        qle.move(60, 100)
        self.lb1.move(60, 40)

        qle.textChanged[str].connect(self.onChanged)

        self.setGeometry(200, 300, 300, 150)
        self.setWindowTitle('QCheckBox')
        self.show()

    def onChanged(self, text):
        self.lb1.setText(text)
        self.lb1.adjustSize()  # 调整标签的长度到文本的长度


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

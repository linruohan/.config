import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QDial, QDialog, QHBoxLayout, QSpinBox


# 仪表盘

class ZeroSpinBox(QSpinBox):
    atzero = pyqtSignal(int)
    zeros = 0

    def __init__(self):
        super(ZeroSpinBox, self).__init__()
        self.valueChanged[int].connect(self.checkzero)

    def checkzero(self):
        if self.value() == 0:
            self.zeros += 1
            self.atzero.emit(self.zeros)


class Form(QDialog):
    '''拨号盘和微调器'''

    def __init__(self):
        super(Form, self).__init__()
        self.initUI()

    def initUI(self):
        dial = QDial()
        dial.setNotchesVisible(True)
        spinbox = QSpinBox()
        zspinbox = ZeroSpinBox()
        layout = QHBoxLayout(self)
        layout.addWidget(dial)
        layout.addWidget(spinbox)
        layout.addWidget(zspinbox)

        dial.valueChanged[int].connect(zspinbox.setValue)
        spinbox.valueChanged[int].connect(dial.setValue)
        zspinbox.atzero.connect(self.count)

    def count(self, zeros):
        print('zerospinbox has been at zero %d times' % zeros)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Form()
    win.show()
    sys.exit(app.exec_())

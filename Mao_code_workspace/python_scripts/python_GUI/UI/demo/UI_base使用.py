# coding=utf-8
from PyQt5.QtWidgets import QApplication
import sys
from PyQt5.QtWidgets import QLabel
from UI_base import UI_base


class Mydemo(UI_base):
    """docstring for Mydemo."""
    def __init__(self):
        super(Mydemo, self).__init__()
        self.main_layout.addWidget(QLabel('123'), 1, 0, 1, 1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Mydemo()
    win.show()
    sys.exit(app.exec_())

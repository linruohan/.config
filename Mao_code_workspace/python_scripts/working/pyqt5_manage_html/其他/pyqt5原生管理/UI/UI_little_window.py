# *_*coding:utf-8 *_* 
__Author__ = 'xiaohan'

import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QBrush, QColor
from PyQt5.QtCore import *
import sys
from PyQt5.QtWidgets import *


class Window(QMainWindow):

    def __init__(self, title, path, parent=None):
        super(Window, self).__init__(parent)
        layout = QFormLayout()
        self.text = QTextEdit("请输入工作目录： ")
        self.text.selectAll()
        self.selectBtn = QPushButton("请选择")
        self.selectBtn.clicked.connect(self.click)
        layout.addWidget(self.text)
        layout.addWidget(self.selectBtn)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.setWindowTitle('小窗口')
        self.setGeometry(500, 300, 800, 600)

    def click(self):
        text, okPressed = QInputDialog.getText(self, "Get text", "Your name:", QLineEdit.Normal, "")
        if okPressed and text != '':
            self.text.setText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window("123", "123")
    w.show()
    sys.exit(app.exec_())

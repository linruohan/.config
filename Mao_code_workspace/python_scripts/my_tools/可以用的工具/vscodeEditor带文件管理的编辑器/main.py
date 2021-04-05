# *_*coding:utf-8 *_*
__Author__ = 'xiaohan'

import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from UI_main import UIMain


class MyVscodeEditor(UIMain):

    def __init__(self, parent=None):
        super(MyVscodeEditor, self).__init__(parent)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/main.ico"))
    form = MyVscodeEditor()
    form.show()
    app.exec_()

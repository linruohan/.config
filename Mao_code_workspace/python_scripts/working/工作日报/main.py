# *_*coding:utf-8 *_* 

import sys

from PyQt5.QtWidgets import QApplication

from UI_Main import UiMain


class WokeReport(UiMain):
    def __init__(self):
        super(WokeReport, self).__init__()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WokeReport()
    window.show()
    sys.exit(app.exec_())

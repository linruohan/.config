# coding=utf-8
import os
import sys

from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from UI_main import Ui_MainWindow

class MainWindow(Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi()
        splitter2 = QSplitter(Qt.Horizontal)
        splitter2.addWidget(self.splitter1)
        splitter2.addWidget(self.webview)
        splitter2.setSizes([100, 500])
        self.mainLayout.addWidget(splitter2, 0, 0, 8, 5)

    def setupUi(self):
        self.webview = QWebEngineView()
        self.webview.setObjectName("webview")
        self.webview.setMinimumWidth(400)
        self.index = (os.path.split(os.path.realpath(__file__))
        [0]) + "/index.html"
        self.webview.load(QUrl.fromLocalFile(self.index))
        self.webview.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())

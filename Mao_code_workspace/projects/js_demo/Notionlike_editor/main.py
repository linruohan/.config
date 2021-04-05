# coding=utf-8
import os
import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow, QApplication,QHBoxLayout,QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.mainlayout=QHBoxLayout()
        self.setupUi()
        self.mainlayout.addWidget(self.webview)


        self.widget=QWidget()
        self.widget.setLayout(self.mainlayout)
        self.setCentralWidget(self.widget)
        self.setGeometry(300,500,800,600)
        self.setWindowTitle('小寒编辑器')

        
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

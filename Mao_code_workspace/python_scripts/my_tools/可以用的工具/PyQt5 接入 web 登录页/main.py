import sys
import time
from threading import Thread
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction

import context
from content import MainContent
from login import Login


class Main(QMainWindow):
    str_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi()
        self.init_signal()
        self.connect()

    def setupUi(self):
        self.resize(1000, 700)
        self.menu = self.menuBar().addMenu('User')
        self.logout_action = QAction("&Logout", self)
        self.menu.addAction(self.logout_action)

        self.centralWidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralWidget)

        self.grid_layout = QtWidgets.QGridLayout(self.centralWidget)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.grid_layout.setSpacing(0)

        self.login_form = Login(self)
        self.main_content = MainContent(self)
        self.grid_layout.addWidget(self.login_form, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.main_content, 1, 2, 1, 1)

        self.show_login()
        self.monitor_token()

    def init_signal(self):
        def func(signal):
            getattr(self, signal)()

        self.str_signal[str].connect(func)

    def connect(self):
        self.logout_action.triggered.connect(self.show_login)

    def show_login(self):
        self.login_form.logout()
        self.login_form.show()
        self.main_content.hide()

    def show_main(self):
        self.login_form.hide()
        self.main_content.show()

    def monitor_token(self):
        def func():
            while True:
                if not context.cookies.get('_accessToken'):
                    self.login_form.load_cookies()
                    time.sleep(1)
                    if context.cookies.get('_accessToken'):
                        self.str_signal.emit("show_main")

        t = Thread(target=func)
        t.setDaemon(True)
        t.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Main()
    ui.show()
    sys.exit(app.exec_())
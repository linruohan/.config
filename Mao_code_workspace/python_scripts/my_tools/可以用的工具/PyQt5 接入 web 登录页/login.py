# -*- encoding:utf-8 -*-
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtCore import QUrl
import json
import context


class Login(QtWebEngineWidgets.QWebEngineView):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi()
        self.connect()

    def setupUi(self):
        self.load(QUrl('https://crm.chengfayun.com'))

    def connect(self):
        self.loadFinished.connect(self.load_cookies)

    def load_cookies(self):
        print('load cookies', self.url())

        def parse_cookies(origin):
            if origin:
                context.cookies = {item.split("=")[0]: item.split(
                    "=")[1] for item in origin.split('; ')}

        self.page().runJavaScript('document.cookie', parse_cookies)

    def logout(self):
        self.page().profile().cookieStore().deleteAllCookies()
        self.reload()

    def print_cookie(self):
        print(json.dumps(self.cookies, ensure_ascii=False, indent=2))
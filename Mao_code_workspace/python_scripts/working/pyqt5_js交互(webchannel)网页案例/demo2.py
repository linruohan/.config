import json
import os
import sys

from PyQt5.QtCore import QObject, QUrl, pyqtSlot
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication


class CallHandler(QObject):
    @pyqtSlot(result=str)
    def myHello(self):
        view.page().runJavaScript('uptext("hello, Pythongjhkkkk");')
        print('call received')
        return 'hello, Python'

    @pyqtSlot(str, result=str)
    def myTest(self, test):
        print('test is', test)
        test_dict = {'detail': [{"id": '0', 'name': 'xiaomei'}, {"id": '1', 'name': 'lili'}]}
        return json.dumps(test_dict)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = QWebEngineView()
    channel = QWebChannel()
    handler = CallHandler()
    channel.registerObject('pyjs', handler)  ##前者是str，后者是一个QObject（里面放着需要调用的函数）
    view.page().setWebChannel(channel)
    url_string = os.path.join(os.path.dirname(__file__), "index2.html")
    print(url_string)
    view.load(QUrl.fromLocalFile(url_string))
    view.show()
    sys.exit(app.exec_())

import os
import sys

#==============================================
#       使用python 打开froala editor编辑器
#==============================================

from PyQt5 import QtNetwork
from PyQt5.QtCore import QObject, QUrl, pyqtSignal, pyqtSlot
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QMainWindow

from common import file_read, file_write_or_save
from common_html import render_html_str

# 系统默认设置为自动寻找代理，而使用代理后延迟会变得非常大。
# 解决方法也非常简单，关掉使用系统代理设定即可。
QtNetwork.QNetworkProxyFactory.setUseSystemConfiguration(False)


class TInteractObj(QObject):
    sig_send_to_js = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.receive_str_from_js_callback = None

    @pyqtSlot(str)
    def receive_str_from_js(self, str):
        print('INFO: 从js接受到信息...')
        self.receive_str_from_js_callback(str)


class MyWeb(QMainWindow):
    editor_path = (os.path.split(os.path.realpath(__file__))[0]) + "/web/templates/admin/002.html"

    def __init__(self, html_path, parent=None):
        super(MyWeb, self).__init__(parent)
        self.webview = QWebEngineView()
        self.setCentralWidget(self.webview)

        self.html_path = html_path
        self.setWindowTitle('* ' + os.path.basename(self.html_path))
        # 交互对象
        self.interact_obj = TInteractObj(self)
        self.channel = QWebChannel(self.webview.page())
        self.webview.page().setWebChannel(self.channel)

        self.init_web()

    def init_web(self):
        self.webview.load(QUrl.fromLocalFile(self.editor_path))
        # """为webview绑定交互对象"""
        self.interact_obj.receive_str_from_js_callback = self.receive_data
        self.channel.registerObject("interact_obj", self.interact_obj)

    def receive_data(self, data):
        if len(data):
            file_write_or_save(self.html_path + '.bak', data)

    def go_btn_clicked(self):
        # 这个信号是在js中和一个js方法绑定的,所以发射这个信号时会执行对应的js方法.
        print(f'INFO: pyqt发送信息: {self.html_path} ...')
        self.interact_obj.sig_send_to_js.emit(self.openfile(self.html_path))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MyWeb('data/tasks/tasks_html/1.html')
    ui.show()
    sys.exit(app.exec_())

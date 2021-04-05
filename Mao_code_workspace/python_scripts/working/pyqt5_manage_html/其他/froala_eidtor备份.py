import os
import sys

from PyQt5 import QtCore, QtNetwork, QtWidgets
from PyQt5.QtCore import QObject, QUrl, pyqtSignal, pyqtSlot
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QMainWindow

# 系统默认设置为自动寻找代理，而使用代理后延迟会变得非常大。
# 解决方法也非常简单，关掉使用系统代理设定即可。
QtNetwork.QNetworkProxyFactory.setUseSystemConfiguration(False)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 570)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setReadOnly(False)
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.webview = QWebEngineView(self.centralwidget)
        self.webview.setObjectName("webview")
        self.webview.setMinimumWidth(800)
        self.gridLayout.addWidget(self.webview, 0, 1, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "同步到web"))


class TInteractObj(QObject):
    """
    一个槽函数供js调用(内部最终将js的调用转化为了信号),
    一个信号供js绑定,
    这个一个交互对象最基本的组成部分.
    """
    # 定义信号,该信号会在js中绑定一个js方法.
    sig_send_to_js = pyqtSignal(str)
    def __init__(self, parent=None):
        super().__init__(parent)
        # 交互对象接收到js调用后执行的回调函数.
        self.receive_str_from_js_callback = None

    # str表示接收str类型的信号,信号是从js发出的.可以出传递的参数类型有很多种：str、int、list、object、float、tuple、dict等等
    @pyqtSlot(str)
    def receive_str_from_js(self, str):
        print('接受消息str is ', str)
        self.receive_str_from_js_callback(str)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, html_path, parent=None):
        super(MainWindow, self).__init__(parent)
        self.html_path = html_path
        self.editor_path = (os.path.split(os.path.realpath(__file__))[
            0]) + "/web/templates/froala_editor.html"
        self.setupUi(self)
        self.webview.load(QUrl.fromLocalFile(self.editor_path))
        self.init_channel()

    def init_channel(self):
        """
        为webview绑定交互对象
        """
        self.interact_obj = TInteractObj(self)
        self.interact_obj.receive_str_from_js_callback = self.receive_data

        channel = QWebChannel(self.webview.page())
        # interact_obj 为交互对象的名字,js中使用.
        channel.registerObject("interact_obj", self.interact_obj)

        self.webview.page().setWebChannel(channel)

    def receive_data(self, data):
        # print(data)
        self.textBrowser.setHtml(data)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        # 这个信号是在js中和一个js方法绑定的,所以发射这个信号时会执行对应的js方法.
        print('pyqt发送消息')
        self.interact_obj.sig_send_to_js.emit(self.openfile('./001.html'))

    def openfile(self, filename):
        if not str(filename).endswith('.json'):
            pass
        with open(filename, 'r', encoding='utf-8') as f:
            string = f.read()
        print(string)
        return string


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWindow('')
    ui.show()
    sys.exit(app.exec_())

import os
import sys
from PyQt5.QtCore import QUrl, pyqtSlot, QObject, pyqtSignal
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QHBoxLayout, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView


class TInteractObj(QObject):
    # 定义信号,该信号会在js中绑定一个js方法.
    sig_send_to_js = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        # 交互对象接收到js调用后执行的回调函数.
        self.receive_str_from_js_callback = None

    # str表示接收str类型的信号,信号是从js发出的.可以出传递的参数类型有很多种：str、int、list、object、float、tuple、dict等等
    @pyqtSlot(str)
    def receive_str_from_js(self, str):
        print('pyqt5接受消息str is :', str)
        self.receive_str_from_js_callback(str)

    @pyqtSlot(str, result=list)
    def get_str_from_js_withargs(self, content):
        print('输出文本：', content)  # 对接收到的内容进行处理，比如调用打印机进行打印等等。此处略去，只在bash中显示接收到的消息
        data = {
            'path': 123,
            'list': "123"
        }
        return [123, data]

    @pyqtSlot(result=str)
    def myHello(self, view):
        view.page().runJavaScript('uptext("hello, Pythongjhkkkk");')
        print('call received')
        return 'hello, Python'

    @pyqtSlot(str, result=str)
    def myTest(self, test):
        print('test is', test)
        return '返回前端结果'


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setObjectName("MainWindow")
        self.setGeometry(300, 100, 800, 570)
        widget = QWidget()
        self.main_layout = QHBoxLayout()
        self.webview = QWebEngineView()
        self.webview.setObjectName("webview")
        self.btn = QPushButton("转换")
        self.btn.clicked.connect(self.on_pushButton_clicked)
        self.main_layout.addWidget(self.btn)
        self.main_layout.addWidget(self.webview)
        widget.setLayout(self.main_layout)
        self.setCentralWidget(widget)

        self.webview.load(QUrl.fromLocalFile(
            os.path.abspath('templates/003.html')))
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

    # pyqt5 获取js传过来的值,并进行处理
    def receive_data(self, data):
        print("receive_datad:")
        print(data)

    # js获取pyQT5传递的变量值
    def on_pushButton_clicked(self):
        print('pyqt发送消息')
        data = {
            'path': 123,
            'list': "123"
        }
        self.interact_obj.sig_send_to_js.emit("123")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())

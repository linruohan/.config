# *_*coding:utf-8 *_*
__Author__ = 'xiaohan'
import sys, time
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Test_demo(QMainWindow):

    def __init__(self, parent=None):
        super(Test_demo, self).__init__(parent)
        self.main_layout = QGridLayout()
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)
        self.setGeometry(800, 150, 800, 600)

    def initUI(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)

    splash = QSplashScreen(QPixmap('./start.jpg'))
    splash.show()
    for i in range(5):
        i = str(i * 20)
        splash.showMessage(f'正在加载中...{i}%%', Qt.AlignRight + Qt.AlignBottom, Qt.red)
        time.sleep(1)
    splash.showMessage('加载完毕...启动中', Qt.AlignRight + Qt.AlignBottom, Qt.red)
    time.sleep(1)
    app.processEvents()
    demo = Test_demo()
    demo.show()
    splash.finish(demo)
    sys.exit(app.exec_())

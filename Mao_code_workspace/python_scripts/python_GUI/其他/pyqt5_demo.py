# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtSlot, QBasicTimer, Qt
from PyQt5.QtWidgets import QDialog, QSplashScreen
from Ui_processbar1 import Ui_windows2


class windows2(QDialog, Ui_windows2):

    def __init__(self, parent=None):
        super(windows2, self).__init__(parent)
        self.setupUi(self)
        # 创建一个定时器对象，默认开始为0
        self.timer = QBasicTimer()
        self.step = 0

    @pyqtSlot()
    def on_pushButton_clicked(self):
        if self.timer.isActive():
            self.timer.stop()
            self.pushButton.setText('开始')
        else:
            self.timer.start(100, self)
            self.pushButton.setText('暂停')

    def timerEvent(self, event):
        if self.step >= 100:
            self.timer.stop()
            return
        self.step = self.step + 1
        self.progressBar.setValue(self.step)

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        self.timer.stop()
        self.progressBar.setValue(0)

    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        for i in range(100):
            self.progressBar_2.setValue(i)
            time.sleep(0.1)

    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        self.progressBar_2.setValue(0)

    @pyqtSlot()
    def on_pushButton_5_clicked(self):
        self.progressBar_5.setMaximum(0)
        self.progressBar_7.setMaximum(0)
        self.progressBar_4.setMaximum(0)
        self.progressBar_6.setMaximum(0)

    @pyqtSlot()
    def on_pushButton_6_clicked(self):
        self.progressBar_4.setMaximum(1)
        self.progressBar_5.setMaximum(1)
        self.progressBar_6.setMaximum(1)
        self.progressBar_7.setMaximum(1)


if __name__ == "__main__":
    import sys
    import time
    import PyQt5
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    # 定义QSplashScreen 插入启动页背景图
    splash = QSplashScreen(PyQt5.QtGui.QPixmap("splash.jpg"))
    splash.show()
    # 定义字体格式
    font = PyQt5.QtGui.QFont()
    font.setPointSize(16)
    font.setBold(True)
    font.setWeight(75)
    splash.setFont(font)
    splash.showMessage("正在加载。。。", Qt.AlignCenter, Qt.red,)
    time.sleep(1)
    splash.showMessage("渲染图片。。。", Qt.AlignCenter, Qt.red)
    time.sleep(1)
    # 设置进程，启动加载页面时可以进行其他操作而不会卡死
    app.processEvents()
    ui = windows2()
    ui.show()
    # 结束启动页
    splash.finish(ui)
    sys.exit(app.exec_())

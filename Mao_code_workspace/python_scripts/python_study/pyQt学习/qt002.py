#coding=utf-8
from PyQt5.QtWidgets import QApplication, QWidget
import sys
from PyQt5 import QtWidgets
# 最后面写入程序入口：
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    label=QtWidgets.QLabel(MainWindow)     #在窗口中绑定label
    label.setText("hello world")













    MainWindow.show()
    sys.exit(app.exec_())

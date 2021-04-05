# -*- encoding:utf-8 -*-
import base64
import os
import sys

from PyQt5 import QtWebEngineWidgets, QtWidgets
from PyQt5.QtCore import QSize, QUrl


class ViewCode(QtWidgets.QDockWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        widget = QtWidgets.QWidget(self)
        vertical_layout = QtWidgets.QVBoxLayout(widget)
        vertical_layout.setContentsMargins(0, 0, 0, 0)
        vertical_layout.setSpacing(2)

        index = (os.path.split(os.path.realpath(__file__))[0]) + "/monaco_index.html"
        self.editor = QtWebEngineWidgets.QWebEngineView(widget)
        self.editor.load(QUrl.fromLocalFile(index))
        layout = QtWidgets.QHBoxLayout()
        self.open_btn = QtWidgets.QPushButton("打开", widget)
        self.save_btn = QtWidgets.QPushButton("保存", widget)
        layout.addWidget(self.open_btn)
        layout.addWidget(self.save_btn)
        vertical_layout.addLayout(layout)
        vertical_layout.addWidget(self.editor)
        self.setWidget(widget)

    def sizeHint(self):
        return QSize(700, 900)

    def get_value(self, callback):
        self.editor.page().runJavaScript("monaco.editor.getModels()[0].getValue()", callback)

    def set_value(self, data):
        if data is None:
            return
        data = base64.b64encode(data.encode())
        data = data.decode()
        self.editor.page().runJavaScript("monaco.editor.getModels()[0].setValue(Base.decode('{}'))".format(data))

    def copy(self):
        pass

    def cut(self):
        pass

    def paste(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = ViewCode()
    ui.show()
    sys.exit(app.exec_())

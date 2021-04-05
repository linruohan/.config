# -*- encoding:utf-8 -*-
import base64
import os
import sys

from PyQt5 import QtWebEngineWidgets, QtWidgets
from PyQt5.QtCore import QSize, QUrl, Qt


class ViewCode(QtWidgets.QDockWidget):

    def __init__(self, filename=None, parent=None):
        super().__init__(parent=parent)
        self.filename = filename
        self.setWindowFlags(Qt.FramelessWindowHint)  # 无边框
        self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
        self.setup_ui()

    def setup_ui(self):
        widget = QtWidgets.QWidget(self)
        vertical_layout = QtWidgets.QVBoxLayout(widget)
        vertical_layout.setContentsMargins(0, 0, 0, 0)
        vertical_layout.setSpacing(2)

        index = (os.path.split(os.path.realpath(__file__))[0]) + "/utils/index.html"
        self.editor = QtWebEngineWidgets.QWebEngineView(widget)
        self.editor.load(QUrl.fromLocalFile(index))
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

    # def fileOpen(self):
    #     print("in fileopen", self.filename)
    #     dir = (os.path.dirname(self.filename)
    #            if self.filename is not None else ".")
    #     if not self.filename:
    #         fname = str(QFileDialog.getOpenFileName(self,
    #                                                 "Python Editor - Choose File", dir,
    #                                                 "all files(*.*)")[0])
    #         if fname:
    #             self.filename = fname
    #     if self.filename:
    #         self.set_value(self.get_code())
    #         print('load_file success')
    #         self.setWindowTitle("Python Editor - {0}".format(
    #             QFileInfo(self.filename).fileName()))
    #
    # def get_code(self):
    #     with open(self.filename, encoding='utf-8') as f:
    #         print(f.read())
    #         return f.read()
    #
    # def save_code(self):
    #     def func(code):
    #         if not self.filename:
    #             filename, filetype = QFileDialog.getSaveFileName(self,
    #                                                              "Python Editor -- Save File As", '.',
    #                                                              "all files(*.*)")
    #             if filename:
    #                 self.filename = filename
    #                 self.setWindowTitle("Python Editor - {0}".format(
    #                     QFileInfo(self.filename).fileName()))
    #         with open(self.filename, "w", encoding='utf-8') as f:
    #             f.write(code)
    #
    #     self.get_value(func)

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

'''
@Author: your name
@Date: 2019-12-14 09:45:25
@LastEditTime: 2019-12-14 11:51:51
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python_GUI\vscode_editor\vscode_editor.py
'''
import sys
import os
import UI_textedit as textedit
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *


class Editor(QWebEngineView):
    def __init__(self, par):
        super().__init__(par)
        self.editor_flag = []
        self.text = ""
        # 这里是本地html路径,需根据实际情况进行修改.
        self.editor_index = os.path.join(os.path.dirname(os.path.dirname(__file__)), "./utils/index.html")
        self.load(QUrl.fromLocalFile(self.editor_index))
        self.showMaximized()
        # self.document=self.get_value(self.check)

    def callback(self, result):
        print(result)
        self.text = result

    def get_value(self,callback):
        """设置编辑器内容"""
        self.page().runJavaScript("monaco.editor.getModels()[0].getValue()", callback)

    def set_value(self, data):
        """获取编辑器内容"""
        import base64
        data = base64.b64encode(data.encode())
        data = data.decode()
        self.page().runJavaScript("monaco.editor.getModels()[0].setValue(Base.decode('{}'))".format(data))

    def change_language(self, lan):
        """切换智能提示语言"""
        self.page().runJavaScript("monaco.editor.setModelLanguage(monaco.editor.getModels()[0],'{}')".format(lan))

    def save(self):
        self.get_value(self.callback)
        print(self.text)
        if self.filename.startswith("Untitled"):
            self.filename = \
                QFileDialog.getSaveFileName(self, "保存文件", self.filename, "Text files (*.txt);;HTML files (*.html)")[0]
        with open(self.filename, 'w') as file_path:
            file_path.write(self.text)
        self.setWindowTitle(QFileInfo(self.filename).fileName())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = Editor(None)
    w.setWindowTitle('Editor')
    w.show()
    sys.exit(app.exec_())

    """2. 在主界面中添加编辑器标签(多标签的实现)
增加标签
关闭标签
QTabwidget刚好可以满足多标签的需求,下面有几个问题要解决:

每个标签右上角显示关闭按钮
默认情况下,标签是不显示关闭按钮的,可以通过设置self.tabWidget.setTabsClosable(True)方法显示出关闭按钮.
关闭按钮点击事件

self.tabWidget.tabCloseRequested.connect(self.closeTab)

def closeTab(self):
# 获取当前处于激活状态的标签
i = self.tabWidget.currentIndex()
self.tabWidget.removeTab(i)
增加页面

new_tab = Editor(self)
self.tabWidget.addTab(new_tab, tab_name)
self.tabWidget.setCurrentWidget(new_tab)"""

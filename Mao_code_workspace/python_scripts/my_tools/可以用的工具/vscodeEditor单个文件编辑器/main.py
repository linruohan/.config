import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QPushButton

from components.viewCode import ViewCode


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 100, 800, 600)
        self.setup_ui()
        self.filename = None
        # 主控件,QMainWindow一般有一个主控件,用来布局.
        self.cw = QtWidgets.QWidget(self)
        self.cw_layout = QtWidgets.QVBoxLayout(self.cw)
        self.cw_layout.setContentsMargins(0, 0, 0, 0)
        self.cw_layout.setSpacing(0)
        self.setCentralWidget(self.cw)
        # 布局
        self.code_view = ViewCode()
        self.code_view.open_btn.clicked.connect(self.click_query_btn)
        self.code_view.save_btn.clicked.connect(self.save_code)

        self.cw_layout.addWidget(self.code_view)

    def setup_ui(self):
        # 尺寸
        self.showMaximized()
        # 标题
        self.setWindowTitle('PyQt5 Playground')
        # 菜单栏
        # 树形菜单
        # 代码编辑器

        # 加载控件

    def click_query_btn(self):
        if not self.filename:
            self.filename = str(QFileDialog.getOpenFileName(self,
                                                            "Python Editor - Choose File", '.', "all files(*.*)")[0])
        self.code_view.set_value(self.get_code())

    def get_code(self):
        with open(self.filename, encoding='utf-8') as f:
            return f.read()

    def save_code(self):
        def func(code):
            if not self.filename:
                self.filename = str(QFileDialog.getOpenFileName(self,
                                                "Python Editor - Choose File", '.', "all files(*.*)")[0])
            with open(self.filename, "w", encoding='utf-8') as f:
                f.write(code)
        self.code_view.get_value(func)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Main()
    ui.show()
    sys.exit(app.exec_())

# *_*coding:utf-8 *_*
__Author__ = 'xiaohan'

import sys

from PyQt5.QtWidgets import *

from UI_mywidget import MyTree


class Mywidget(QMainWindow):
    def __init__(self, parent=None):
        super(Mywidget, self).__init__(parent)
        self.main_layout = QGridLayout()
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)
        self.setGeometry(800, 150, 800, 600)

        self.tree_widget = MyTree(['h1', 'h2'], ['1_2', '3_4', '5_6'])
        # self.tree_widget.get_tree_nodes()
        updateBtn = QPushButton("修改节点")
        updateBtn.clicked.connect(self.get_tree_nodes)

        self.main_layout.addWidget(updateBtn, 0, 0, 1, 1)
        self.main_layout.addWidget(self.tree_widget, 1, 0, 1, 1)

    def get_tree_nodes(self):
        self.tree_widget.update_tree()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Mywidget()
    demo.show()
    sys.exit(app.exec_())

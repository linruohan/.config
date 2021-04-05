# _*_ coding=utf-8 _*_
import os
import sys

from PyQt5.QtCore import QFileInfo
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QFileDialog, QFileIconProvider, QHBoxLayout, QInputDialog, \
    QLineEdit, QMainWindow, QPushButton, QTreeWidgetItem, QVBoxLayout, QWidget

"根据传入的路径,显示文件tree"
sys.path.append('.')
from UI_mywidget import MyTree


class FileTree(QMainWindow):

    def __init__(self, parent=None):
        self.work_path = ''
        super(FileTree, self).__init__(parent)
        self.filepath = None
        self.tree = MyTree(['文件管理'], [])
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.addLayout(self.get_file_operations_layout())

        main_layout.addWidget(self.tree)

        widget = QWidget()
        widget.setLayout(main_layout)
        QApplication.processEvents()
        self.setCentralWidget(widget)

    def get_file_operations_layout(self):
        operator_layout = QHBoxLayout()
        add_btn = QPushButton("打开文件夹")
        update_btn = QPushButton("Rename")
        del_btn = QPushButton("Delete")
        operator_layout.addWidget(add_btn)
        operator_layout.addWidget(update_btn)
        operator_layout.addWidget(del_btn)
        # 按钮的信号槽连接
        add_btn.clicked.connect(self.click_add_work_dir)
        update_btn.clicked.connect(self.rename)
        del_btn.clicked.connect(self.tree.delete_node)
        return operator_layout

    def click_add_work_dir(self):
        self.work_path = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")
        self.get_root_child()
        self.tree.expandAll()

    def get_root_child(self):
        dirs = os.listdir(self.work_path)
        file_info = QFileInfo(self.work_path)
        file_icon = QFileIconProvider()
        icon = QIcon(file_icon.icon(file_info))
        root = QTreeWidgetItem(self.tree)
        root.setText(0, self.work_path.split('/')[-1])
        root.setIcon(0, QIcon(icon))
        self.tree.addTopLevelItem(root)
        self.render_file_tree(dirs, root, self.work_path)

    def render_file_tree(self, dirs, root, path):
        for dir in dirs:
            path_new = path + '\\' + dir
            if os.path.isdir(path_new):
                file_info = QFileInfo(path_new)
                file_icon = QFileIconProvider()
                icon = QIcon(file_icon.icon(file_info))
                child = QTreeWidgetItem(root)
                child.setText(0, dir)
                child.setIcon(0, QIcon(icon))
                dirs_new = os.listdir(path_new)
                self.render_file_tree(dirs_new, child, path_new)
            else:
                file_info = QFileInfo(path_new)
                file_icon = QFileIconProvider()
                icon = QIcon(file_icon.icon(file_info))
                child = QTreeWidgetItem(root)
                child.setText(0, dir)
                child.setIcon(0, QIcon(icon))

    def rename(self):
        item = self.tree.currentItem()
        text, ok = QInputDialog.getText(self, "Rename", "Rname this file by string :", QLineEdit.Normal, "")
        if ok and text != '':
            item.setText(0, text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tree = FileTree()
    tree.show()
    sys.exit(app.exec_())

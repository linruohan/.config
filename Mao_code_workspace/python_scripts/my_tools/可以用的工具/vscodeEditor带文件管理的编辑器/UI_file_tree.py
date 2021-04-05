import os
import sys
from time import sleep

from PyQt5.QtCore import QFileInfo, Qt
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QAbstractItemView, QApplication, QFileDialog, QFileIconProvider, QHBoxLayout, QInputDialog, \
    QLineEdit, QPushButton, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget

"根据传入的路径,显示文件tree"


class MyTree(QTreeWidget):

    def __init__(self, header_list, node_name_list, parent=None):
        super(MyTree, self).__init__(parent)
        self.current_filename = ''
        self.node_name_list = node_name_list
        self.header_list = header_list
        self.setWindowTitle('My Browser')
        self.showMaximized()
        # self.setWindowFlags(Qt.FramelessWindowHint)# 无边框
        self.setFont(QFont("Consolas", 12, QFont.Normal, False))
        self.headerItem().setFont(0, QFont("Consolas", 12, QFont.Normal, False))  # 设置treewidget头字体格式
        self.setColumnCount(len(self.header_list))  # 设置列数
        self.setHeaderLabels(self.header_list)  # 设置头的标题
        # self.root = QTreeWidgetItem(self)
        # self.root.setText(0, 'root')
        # self.addTopLevelItem(self.root)
        self.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.setDragDropOverwriteMode(True)
        self.setEnabled(True)
        # self.setItemDelegateForColumn(1, EmptyDelegate(self))  # 设置第二列不可编辑
        # self.setDragEnabled(True)
        # self.expandAll()
        # self.clicked.connect(self.click_tree)

    def update_tree(self, root):
        # self.root.takeChildren() # QTreeWidgetItem::takeChildren() //删除所有子列表项
        # self.root.removeChild(self.currentItem()) //删除指定子列表项,参数为:QTreeWidgetItem
        # self.root.takeChild(index) //删除指定索引的子列表项
        # self.root.addChild(QTreeWidgetItem * child) //添加子列表项
        # self.root.addChildren(const QList<QTreeWidgetItem *> & children) //添加多条子列表项
        root.takeChildren()
        sleep(1)
        self.get_treenodes()

    def get_tree_nodes(self):
        for node_name in self.node_name_list:
            child1 = QTreeWidgetItem(self.root)
            for i in range(len(self.headerslist)):
                child1.setText(i, node_name.split('_', maxsplit=1)[i])

    def click_tree(self):
        item = self.currentItem()
        data = item.data(0, Qt.UserRole)
        if data:
            self.current_filename = data
        else:
            self.current_filename = item.text(0)
        print(self.current_filename)

    def add_node(self, namelist):
        print('--- addTreeNodeBtn ---')
        item = self.currentItem()
        node = QTreeWidgetItem(item)
        for i in range(len(namelist)):
            node.setText(i, namelist[i])

    def modify_node(self, new_name_list):
        print('--- updateTreeNodeBtn ---')
        item = self.currentItem()
        for i in range(len(new_name_list)):
            item.setText(i, new_name_list[i])

    def delete_node(self):
        print('--- delTreeNodeBtn ---')
        root = self.invisibleRootItem()
        for item in self.selectedItems():
            (item.parent() or root).removeChild(item)


class FileTree(QWidget):

    def __init__(self, parent=None):
        self.work_path = None
        super(FileTree, self).__init__(parent)
        self.filepath = None
        self.tree = MyTree(['文件管理'], [])
        self.root = QTreeWidgetItem(self.tree)
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.addLayout(self.get_file_operations_layout())

        main_layout.addWidget(self.tree)

        widget = QWidget()
        widget.setLayout(main_layout)
        QApplication.processEvents()
        self.setLayout(main_layout)

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
        if self.work_path:
            self.tree.update_tree(self.root)
        self.work_path = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")
        self.get_root_child()
        self.tree.expandAll()

    def get_root_child(self):
        dirs = os.listdir(self.work_path)
        file_info = QFileInfo(self.work_path)
        file_icon = QFileIconProvider()
        icon = QIcon(file_icon.icon(file_info))

        self.root.setText(0, self.work_path.split('/')[-1])
        self.root.setIcon(0, QIcon(icon))
        self.root.setData(0, Qt.UserRole, self.work_path)
        self.tree.addTopLevelItem(self.root)
        self.render_file_tree(dirs, self.root, self.work_path)

    def render_file_tree(self, dirs, root, path):
        for dir in dirs:
            child = QTreeWidgetItem(root)
            child.setText(0, dir)
            path_new = path + '/' + dir
            child.setIcon(0, QIcon(QIcon(QFileIconProvider().icon(QFileInfo(path_new)))))
            child.setData(0, Qt.UserRole, os.path.join(self.work_path, path_new))
            if os.path.isdir(path_new):
                dirs_new = os.listdir(path_new)
                self.render_file_tree(dirs_new, child, path_new)

    def rename(self, item):
        text, ok = QInputDialog.getText(self, "Rename", "Rname this file by string :", QLineEdit.Normal, "")
        if ok and text != '':
            item.setText(0, text)

    def click_tree(self):
        item = self.tree.currentItem()
        file_name = ""
        root = self.tree.invisibleRootItem()
        print(root.parent())
        # print(item.parent())
        print(self.work_path, item.text(0))

        while item.parent() is None:
            print("parent:", item.parent.text(0))
        # while True:
        # if not item.parent():
        # break
        # file_name = os.path.join(item.text(0), file_name)

        # print(file_name)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tree = FileTree()
    tree.show()
    sys.exit(app.exec_())

# *_*coding:utf-8 *_*
__Author__ = 'xiaohan'
from time import sleep

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Mytree(QTreeWidget):
    def __init__(self, headerslist, nodesnamelist, parrent=None):
        super(Mytree, self).__init__(parrent)
        self.nodesnamelist = nodesnamelist
        self.headerslist = headerslist
        self.setWindowTitle('My Browser')
        self.showMaximized()
        # self.setWindowFlags(Qt.FramelessWindowHint)# 无边框

        self.setFont(QFont("Consolas", 12, QFont.Normal, False))
        self.headerItem().setFont(0, QFont("Consolas", 12, QFont.Normal,
                                           False))  # 设置treewidget头字体格式
        self.setColumnCount(len(self.headerslist))  # 设置列数
        self.setHeaderLabels(self.headerslist)  # 设置头的标题
        self.root = QTreeWidgetItem(self)
        self.root.setText(0, 'root')
        self.addTopLevelItem(self.root)
        self.expandAll()
        self.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.setDragDropOverwriteMode(True)
        self.setEnabled(True)
        # self.setItemDelegateForColumn(1, EmptyDelegate(self))  # 设置第二列不可编辑
        self.setDragEnabled(True)
        # self.tree.expandAll()
        self.clicked.connect(self.onTreeClicked)

    def update(self):
        self.takeChildren()
        self.get_tree_nodes()

    def get_tree_nodes(self):
        for nodename in self.nodesnamelist:
            child1 = QTreeWidgetItem(self.root)
            for i in range(len(self.headerslist)):
                child1.setText(i, nodename.split('_', maxsplit=1)[i])

    def onTreeClicked(self, index):
        item = self.currentItem()
        if item.parent():
            print(item.text(0), item.text(1))

    def addTreeNodeBtn(self):
        print('--- addTreeNodeBtn ---')
        item = self.tree.currentItem()
        node = QTreeWidgetItem(item)
        node.setText(0, 'newNode')
        node.setText(1, '10')

    def updateTreeNodeBtn(self):
        print('--- updateTreeNodeBtn ---')
        item = self.tree.currentItem()
        item.setText(0, 'updateNode')
        item.setText(1, '20')

    def delTreeNodeBtn(self):
        print('--- delTreeNodeBtn ---')
        item = self.tree.currentItem()
        root = self.tree.invisibleRootItem()
        for item in self.tree.selectedItems():
            (item.parent() or root).removeChild(item)

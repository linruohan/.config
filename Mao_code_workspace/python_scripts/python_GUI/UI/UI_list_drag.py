# -*-coding:utf-8-*-
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class DropInList(QListWidget):
    def __init__(self):
        super(DropInList, self).__init__()
        self.setAcceptDrops(True)  # 开启接受拖入事件

    def dropEvent(self, QDropEvent):
        source_Widget = QDropEvent.source()  # 获取拖入元素的父组件
        items = source_Widget.selectedItems()
        for i in items:
            source_Widget.takeItem(source_Widget.indexFromItem(i).row())  # 通过实时计算选中的item的索引来删除listItem
            self.addItem(i)
        print('有东西拖入')


class MainWidget(QWidget):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.setWindowTitle('检测拖入')
        self.main_layout = QHBoxLayout()
        self.left_widget = DropInList()
        self.right_widget = QListWidget()
        pre_list = ['a 123123123', 'b12312', 'c12312', 'd123123123']
        self.right_widget.addItems(pre_list)
        self.right_widget.setDragEnabled(True)  # 开启拖出功能
        self.right_widget.setDragDropMode(self.right_widget.InternalMove)  # 支持内部拖拽

        self.right_widget.setDragDropOverwriteMode(False)  # 不能拖入
        self.right_widget.setSelectionMode(QAbstractItemView.ExtendedSelection)  # 开启多选模式
        self.right_widget.setDefaultDropAction(Qt.MoveAction)  # 设置drop事件默认为移动事件
        self.main_layout.addWidget(self.left_widget)
        self.main_layout.addWidget(self.right_widget)
        self.setLayout(self.main_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = MainWidget()
    m.show()
    sys.exit(app.exec_())

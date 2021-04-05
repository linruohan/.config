# *_*coding:utf-8 *_*
__Author__ = 'xiaohan'

import sys
from time import sleep

from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QAbstractItemView, QApplication, QCalendarWidget, QComboBox, QCompleter, QHBoxLayout, \
    QItemDelegate, QLabel, QLineEdit, QSlider, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget


class EmptyDelegate(QItemDelegate):

    def __init__(self, parent):
        super(EmptyDelegate, self).__init__(parent)

    def createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex):
        return None


class MyTree(QTreeWidget):

    def __init__(self, header_list, node_name_list, parent=None):
        super(MyTree, self).__init__(parent)
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
        self.clicked.connect(self.click_tree)

    def update_tree(self):
        # self.root.takeChildren() # QTreeWidgetItem::takeChildren() //删除所有子列表项
        # self.root.removeChild(self.currentItem()) //删除指定子列表项,参数为:QTreeWidgetItem
        # self.root.takeChild(index) //删除指定索引的子列表项
        # self.root.addChild(QTreeWidgetItem * child) //添加子列表项
        # self.root.addChildren(const QList<QTreeWidgetItem *> & children) //添加多条子列表项
        self.root.takeChildren()
        sleep(1)
        self.get_tree_nodes()

    def get_tree_nodes(self):
        for node_name in self.node_name_list:
            child1 = QTreeWidgetItem(self.root)
            for i in range(len(self.headerslist)):
                child1.setText(i, node_name.split('_', maxsplit=1)[i])

    def click_tree(self):
        item = self.currentItem()
        if item.parent():
            print(item.text(0))

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


class MyCalendar(QWidget):
    def __init__(self, parent=None):
        super(MyCalendar, self).__init__(parent)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.cal = QCalendarWidget(self)
        self.cal.setGridVisible(True)
        self.cal.selectionChanged.connect(self.showDate)
        self.label = QLabel(self)
        date = self.cal.selectedDate()
        self.label.setText(str(date.toPyDate()))
        vbox = QVBoxLayout()
        vbox.addWidget(self.cal)
        vbox.addWidget(self.label)
        self.setLayout(vbox)

    def show_date(self):
        date = self.cal.selectedDate()
        self.label.setText(str(date.toPyDate()))


class MyProcessBar(QWidget):
    def __init__(self):
        super(MyProcessBar, self).__init__()
        layout = QHBoxLayout()
        self.setLayout(layout)
        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)  # 设置初始位置
        sld.setTickInterval(5)
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.change_value)  # 绑定信号
        self.label = QLabel('0%')
        layout.addWidget(sld)
        layout.addWidget(self.label)

    @property
    def value(self):
        return self.label.text()

    def change_value(self, value):
        self.label.setText(str(value) + '%')


class CompletionQComboBox(QComboBox):
    def __init__(self, items_list, *args, **kwargs):
        super(CompletionQComboBox, self).__init__(*args, **kwargs)
        self.setMinimumWidth(200)
        self.setEditable(True)
        self.items_list = items_list
        self.name = None
        # 增加选项元素
        for i in range(len(self.items_list)):
            self.addItem(self.items_list[i])
        self.setCurrentIndex(-1)
        self.setCompleter(self.get_completer(self.items_list))
        # 增加选中事件
        self.combobox.activated.connect(self.on_combobox_Activate)

    def get_completer(self, items_list, pipeiMode=Qt.MatchContains, buquanMode=QCompleter.PopupCompletion):
        completer = QCompleter(items_list)
        # 设置匹配模式  有三种：
        # Qt.MatchStartsWith 开头匹配（默认）
        # Qt.MatchContains 内容匹配
        # Qt.MatchEndsWith 结尾匹配
        completer.setFilterMode(pipeiMode)
        # 设置补全模式  有三种：
        # QCompleter.PopupCompletion（默认）根据输入字符显示匹配项的下拉列表(区分大小写)
        # QCompleter.InlineCompletion 根据输入字符,在行内显示匹配的项(区分大小写)
        # QCompleter.UnfilteredPopupCompletion 任意输入,显示所有项下拉列表
        completer.setCompletionMode(buquanMode)
        return completer

    def on_combobox_Activate(self, index):
        """获取combobox的内容和索引"""
        # print("counts: ", self.combobox.count())
        # print("currentIndex: ", self.combobox.currentIndex())
        # print("currentText: ", self.combobox.currentText())
        # print("currentData: ", self.combobox.currentData())
        # print("itemData: ", self.combobox.itemData(self.combobox.currentIndex()))
        # print("itemText: currentIndex  ", self.combobox.itemText(self.combobox.currentIndex()))
        # print("itemText: index", self.combobox.itemText(index))
        self.name = self.currentText()


class CompletionQLineEdit(QLineEdit):
    items_list = ["C", "C++", "Java", "Python", "JavaScript", "C#", "Swift", "go", "Ruby", "Lua", "PHP"]

    def __init__(self, items_list, *args, **kwargs):
        super(CompletionQLineEdit, self).__init__(*args, **kwargs)
        layout = QHBoxLayout(self)
        self.setMinimumWidth(200)
        self.items_list = items_list
        self.setCompleter(self.get_completer(self.items_list))

    def get_completer(self, items_list, pipeiMode=Qt.MatchContains, buquanMode=QCompleter.PopupCompletion):
        completer = QCompleter(items_list)
        # 设置匹配模式  有三种：
        # Qt.MatchStartsWith 开头匹配（默认）
        # Qt.MatchContains 内容匹配
        # Qt.MatchEndsWith 结尾匹配
        completer.setFilterMode(pipeiMode)
        # 设置补全模式  有三种：
        # QCompleter.PopupCompletion（默认）根据输入字符显示匹配项的下拉列表(区分大小写)
        # QCompleter.InlineCompletion 根据输入字符,在行内显示匹配的项(区分大小写)
        # QCompleter.UnfilteredPopupCompletion 任意输入,显示所有项下拉列表
        completer.setCompletionMode(buquanMode)
        return completer


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MyProcessBar()
    ui.show()
    sys.exit(app.exec_())

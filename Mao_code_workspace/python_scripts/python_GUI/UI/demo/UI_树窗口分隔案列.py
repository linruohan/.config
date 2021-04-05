# coding=utf-8
import sys
from PyQt5.QtWidgets import (QHBoxLayout, QFrame, QSplitter, QStackedWidget,
                             QWidget, QApplication, QTreeWidget,
                             QAbstractItemView, QTreeWidgetItem, QLabel,
                             QSizePolicy)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from UI_base import UI_base
'''stackedWidget + QFrame + Qtree +QSplitter
树叶签 的tab实例
'''


class Example(UI_base):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)
        left = QFrame(self)
        left.setFrameShape(QFrame.StyledPanel)
        # 添加StyledPanel样式能使QFrame 控件之间的界限更加明显

        right = QFrame(self)
        right.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(left)
        splitter1.setSizes([
            20,
        ])
        # 设置分隔条位置
        splitter1.addWidget(right)

        hbox.addWidget(splitter1)
        self.addLayout(hbox, 1, 0, 10, 5)
        self.get_tree(left)
        self.create(right)

    def create(self, stack):

        self.form1 = self.get_form("增加")
        self.form2 = self.get_form("查询")
        self.stackedWidget = QStackedWidget(stack)  # 设置stackedWidget
        # 将两个面板，加入stackedWidget
        self.stackedWidget.addWidget(self.form1)
        self.stackedWidget.addWidget(self.form2)

        # 窗口最大化
        self.showMaximized()
        self.setWindowTitle('树窗口分隔案列')
        self.show()

    def get_tree(self, parent):
        # 树
        self.tree = QTreeWidget(parent)
        self.tree.setStyleSheet(
            "background-color:#eeeeee;border:outset;color:#215b63;")
        self.tree.setAutoScroll(True)
        self.tree.setEditTriggers(QAbstractItemView.DoubleClicked
                                  | QAbstractItemView.EditKeyPressed)
        self.tree.setTextElideMode(Qt.ElideMiddle)
        # self.tree.setIndentation(30)
        self.tree.setRootIsDecorated(True)
        self.tree.setUniformRowHeights(False)
        self.tree.setItemsExpandable(True)
        self.tree.setAnimated(False)
        self.tree.setHeaderHidden(True)
        self.tree.setExpandsOnDoubleClick(True)
        self.tree.setObjectName("tree")

        # 设置根节点
        root = QTreeWidgetItem(self.tree)
        root.setText(0, '系统管理')
        # 设置树形控件的列的宽度
        self.tree.setColumnWidth(0, 150)
        # 设置子节点1
        child1 = QTreeWidgetItem()
        child1.setText(0, '增加人员信息')
        root.addChild(child1)
        # 设置子节点2
        child2 = QTreeWidgetItem(root)
        child2.setText(0, '查询人员信息')
        self.tree.addTopLevelItem(root)  # 加载根节点的所有属性与子控件
        self.tree.clicked.connect(self.onClicked)  # 树节点监听事件
        self.tree.expandAll()

    def get_form(self, name, fontname="Consolas", fontsize=10):
        """批量创建form表单"""
        # 设置第一个面板
        form = QWidget()
        formLayout = QHBoxLayout(form)
        label = QLabel()
        label.setText(name)
        label.setSizePolicy(
            QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        label.setAlignment(Qt.AlignCenter)
        label.setFont(QFont(fontname, fontsize, QFont.Bold))
        formLayout.addWidget(label)
        return form

    def onClicked(self, qmodeLindex):
        item = self.tree.currentItem()
        print('Key=%s,value=%s' % (item.text(0), item.text(1)))
        if item.text(0) == '增加人员信息':
            self.on1_clicked()
        elif item.text(0) == '查询人员信息':
            self.on2_clicked()
        else:
            print('返回主界面')

    def on1_clicked(self):
        self.stackedWidget.setCurrentIndex(0)

    def on2_clicked(self):
        self.stackedWidget.setCurrentIndex(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

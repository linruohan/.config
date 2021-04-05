import os
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from threading import Thread

class Mytree(QTreeWidget):

    def __init__(self, headerslist, nodesnamelist, parrent=None):
        super(Mytree, self).__init__(parrent)
        self.nodesnamelist = nodesnamelist
        self.headerslist = headerslist
        self.setWindowTitle('My file Browser')
        self.showMaximized()
        # self.setWindowFlags(Qt.FramelessWindowHint)# 无边框
        self.setFont(QFont("Consolas", 12, QFont.Normal, False))
        self.headerItem().setFont(0, QFont("Consolas", 12, QFont.Normal, False))  # 设置treewidget头字体格式
        self.setColumnCount(len(self.headerslist))  # 设置列数
        self.setHeaderLabels(self.headerslist)  # 设置头的标题
        self.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.setDragDropOverwriteMode(True)
        self.setEnabled(True)
        # self.setItemDelegateForColumn(1, EmptyDelegate(self))  # 设置第二列不可编辑
        self.setDragEnabled(True)
        self.clicked.connect(self.onTreeClicked)

    def onTreeClicked(self, index):
        item = self.currentItem()
        if item.parent():
            print(item.text(0), item.text(1))

class Ui_MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        self.setObjectName("MainWindow")
        self.initUI()

    def initUI(self):
        self.mainLayout = QGridLayout()

        self.tree = Mytree(['filepath'], [])

        self.splitter1 = QSplitter(Qt.Vertical)
        operator=QWidget()
        operator.setLayout(self.operator_UI())
        self.splitter1.addWidget(operator)
        self.splitter1.addWidget(self.tree)
        # self.mainLayout.addWidget(self.splitter1,0, 0, 8, 2)
        widget = QWidget()
        widget.setLayout(self.mainLayout)
        QApplication.processEvents()
        self.setCentralWidget(widget)

        self.setGeometry(300, 500, 800, 600)
        self.setWindowTitle('小寒编辑器')

    def operator_UI(self):
        operatorLayout = QHBoxLayout()
        settingWorkPathBtn = QPushButton("设置工作路径")
        addBtn = QPushButton("新建")
        modifyBtn = QPushButton("修改")
        delBtn = QPushButton("删除")
        operatorLayout.addWidget(settingWorkPathBtn)
        operatorLayout.addWidget(addBtn)
        operatorLayout.addWidget(modifyBtn)
        operatorLayout.addWidget(delBtn)
        # 按钮的信号槽连接
        settingWorkPathBtn.clicked.connect(self.settingWorkPath)
        addBtn.clicked.connect(self.new)
        modifyBtn.clicked.connect(self.modify)
        delBtn.clicked.connect(self.delete)
        return operatorLayout

    def settingWorkPath(self):
        '''设置工作路径'''
        self.workpath = QFileDialog.getExistingDirectory(self, "设置工作路径", "./")
        self.get_root_child()

    def new(self):
        """新增节点"""
        fname = QFileDialog.getSaveFileName(self, "Write File", self.workpath, "All (*.*)")
        if fname[0]:
            with open(fname[0], 'w') as f: f.write('')
            self.update_thread()

    def modify(self):
        item = self.tree.currentItem()
        text, okPressed = QInputDialog.getText(self, "Rename", "Rname this file by string :", QLineEdit.Normal, "")
        if okPressed and text != '':
            item.setText(0,text)

    def update_thread(self):
        t = Thread(target=self.update)
        t.start()

    def update(self):
        self.root.takeChildren()
        self.get_root_child()

    def delete(self):
        item = self.tree.currentItem()
        root = self.tree.invisibleRootItem()
        for item in self.tree.selectedItems():
            (item.parent() or root).removeChild(item)

    def get_root_child(self):
        dirs = os.listdir(self.workpath)
        fileInfo = QFileInfo(self.workpath)
        fileIcon = QFileIconProvider()
        icon = QIcon(fileIcon.icon(fileInfo))
        self.root = QTreeWidgetItem(self.tree)
        self.root.setText(0, self.workpath.split('/')[-1])
        self.root.setIcon(0, QIcon(icon))
        self.CreateTree(dirs, self.root, self.workpath)
        # self.tree.expandAll()

    def CreateTree(self, dirs, root, path):
        for i in dirs:
            path_new = path + '\\' + i
            if os.path.isdir(path_new):
                fileInfo = QFileInfo(path_new)
                fileIcon = QFileIconProvider()
                icon = QIcon(fileIcon.icon(fileInfo))
                child = QTreeWidgetItem(root)
                child.setText(0, i)
                child.setIcon(0, QIcon(icon))
                dirs_new = os.listdir(path_new)
                self.CreateTree(dirs_new, child, path_new)
            else:
                fileInfo = QFileInfo(path_new)
                fileIcon = QFileIconProvider()
                icon = QIcon(fileIcon.icon(fileInfo))
                child = QTreeWidgetItem(root)
                child.setText(0, i)
                child.setIcon(0, QIcon(icon))

    def open(self):
        filename = QFileDialog.getOpenFileName(self, 'open file')
        with open(filename[0], 'r') as f:
            my_txt = f.read()
            self.textEdit.setPlainText(my_txt)

    def save(self):
        filename = QFileDialog.getSaveFileName(self, 'save file')
        with open(filename[0], 'w') as f:
            my_text = self.textEdit.toPlainText()
            f.write(my_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())

# *_*coding:utf-8 *_*
__Author__ = 'xiaohan'

import os
import sys

from PyQt5.QtCore import QFileInfo, Qt
from PyQt5.QtGui import QFont, QIcon, QKeySequence, QTextCursor
from PyQt5.QtWidgets import QAction, QApplication, QFileDialog, QHBoxLayout, QMainWindow, QMessageBox, QSplitter, \
    QWidget

from UI_file_tree import FileTree
from UI_vscodeEditor import ViewCode


class UIMain(QMainWindow):

    def __init__(self, parent=None):
        super(UIMain, self).__init__(parent)
        font = QFont("Courier", 11)
        font.setFixedPitch(True)
        self.resize(800, 600)
        self.setWindowTitle("Python Editor")
        self.widget = QWidget()
        self.layout = QHBoxLayout()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        self.code_view = ViewCode()
        self.file_tree = FileTree()
        self.file_tree.tree.clicked.connect(self.open_tree_file)
        # 向Splitter内添加控件。并设置游戏的初始大小
        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(self.file_tree)
        splitter1.setSizes([100, 200])
        # 实例化Splitter管理器，添加控件到其中，设置垂直方向
        self.splitter = QSplitter(Qt.Horizontal)
        self.splitter.addWidget(splitter1)
        self.splitter.addWidget(self.code_view)
        # 设置窗体全局布局以及子布局的添加
        self.layout.addWidget(self.splitter)
        self.menu_action()
        QApplication.clipboard().dataChanged.connect(self.updateUi)

        self.filename = None
        self.updateUi()

    def menu_action(self):
        status = self.statusBar()
        status.setSizeGripEnabled(False)
        status.showMessage("Ready", 5000)
        file_new_action = self.createAction("&New...", self.fileNew,
                                          QKeySequence.New, "filenew", "Create a Python file")
        file_open_action = self.createAction("&Open...", self.open,
                                           QKeySequence.Open, "fileopen",
                                           "Open an existing Python file")
        self.file_save_action = self.createAction("&Save", self.save_code,
                                                QKeySequence.Save, "filesave", "Save the file")
        self.file_save_as_action = self.createAction("Save &As...",
                                                  self.save_code, icon="filesaveas",
                                                  tip="Save the file using a new name")
        file_quit_action = self.createAction("&Quit", self.close,
                                           "Ctrl+Q", "filequit", "Close the application")
        self.editCopyAction = self.createAction("&Copy",
                                                self.code_view.copy, QKeySequence.Copy, "editcopy",
                                                "Copy text to the clipboard")
        self.editCutAction = self.createAction("Cu&t", self.code_view.cut,
                                               QKeySequence.Cut, "editcut",
                                               "Cut text to the clipboard")
        self.editPasteAction = self.createAction("&Paste",
                                                 self.code_view.paste, QKeySequence.Paste, "editpaste",
                                                 "Paste in the clipboard's text")
        self.editIndentAction = self.createAction("&Indent",
                                                  self.editIndent, "Ctrl+]", "editindent",
                                                  "Indent the current line or selection")
        self.editUnindentAction = self.createAction("&Unindent",
                                                    self.editUnindent, "Ctrl+[", "editunindent",
                                                    "Unindent the current line or selection")

        file_menu = self.menuBar().addMenu("&File")
        self.addActions(file_menu, (file_new_action, file_open_action,
                                   self.file_save_action, self.file_save_as_action, None,
                                   file_quit_action))
        edit_menu = self.menuBar().addMenu("&Edit")
        self.addActions(edit_menu, (
            self.editCopyAction,
            self.editCutAction,
            self.editPasteAction,
            None,
            self.editIndentAction,
            self.editUnindentAction
        ))
        file_toolbar = self.addToolBar("File")
        file_toolbar.setObjectName("FileToolBar")
        self.addActions(file_toolbar, (file_new_action, file_open_action,
                                      self.file_save_action))
        edit_toolbar = self.addToolBar("Edit")
        edit_toolbar.setObjectName("EditToolBar")
        self.addActions(edit_toolbar, (
            self.editCopyAction,
            self.editCutAction,
            self.editPasteAction,
            None,
            self.editIndentAction,
            self.editUnindentAction
        ))

    def connect(self):
        self.code_view.selectionChanged.connect(self.updateUi)
        self.code_view.document().modificationChanged.connect(self.updateUi)

    def updateUi(self, arg=None):
        # self.file_save_action.setEnabled(
        #         self.code_view.document().isModified())
        # self.file_save_action.setEnabled(True)
        # enable = not self.code_view.document().isEmpty()
        enable = True
        self.file_save_as_action.setEnabled(enable)
        self.editIndentAction.setEnabled(enable)
        self.editUnindentAction.setEnabled(enable)
        # enable = self.code_view.textCursor().hasSelection()
        self.editCopyAction.setEnabled(enable)
        self.editCutAction.setEnabled(enable)
        # self.editPasteAction.setEnabled(self.code_view.canPaste())

    def createAction(self, text, slot=None, shortcut=None, icon=None,
                     tip=None, checkable=False, signal="triggered()"):
        action = QAction(text, self)
        if icon is not None:
            action.setIcon(QIcon("./images/{0}.png".format(icon)))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            action.triggered.connect(slot)
        if checkable:
            action.setCheckable(True)
        return action

    def addActions(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)

    def closeEvent(self, event):
        if not self.okToContinue():
            event.ignore()

    def okToContinue(self):
        if True:
            reply = QMessageBox.question(self,
                                         "Editor - Unsaved Changes",
                                         "Save unsaved changes?",
                                         QMessageBox.Yes | QMessageBox.No |
                                         QMessageBox.Cancel)
            if reply == QMessageBox.Cancel:
                return False
            elif reply == QMessageBox.Yes:
                self.save_code()
        return True

    def fileNew(self):
        self.filename = None
        self.setWindowTitle("Python Editor - Unnamed")
        self.updateUi()

    def open(self):
        if not self.filename:
            self.filename = str(QFileDialog.getOpenFileName(self,
                                                            "Python Editor - Choose File", '.', "all files(*.*)")[0])

    def open_tree_file(self):
        item = self.file_tree.tree.currentItem()
        data = item.data(0, Qt.UserRole)
        self.filename = data if data else item.text(0)
        if os.path.isfile(self.filename):
            self.code_view.filename = self.filename
            self.code_view.set_value(self.get_code())
            print(f'load_file success: [{os.path.basename(self.filename)}] ')
            self.setWindowTitle("Python Editor - {0}".format(
                QFileInfo(self.filename).fileName()))

    def get_code(self):
        with open(self.filename, encoding='utf-8') as f:
            print(f"read success: [{os.path.basename(self.filename)}] ")
            return f.read()

    def save_code(self):
        def func(code):
            if not self.filename:
                filename, filetype = QFileDialog.getSaveFileName(self,
                                                                 "Python Editor -- Save File As", '.',
                                                                 "all files(*.*)")
                if filename:
                    self.filename = filename
                    self.setWindowTitle("Python Editor - {0}".format(
                        QFileInfo(self.filename).fileName()))
            with open(self.filename, "w", encoding='utf-8') as f:
                print(f"save success: [{os.path.basename(self.filename)}]")
                f.write(code)

        self.code_view.get_value(func)

    def editIndent(self):
        cursor = self.code_view.textCursor()
        cursor.beginEditBlock()
        if cursor.hasSelection():
            start = pos = cursor.anchor()
            end = cursor.position()
            if start > end:
                start, end = end, start
                pos = start
            cursor.clearSelection()
            cursor.setPosition(pos)
            cursor.movePosition(QTextCursor.StartOfLine)
            while pos <= end:
                cursor.insertText("    ")
                cursor.movePosition(QTextCursor.Down)
                cursor.movePosition(QTextCursor.StartOfLine)
                pos = cursor.position()
            cursor.setPosition(start)
            cursor.movePosition(QTextCursor.NextCharacter,
                                QTextCursor.KeepAnchor, end - start)
        else:
            pos = cursor.position()
            cursor.movePosition(QTextCursor.StartOfBlock)
            cursor.insertText("    ")
            cursor.setPosition(pos + 4)
        cursor.endEditBlock()

    def editUnindent(self):
        cursor = self.code_view.textCursor()
        cursor.beginEditBlock()
        if cursor.hasSelection():
            start = pos = cursor.anchor()
            end = cursor.position()
            if start > end:
                start, end = end, start
                pos = start
            cursor.setPosition(pos)
            cursor.movePosition(QTextCursor.StartOfLine)
            while pos <= end:
                cursor.clearSelection()
                cursor.movePosition(QTextCursor.NextCharacter,
                                    QTextCursor.KeepAnchor, 4)
                if cursor.selectedText() == "    ":
                    cursor.removeSelectedText()
                cursor.movePosition(QTextCursor.Down)
                cursor.movePosition(QTextCursor.StartOfLine)
                pos = cursor.position()
            cursor.setPosition(start)
            cursor.movePosition(QTextCursor.NextCharacter,
                                QTextCursor.KeepAnchor, end - start)
        else:
            cursor.clearSelection()
            cursor.movePosition(QTextCursor.StartOfBlock)
            cursor.movePosition(QTextCursor.NextCharacter,
                                QTextCursor.KeepAnchor, 4)
            if cursor.selectedText() == "    ":
                cursor.removeSelectedText()
        cursor.endEditBlock()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/main.ico"))
    form = UIMain()
    form.show()
    app.exec_()

# *_*coding:utf-8 *_*
__Author__ = 'xiaohan'

import os
import sys

from PyQt5.QtCore import QFileInfo
from PyQt5.QtGui import QFont, QIcon, QKeySequence, QTextCursor
from PyQt5.QtWidgets import QAction, QApplication, QFileDialog, QGridLayout, QMainWindow, QMessageBox, QPushButton, \
    QTextBrowser, QWidget


from components.viewCode import ViewCode


class UI_vscode(QMainWindow):

    def __init__(self, parent=None):
        super(UI_vscode, self).__init__(parent)

        font = QFont("Courier", 11)
        font.setFixedPitch(True)
        self.widget = QWidget()
        self.main_layout = QGridLayout()
        self.code_view = ViewCode()
        self.code_view.save_btn.clicked.connect(self.save_code)
        self.tree = QPushButton("测试")
        self.browser = QTextBrowser()
        self.main_layout.addWidget(self.browser, 0, 0, 1, 1)
        self.main_layout.addWidget(self.code_view, 1, 3, 5, 5)
        self.widget.setLayout(self.main_layout)
        self.setCentralWidget(self.widget)

        status = self.statusBar()
        status.setSizeGripEnabled(False)
        status.showMessage("Ready", 5000)

        fileNewAction = self.createAction("&New...", self.fileNew,
                                          QKeySequence.New, "filenew", "Create a Python file")
        fileOpenAction = self.createAction("&Open...", self.fileOpen,
                                           QKeySequence.Open, "fileopen",
                                           "Open an existing Python file")
        self.fileSaveAction = self.createAction("&Save", self.save,
                                                QKeySequence.Save, "filesave", "Save the file")
        self.fileSaveAsAction = self.createAction("Save &As...",
                                                  self.save, icon="filesaveas",
                                                  tip="Save the file using a new name")
        fileQuitAction = self.createAction("&Quit", self.close,
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
        # self.editIndentAction = self.createAction("&Indent",
        #                                           self.editIndent, "Ctrl+]", "editindent",
        #                                           "Indent the current line or selection")
        # self.editUnindentAction = self.createAction("&Unindent",
        #                                             self.editUnindent, "Ctrl+[", "editunindent",
        #                                             "Unindent the current line or selection")

        fileMenu = self.menuBar().addMenu("&File")
        self.addActions(fileMenu, (fileNewAction, fileOpenAction,
                                   self.fileSaveAction, self.fileSaveAsAction, None,
                                   fileQuitAction))
        editMenu = self.menuBar().addMenu("&Edit")
        self.addActions(editMenu, (
            self.editCopyAction,
            self.editCutAction,
            self.editPasteAction,
            None,
            # self.editIndentAction,
            # self.editUnindentAction
        ))
        fileToolbar = self.addToolBar("File")
        fileToolbar.setObjectName("FileToolBar")
        self.addActions(fileToolbar, (fileNewAction, fileOpenAction,
                                      self.fileSaveAction))
        editToolbar = self.addToolBar("Edit")
        editToolbar.setObjectName("EditToolBar")
        self.addActions(editToolbar, (
            self.editCopyAction,
            self.editCutAction,
            self.editPasteAction,
            None,
            # self.editIndentAction,
            # self.editUnindentAction
        ))

        QApplication.clipboard().dataChanged.connect(self.updateUi)

        self.resize(800, 600)
        self.setWindowTitle("Python Editor")
        self.filename = None
        self.updateUi()

    def connect(self):
        self.code_view.selectionChanged.connect(self.updateUi)
        self.code_view.document().modificationChanged.connect(self.updateUi)

    def updateUi(self, arg=None):
        # self.fileSaveAction.setEnabled(
        #         self.code_view.document().isModified())
        # self.fileSaveAction.setEnabled(True)
        # enable = not self.code_view.document().isEmpty()
        enable = True
        self.fileSaveAsAction.setEnabled(enable)
        # self.editIndentAction.setEnabled(enable)
        # self.editUnindentAction.setEnabled(enable)
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
                return self.fileSave()
        return True

    def fileNew(self):
        self.filename = None
        self.setWindowTitle("Python Editor - Unnamed")
        self.updateUi()

    def fileOpen(self):
        dir = (os.path.dirname(self.filename)
               if self.filename is not None else ".")
        fname = str(QFileDialog.getOpenFileName(self,
                                                "Python Editor - Choose File", dir,
                                                "all files(*.*)")[0])
        if fname:
            self.filename = fname
            self.code_view.set_value(self.get_code())
            print('load_file success')
            self.setWindowTitle("Python Editor - {0}".format(
                QFileInfo(self.filename).fileName()))

    def get_code(self):
        with open(self.filename, encoding='utf-8') as f:
            return f.read()

    def save(self):
        if self.filename is None:
            filename, filetype = QFileDialog.getSaveFileName(self,
                                                             "Python Editor -- Save File As", '.',
                                                             "all files(*.*)")
            if filename:
                self.filename = filename
                self.setWindowTitle("Python Editor - {0}".format(
                    QFileInfo(self.filename).fileName()))
        self.save_code()
        print("save success: ", self.filename)
        self.filename = None

    def save_code(self):
        def func(code):
            if not self.filename:
                return
            with open(self.filename, "w", encoding='utf-8') as f:
                f.write(code)

        self.code_view.get_value(func)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/main.ico"))
    form = UI_vscode()
    form.show()
    app.exec_()

from __future__ import division
import sys
from math import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Form(QDialog):
    # returnPressed=pyqtSignal()
    def __init__(self, parent=None):
        super(Form, self).__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.browser = QTextBrowser()
        self.lineedit = QLineEdit("please input some words:")
        self.lineedit.selectAll()
        layout = QVBoxLayout(self)

        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.lineedit.setFocus()
        self.lineedit.returnPressed.connect(self.updateUI)
        self.setWindowTitle('Calculate')

    def updateUI(self):
        try:
            text = str(self.lineedit.text())
            self.browser.append("%s=<b>%s</b>" % (text, eval(text)))
        except:
            self.browser.append(
                "<font color=red>%s is invalid!</font>" % text
            )

    def keyPressEvent(self, event):
        if event.modifiers () & Qt.ControlModifier:
            handled = False
            if event.key () == Qt.Key_B:
                self.toggleBold ()
                handled = True
            elif event.key () == Qt.Key_I:
                self.toggleItalic ()
                handled = True
            elif event.key () == Qt.Key_K:
                self.colorMenu ()
                handled = True
            elif event.key () == Qt.Key_M:
                self.textEffectMenu ()
                handled = True
            elif event.key () == Qt.Key_U:
                self.toggleUnderline ()
                handled = True
            if handled:
                event.accept ()
                return
        if event.key () in (Qt.Key_Enter, Qt.Key_Return):
            self.returnPressed.emit ()
            event.accept ()
        else:
            QTextEdit.keyPressEvent (self, event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Form()
    sys.exit(app.exec_())

# *_*coding:utf-8 *_* 
__Author__ = 'xiaohan'

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QCalendarWidget, QLabel, QVBoxLayout


class Calendar(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self)

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

    def showDate(self):
        date = self.cal.selectedDate()
        self.label.setText(str(date.toPyDate()))


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    qb = Calendar()
    qb.show()
    sys.exit(app.exec_())

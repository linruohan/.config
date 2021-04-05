from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor,QPixmap
from PyQt5.QtCore import Qt,QDate

import sys
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #日历控件
        cal=QCalendarWidget(self)
        cal.setGridVisible(False)#显示格线
        cal.move(80,80)
        cal.clicked[QDate].connect(self.showDate)

        self.lb1=QLabel(self)
        date=cal.selectedDate()
        self.lb1.setText(date.toString())
        self.lb1.move(30,60)

        self.setGeometry(300,300,380,370)
        self.setWindowTitle('toggle button')
        self.show()


    def showDate(self, date):
        self.lb1.setText(date.toString())



if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())

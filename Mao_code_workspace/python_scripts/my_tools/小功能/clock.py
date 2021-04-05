import sys,time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
    def initUI(self):
        try:
            due = QTime.currentTime ()
            message = "Alert!"
            if len (sys.argv) < 2:
                raise ValueError
            hours, mins = sys.argv[1].split (':')
            due = QTime (int (hours), int (mins))
            if not due.isValid ():
                raise ValueError
            if len (sys.argv) > 2:
                message = " ".join (sys.argv[2:])
        except ValueError:
            message = "Usage:alert.pyw HH:MM [optional message]"  # 24hr clcck
        while QTime.currentTime()<due:
            time.sleep(20)#20 seconds
        label=QLabel("<font color=red size=72><b>"+message +"</b></font>")
        h=QHBoxLayout(self)
        h.addWidget(label)

        self.setWindowFlags(Qt.SplashScreen)# no header 闪频模式
        QTimer.singleShot(2000,app.quit)#2 s  单次定时器



if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Example()
    window.show()
    sys.exit(app.exec_ ())
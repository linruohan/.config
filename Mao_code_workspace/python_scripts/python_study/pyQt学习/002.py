import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMessageBox, QDesktopWidget,QMainWindow,QAction,qApp,QTextEdit



class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        #文件编辑器部件.我们设置它为QMainWindow的中心部件.中心部件会占据所有的剩余区域.
        textEdit=QTextEdit()
        self.setCentralWidget(textEdit)

        # 一个QAction是一个菜单栏、工具栏或自定义键盘快捷键的动作被执行的抽象.
        # 在以上三行代码中,我们创建了一个动作,它指定了一个图标和一个Exit标签.而且还定义了一个快捷键.
        # 第三行代码创建了一个状态提示,当我们将鼠标放到这个菜单上的时候它会显示在状态栏上.
        exitAction=QAction(QIcon('setting.bmp'),'&exit',self)#图标
        exitAction.setShortcut('Ctrl+Q')#快捷键
        exitAction.setStatusTip('Exit application')#状态条
        exitAction.triggered.connect(qApp.quit)#动作绑定触发的信号
        #菜单栏--file
        menubar=self.menuBar()#实例化
        fileMenu=menubar.addMenu('&File')
        fileMenu.addAction(exitAction)#绑定动作
        #工具栏
        self.toobar=self.addToolBar('Exit')
        self.toobar.addAction(exitAction)


        #底部状态栏
        self.statusBar().showMessage('Ready to loading the file ....')
        #鼠标放置后显示的提示信息
        QToolTip.setFont(QFont('SansSerif'))
        self.setToolTip('this is a <b>Qwidget</b>widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('this is a <b>QPushButton</b>widget')
        btn.resize(btn.sizeHint())#设置为推荐大小
        btn.move(50, 50)

        btn1 = QPushButton('Quit', self)
        btn1.clicked.connect(QCoreApplication.instance().quit)
        btn1.resize(btn1.sizeHint())#设置为推荐大小
        btn1.move(100, 100)


        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.setWindowIcon(QIcon('1.jpg'))
        self.center()

        self.show()

    #重写closeEvent方法
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'message', 'Are you sure to quit?', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = Example()

    sys.exit(app.exec_())

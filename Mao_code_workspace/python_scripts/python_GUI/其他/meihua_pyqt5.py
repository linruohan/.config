import sys

import qtawesome
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtWidgets import QMainWindow


class Ui_MainWindow3(QMainWindow):
    def setupUi(self, Ui_MainWindow3):
        Ui_MainWindow3.setObjectName("Ui_MainWindow3")
        Ui_MainWindow3.resize(511, 367)
        # 设置标题和图标
        Ui_MainWindow3.setWindowTitle("语音识别")
        Ui_MainWindow3.setWindowIcon(QIcon('Amg.jpg'))  # 设置图标
        # qtawesome库里面有很多精美的图标 https://github.com/spyder-ide/qtawesome
        spin_icon = qtawesome.icon('fa5s.microphone-alt', color='black')
        # self.pushButton.setIcon(spin_icon)#设置图标
        Ui_MainWindow3.setWindowIcon(spin_icon)

        self.pushbutton_close = QtWidgets.QPushButton(Ui_MainWindow3)
        self.pushbutton_close.setGeometry(QtCore.QRect(30, 20, 30, 30))
        self.pushbutton_close.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Ui_MainWindow3)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 20, 30, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushbutton_mini = QtWidgets.QPushButton(Ui_MainWindow3)
        self.pushbutton_mini.setGeometry(QtCore.QRect(130, 20, 30, 30))
        self.pushbutton_mini.setObjectName("pushbutton_mini")
        self.text_label = QtWidgets.QLabel(Ui_MainWindow3)
        self.text_label.setGeometry(QtCore.QRect(80, 130, 351, 91))
        self.text_label.setObjectName("text_label")
        self.pushButton = QtWidgets.QPushButton(Ui_MainWindow3)
        self.pushButton.setGeometry(QtCore.QRect(190, 250, 101, 71))
        self.pushButton.setObjectName("pushbutton_close")
        self.pushbutton_close.clicked.connect(self.close)  # 关闭窗口
        self.pushbutton_mini.clicked.connect(self.showMinimized)  # 最小化窗口
        # self.pushbutton_close = QtWidgets.QPushButton(qtawesome.icon('fa5s.microphone',color='red'),"")
        self.label = QtWidgets.QLabel(Ui_MainWindow3)
        self.label.setGeometry(QtCore.QRect(80, 60, 351, 70))
        self.label.setObjectName("label")

        self.retranslateUi(Ui_MainWindow3)
        QtCore.QMetaObject.connectSlotsByName(Ui_MainWindow3)
        # 美化左上角的三个按钮。美化的效果就是圆形，红 黄 绿色 悬停时颜色会加深
        # QPushButton{background:#F76677;border-radius:15px;}  QPushButton是控件的属性，然后设置背景色background，设置边界半径（border-radius），注意这里要看原按钮大小，半径大了就没效果，小了不少圆形
        # setStyleSheet 就是用来美化的，使用的是qss。其实也就是css的美化方式。由于qt刚开始是用在c++后来有了pyqt用于python。这方面的官方文档基于python的目前还没有，直接跳转到c++的。
        # QPushButton:hover{background:red;} hover 意思就是当鼠标到按钮的时候，触发的，这里设置的就是颜色变深。

        self.pushbutton_close.setStyleSheet('''QPushButton{background:#F76677;border-radius:15px;}
QPushButton:hover{background:red;}''')
        self.pushButton_2.setStyleSheet('''QPushButton{background:#F7D674;border-radius:15px;}
QPushButton:hover{background:yellow;}''')
        self.pushbutton_mini.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:15px;}
QPushButton:hover{background:green;}''')
        # 美化中间靠上的label
        self.label.setStyleSheet(
            '''QLabel{color:white;font-size:40px;font-family:Roman times;}''')
        # 中间的label,除了设置字体颜色大小类型外，还设置了边界半径边界宽度，背景颜色等。
        self.text_label.setStyleSheet('''QLabel{color:darkGray;background:white;border:2px solid #F3F3F5;border-radius:45px;
                        font-size:14pt; font-weight:400;font-family: Roman times;} ''')
        # 对于label的设置还有 使字体居中显示
        self.text_label.setAlignment(Qt.AlignCenter)
        self.label.setAlignment(Qt.AlignCenter)
        # 最下面的按钮美化
        spin_icon = qtawesome.icon('fa5s.microphone-alt', color='white')
        self.pushButton.setIcon(spin_icon)  # 设置图标
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setStyleSheet('''QPushButton{border:none;}
        QPushButton:hover{color:white;
                    border:2px solid #F3F3F5;
                    border-radius:35px;
                    background:darkGray;}''')
        # 进度条的设置美化
        self.progressBar.setStyleSheet('''
            QProgressBar::chunk {
                background-color: darkgray;
            }''')  # 进度条跑的时候 颜色改变
        # 对于一个布局内的部分控件进行集体的美化，left_wideget可以看成是一个布局内的控件的集合
        self.left_widget.setStyleSheet('''
            QPushButton{border:none;color:white;padding-left:5px;
                    height:35px;
                    font-size:15px;
                    padding-right:10px;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:20px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QWidget#left_widget{
                background:Gray;
                border-top:1px solid white;
                border-bottom:1px solid white;
                border-left:1px solid white;
                border-top-left-radius:10px;
                border-bottom-left-radius:10px;
            }
            QPushButton#left_button:hover{ color:white;
                    border:2px solid #F3F3F5;
                    border-radius:15px;
                    background:black;}
        ''')

    def close(self):
        pass

    def showMinimized(self):
        pass

    def retranslateUi(self, Ui_MainWindow3):
        _translate = QtCore.QCoreApplication.translate
        Ui_MainWindow3.setWindowTitle(
            _translate("Ui_MainWindow3", "Ui_MainWindow3"))
        self.pushbutton_close.setText(_translate("Ui_MainWindow3", ""))
        self.pushButton_2.setText(_translate("Ui_MainWindow3", ""))
        self.pushbutton_mini.setText(_translate("Ui_MainWindow3", ""))
        self.pushButton.setText(_translate("Ui_MainWindow3", ""))
        self.label.setText(_translate("Ui_MainWindow3", "语音识别"))
        self.text_label.setText("点击下面的按钮开始录制音频\n再次点击停止录音开始识别")
        # 设置窗口透明度比较好看，原始的边框有点丑，可以给隐藏了，但是隐藏的后果是没法拖动，后面讲解决办法。
        # 使用setcolor 设置背景颜色。
        Ui_MainWindow3.setWindowOpacity(0.9)  # 设置窗口透明度
        # Ui_MainWindow3.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 设置窗口背景透明
        Ui_MainWindow3.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        pe = QPalette()
        Ui_MainWindow3.setAutoFillBackground(True)
        pe.setColor(QPalette.Window, Qt.lightGray)  # 设置背景色
        # pe.setColor(QPalette.Background,Qt.blue)
        Ui_MainWindow3.setPalette(pe)

    # 移动隐藏后的边框,当把边框给隐藏掉，边框将无法拖动移动，这个可以通过重写函数来实现。
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widgets = QtWidgets.QMainWindow()
    ui = Ui_MainWindow3()
    ui.setupUi(widgets)
    widgets.show()
    sys.exit(app.exec_())

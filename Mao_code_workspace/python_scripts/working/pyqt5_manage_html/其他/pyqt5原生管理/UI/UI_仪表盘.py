# *_*coding:utf-8 *_* 
__Author__ = 'xiaohan'

import sys

from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget


class CarInstrument(QWidget):
    def __init__(self):
        super().__init__()
        # self.setWindowFlags(Qt.FramelessWindowHint)  # 设置为无边框

        self.setspeedPointer()  # 创造指针
        self.getdim()  # 获取敏感尺寸
        self.resize(1920, 720)  # 设置为图片的大小
        # self.showMaximized()
        # self.setBackground()
        # self.setStyle("#border-image:url(:/imgs/仪表盘.png)")
        self.SetTimer()  # 开一个定时器来进行自动旋转演示

    # 初始化UI
    def setUI(self):
        pass

    def showMaximized(self):
        desktop = QApplication.desktop()
        rect = desktop.availableGeometry()
        self.setGeometry(rect)

    def SetTimer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.angle = 0
        self.timer.start(50)

    # 设置桌面背景
    def setBackground(self):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # 绘制图像反锯齿
        pix = QPixmap("imgs/仪表盘.png")
        pix = pix.scaled(self.width(), self.height(), Qt.KeepAspectRatio)
        painter.drawPixmap(self.rect(), pix)

    # #重写paintEvent
    def paintEvent(self, event):
        self.setBackground()
        self.angle += 1
        if (self.angle > 360):
            self.angle = 0
        self.drawspeedPoniter(self.angle)

    def setspeedPointer(self):
        self.pointer = QPixmap()  # 创建一个pixmap对象
        self.pointer.load("imgs/Pointery.png")

    # 速度指针
    def drawspeedPoniter(self, angle):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # 绘制图像反锯齿
        painter.translate(960, 350)  # 将坐标重新放置在窗口中央
        painter.save()
        painter.rotate(angle)
        # 计算大小以及坐标
        painter.drawPixmap(-self.pointer.width() / 2.8 / 2, -43, self.pointer.width() / 2.8,
                           self.pointer.height() / 2.8, self.pointer)
        painter.restore()

    # 计算尺寸
    def cdim(self):
        pass
        # widproportion =self.geometrywidth/self.pointer_width
        # hitproportion =self.geometryheight/self.pointer_height

    # 获取各种各样的尺寸
    def getdim(self):
        # 获取屏幕尺寸
        thisgeometry = self.geometry()
        self.geometrywidth = thisgeometry.width()
        self.geometryheight = thisgeometry.height()
        # 获取背景图片尺寸
        # self.back_width =self.pointer.width()
        # self.back_height=self.pointer.height()
        # 获取图标指针图片尺寸
        self.pointer_width = self.pointer.width()
        self.pointer_height = self.pointer.height()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CarInstrument()
    ex.show()
    sys.exit(app.exec_())

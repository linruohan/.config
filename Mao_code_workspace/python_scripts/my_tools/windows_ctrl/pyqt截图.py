# *_*coding:utf-8 *_* 
__Author__ = 'xiaohan'
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class KxScreenshotDelegate:
    def finishedWithData(self, data):
        pass


class KxScreenshotStatus:
    init = 0
    dragging = 1
    ok = 2
    drafting = 3


class KxScreenshotWidget(QWidget):
    def __init__(self, img, delegate):
        super(KxScreenshotWidget, self).__init__()
        self.startX = 0
        self.staryY = 0
        self.endX = 0
        self.endY = 0
        self.draftPointss = []
        self.img = img
        self.delegate = delegate
        self.status = KxScreenshotStatus.init
        self.setCursor(QtCore.Qt.CrossCursor)
        self.initUI()

    def initUI(self):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowTitle("screenshot")
        # self.setGeometry(0,0,screen.width(),screen.height())
        # self.setWindowOpacity(0.3)
        palette1 = QtGui.QPalette()
        palette1.setBrush(self.backgroundRole(), QtGui.QBrush(self.img))
        self.setPalette(palette1)
        tipLabel = QLabel("截图模式，按ESC退出,按右键取消选框,按回车发送截图")
        tipLabel.setObjectName("tip")
        tipLabel.setStyleSheet(
            "QLabel#tip{background-color:white;padding:5px;color:black;font-weight:bold;font-size:16px;}")
        vBox = QVBoxLayout()
        tipBar = QHBoxLayout()
        tipBar.addStretch(1)
        tipBar.addWidget(tipLabel)
        tipBar.addStretch(1)
        vBox.addLayout(tipBar)
        vBox.addStretch(1)
        self.setLayout(vBox)
        mask = QWidget(self)
        black = QColor(0, 0, 0)
        black.setAlphaF(0.2)
        palette2 = QtGui.QPalette()
        palette2.setBrush(mask.backgroundRole(), black)
        mask.setPalette(palette2)
        mask.setAutoFillBackground(True)
        mask.setGeometry(0, 0, self.img.width(), self.img.height())

    def paintEvent(self, e):
        if self.status == KxScreenshotStatus.dragging or self.status == KxScreenshotStatus.ok or self.status == KxScreenshotStatus.drafting:
            qp = QPainter()
            qp.begin(self)
            self.drawCutRect(qp)
            if self.status == KxScreenshotStatus.ok or self.status == KxScreenshotStatus.drafting:
                self.drawDraft(qp)
            qp.end()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        elif event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            if self.status == KxScreenshotStatus.ok:
                ba = QByteArray()
                buf = QBuffer(ba)
                buf.open(QIODevice.WriteOnly)
                cuttedImg = self.img.copy(QRect(QPoint(self.startX, self.startY), QPoint(self.endX, self.endY)))
                painter = QPainter(cuttedImg)
                painter.begin(self)
                pen = QPen(Qt.red, 2, Qt.SolidLine)
                painter.setPen(pen)
                for points in self.draftPointss:
                    for i in range(len(points) - 1):
                        p0 = points[i]
                        p1 = points[i + 1]
                        painter.drawLine(p0.x() - self.startX, p0.y() - self.startY, p1.x() - self.startX,
                                         p1.y() - self.startY)
                painter.end()
                cuttedImg.save(buf, format="PNG")
                self.delegate.finishedWithData(ba.data())
                buf.close()
                self.close()

    def mouseMoveEvent(self, e):
        if self.status == KxScreenshotStatus.dragging:
            self.endX = e.x()
            self.endY = e.y()
            self.update()
        elif self.status == KxScreenshotStatus.drafting:
            if e.x() < self.startX or e.x() > self.endX or e.y() < self.startY or e.y() > self.endY:
                if len(self.draftPointss[-1]) > 0:
                    self.draftPointss.append([])
            else:
                self.draftPointss[-1].append(QPoint(e.x(), e.y()))
            self.update()

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            if self.status == KxScreenshotStatus.init:
                self.startX = e.x()
                self.startY = e.y()
                self.status = KxScreenshotStatus.dragging
            elif self.status == KxScreenshotStatus.ok:
                self.status = KxScreenshotStatus.drafting
                self.draftPointss.append([])
        elif e.button() == Qt.RightButton:
            if self.status == KxScreenshotStatus.dragging:
                self.status = KxScreenshotStatus.init
                self.setCursor(QtCore.Qt.CrossCursor)
            elif self.status == KxScreenshotStatus.ok:
                if len(self.draftPointss) > 0:
                    self.draftPointss = []
                else:
                    self.status = KxScreenshotStatus.init
                    self.setCursor(QtCore.Qt.CrossCursor)
            elif self.status == KxScreenshotStatus.drafting:
                self.draftPointss = []
                self.status = KxScreenshotStatus.ok
        self.update()

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            if self.status == KxScreenshotStatus.dragging:
                self.status = KxScreenshotStatus.ok
                self.setCursor(QtCore.Qt.UpArrowCursor)
                x0 = self.startX
                x1 = self.endX
                if self.startX > self.endX:
                    x0 = self.endX
                    x1 = self.startX
                y0 = self.startY
                y1 = self.endY
                if self.startY > self.endY:
                    y0 = self.endY
                    y1 = self.startY
                self.startX = x0
                self.startY = y0
                self.endX = x1
                self.endY = y1
            elif self.status == KxScreenshotStatus.drafting:
                self.status = KxScreenshotStatus.ok
        self.update()

    def drawCutRect(self, qp):
        pen = QPen(Qt.blue, 2, Qt.DashLine)
        qp.setPen(pen)
        r = QRect(QPoint(self.startX, self.startY), QPoint(self.endX, self.endY))
        qp.drawRect(r)

    def drawDraft(self, qp):
        pen = QPen(Qt.red, 2, Qt.SolidLine)
        qp.setPen(pen)
        for points in self.draftPointss:
            for i in range(len(points) - 1):
                p0 = points[i]
                p1 = points[i + 1]
                qp.drawLine(p0.x(),p0.y(),p1.x(),p1.y())


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# class KxChatWidget(QWidget, KxScreenshotDelegate):
#       ...  # 略去其余代码只保留调用截屏相关
#
#     def toScreenshot(self):
#         if self.session is None:
#             return
#     def finishedWithData(self, data):
#     #    此处的data即为截屏后的结果，是个二进制数组，可直接展示
class Mywidget(QWidget,KxScreenshotDelegate):
    def __init__(self):
        super(Mywidget, self).__init__()

        desktop = QDesktopWidget()
        r = desktop.screenGeometry(desktop.screenNumber(self))
        screenshot = KxScreenshotWidget(
            QGuiApplication.primaryScreen().grabWindow(0, r.x(), r.y(), r.width(), r.height()),self)
        screenshot.setGeometry(desktop.screenGeometry(desktop.screenNumber(self)))
        screenshot.show()

if __name__ == '__main__':
    import sys
    app = KxScreenshotWidget(sys.argv)
    tree = Mywidget()
    tree.show()
    sys.exit(app.exec_())

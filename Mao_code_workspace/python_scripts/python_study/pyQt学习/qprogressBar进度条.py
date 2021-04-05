from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor,QPixmap
from PyQt5.QtCore import Qt,QBasicTimer

import sys
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.pbar=QProgressBar(self)
        self.pbar.setGeometry(30,40,200,25)

        self.btn=QPushButton('Start',self)
        self.btn.move(40,80)
        self.btn.clicked.connect(self.doAction)

        # 计时器
        self.timer=QBasicTimer()
        self.step=0



        self.setGeometry(300,300,380,370)
        self.setWindowTitle('toggle button')
        self.show()
    # 重写timerevent、，超出100时，设置为finished
    def timerEvent(self,e):
        if self.step>=100:
            self.timer.stop()#停止计时
            self.btn.setText('Finished')#显示结束
            return
        self.step+=1
        self.pbar.setValue(self.step)
    #开始和停止状态的转换
    def doAction(self):
        # 工作状态，点击时，停止，并将按钮设置为start
        if self.timer.isActive():#计时器开始运行
            self.timer.stop()#停止计时
            self.btn.setText('Start')
        # 停止状态，点击时，开始，并将按钮设置为stop
        else:#计时器停止了
            #开始计时事件,我们调用start()方法.这个方法有两个参数:超时和接收事件的对象.
            self.timer.start(100,self)
            self.btn.setText('Stop')



    def setColor(self,pressed):
        source=self.sender()
        if pressed:
            print(source.text())
            val=255
        else:val=0
        if source.text()=='red':
            self.col.setRed(val)
        elif source.text()=='green':
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)

        self.square.setStyleSheet("QFrame{ background-color:%s}"%self.col.name())
    def changeValue(self,value):
        if value==0:
            self.label.setPixmap(QPixmap('01.bmp'))
        elif value>0 and value <=30:
            self.label.setPixmap(QPixmap('02.bmp'))
        elif value>30 and value <=80:
            self.label.setPixmap(QPixmap('03.bmp'))
        else:
            self.label.setPixmap(QPixmap('04.bmp'))

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())

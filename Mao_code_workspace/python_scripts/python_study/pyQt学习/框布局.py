import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 两个按钮
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")
        # 水平
        hbox = QHBoxLayout()  # 水平框布局
        hbox.addStretch(1)  # 伸缩因子
        hbox.addWidget(okButton)  # 绑定按钮1
        hbox.addWidget(cancelButton)  # 绑定按钮2

        # 垂直
        vbox = QVBoxLayout()
        vbox.addStretch(1)  # 伸缩因子
        vbox.addLayout(hbox)  # 将水平框加入到垂直布局中

        # 设置窗口的主体布局
        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

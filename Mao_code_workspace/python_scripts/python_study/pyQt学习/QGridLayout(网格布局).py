import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication,QGridLayout)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        # 我们创建了网格按钮.要填补一个空位,我们就添加一个QLabel部件
        grid=QGridLayout()
        self.setLayout(grid)
        names=['Cls','Bck','','Close',
            '7','8','9','/',
            '4','5','6','*',
            '1','2','3','-',
            '0','.','=','+',
            ]
        positions=[(i,j) for i in range(5) for j in range(4)]
        print(positions)
        for position,name in zip(positions,names):
            if name=='':
                continue
            button=QPushButton(name)
            grid.addWidget(button,*position)

        self.move(300,150)
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

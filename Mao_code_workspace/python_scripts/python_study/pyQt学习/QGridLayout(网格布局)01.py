import sys
from PyQt5.QtWidgets import (QWidget,QLabel,QLineEdit,QTextEdit, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication,QGridLayout)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        #label标签
        title=QLabel('Title')
        author=QLabel('Author')
        review=QLabel('Review')
        #文本框标签
        titleEdit=QLineEdit()
        authorEdit=QLineEdit()
        reviewEdit=QTextEdit()

        grid=QGridLayout()
        grid.setSpacing(10)#间隔

        grid.addWidget(title,1,0)
        grid.addWidget(titleEdit,1,1)

        grid.addWidget(author,2,0)
        grid.addWidget(authorEdit,2,1)
        grid.addWidget(review,3,0)
        grid.addWidget(reviewEdit,3,1,5,4)#分成5行1列

        self.setLayout(grid)

        self.move(300,150)
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

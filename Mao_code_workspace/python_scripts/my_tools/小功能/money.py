import  sys
import urllib2
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
'''汇率转换'''
class Form(QDialog):
    def __init__(self):
        super(Form, self).__init__()
        self.initUI()
        self.show()
    def initUI(self):
        date=self.getdata()
        rates=sorted(self.rates.keys())
        dateLabel=QLabel()
        self.fromComboBox=QComboBox()
        self.fromComboBox.addItems(rates)
        self.fromSpinBox=QDoubleSpinBox()#微调框
        self.fromSpinBox.setRange(0.01,1000000.00)#最大最小
        self.fromSpinBox.setValue(1.00)#初值
        self.toComboBox=QComboBox()
        self.toComboBox.addItems(rates)
        self.tolabel=QLabel("1.00")

        grid=QGridLayout(self)
        grid.addWidget(dateLabel,0,0)
        grid.addWidget(self.fromComboBox,1,0)
        grid.addWidget(self.fromSpinBox,1,1)
        grid.addWidget(self.toComboBox,2,0)
        grid.addWidget(self.tolabel,2,1)

        self.fromComboBox.currentIndexChanged[int].connect(self.updateUI)
        self.fromSpinBox.valueChanged.connect(self.updateUI)
        self.toComboBox.currentIndexChanged[int].connect(self.updateUI)

    def getdata(self):
        self.rates={}
        try:
            date="Unkown"
            fh=urllib2.urlopen("http://www/bankofcanada.ca/en/markets/csv/exchange_eng.csv")
            for line in fh:
                if not line or line.startswith('#','closing'):
                    continue
                fields=line.split(',')
                if line.startswith('Date'):
                    date=fields[-1]
                else:
                    try:
                        value=float(fields[-1])
                        self.rates[str(fields[0])]=value
                    except ValueError:
                        pass
            return "Exchange Rates Date: "+date
        except Exception as e:
            return "failed download :%s"%e
    def updateUI(self):
        to=str(self.toComboBox.currentText())
        from1=str(self.fromComboBox.currentText())
        amount=(self.rates[from1]/self.rates[to])*self.fromSpinBox.value()
        self.tolabel.setText("%0.2f"%amount)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=Form()
    sys.exit(app.exec_())


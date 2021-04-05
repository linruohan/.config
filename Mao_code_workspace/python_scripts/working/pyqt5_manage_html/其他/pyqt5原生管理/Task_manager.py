# *_*coding:utf-8 *_*
__Author__ = 'xiaohan'

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLabel, QPushButton, QTabWidget, QWidget

from UI.UI_base import UI_base
from UI_today import UiToday


class TaskManger(UI_base):
    def __init__(self):
        super(TaskManger, self).__init__()
        self.setWindowTitle('Task Manager')
        self.setGeometry(300, 100, 800, 500)
        self.tabs = QTabWidget()
        self.tabs.setMinimumHeight(1000)
        self.tabs.setTabPosition(QTabWidget.North)
        self.main_layout.addWidget(self.tabs, 1, 0, 10, 10)
        self.tab_today = QWidget()
        self.tab_history = QWidget()
        self.tab_all = QWidget()
        self.tab_me = QWidget()
        self.tabs.addTab(self.tab_today, '今日任务')
        self.tabs.addTab(self.tab_history, '历史任务')
        self.tabs.addTab(self.tab_all, '所有任务')
        self.tabs.addTab(self.tab_me, '关于我')
        with open('qss/Task_manager.qss','r')as f:
            self.tabs.setStyleSheet(f.read())
        self.init_ui()

    def init_ui(self):
        self.tab_today_ui()
        self.tab_history_ui()
        self.tab_all_ui()
        self.tab_me_ui()

    def tab_today_ui(self):
        self.ui = UiToday()
        self.tabs.setTabText(2, "教育程度")
        self.tab_today.setLayout(self.ui.layout)

    def tab_history_ui(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel("科目"))
        layout.addWidget(QPushButton("1231"))
        self.tabs.setTabText(2, "教育程度")
        self.tab_history.setLayout(layout)

    def tab_all_ui(self):
        pass

    def tab_me_ui(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = TaskManger()
    ui.show()
    sys.exit(app.exec_())

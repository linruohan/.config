import os
import sys

import qtawesome
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QApplication, QButtonGroup, QGridLayout, QLabel, QLineEdit, QPushButton, QRadioButton, \
    QTextBrowser, \
    QWidget

from common_html import render_html_str
from common_tasks import BASE_TASK_HTML_DIR, Tasks
from my_web import MyWeb


class UiToday(QWidget):
    data = {
        "headrs": [
            "ID",
            "任务名",
            '剩余时间',
            "完成百分比",
            "进展",
            '状态',
            'html',
            "开始时间",
            "结束时间",
            "执行Owner",
            "创建者",
            "任务团队"
        ],
        "tasks": [],
    }

    def __init__(self):
        super(UiToday, self).__init__()
        self.setWindowTitle('Today')
        self.setGeometry(500, 200, 800, 600)
        self.layout = QGridLayout()

        self.layout.setSpacing(20)
        # self.layout.setColumnStretch(2,1)
        self.layout.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        # self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        self.tasks = Tasks()

        self.team = "mine"
        self.init_ui()

    def init_ui(self):
        self.search_ui()
        self.opration_ui()
        self.tasks_init()

    def search_ui(self):
        # 分类选择器
        self.buttonGroup = QButtonGroup()
        self.all_bg = QRadioButton('所有的')
        self.mine_bg = QRadioButton('我的')
        self.team_bg = QRadioButton('团队的')
        self.buttonGroup.addButton(self.all_bg)
        self.buttonGroup.addButton(self.mine_bg)
        self.buttonGroup.addButton(self.team_bg)
        self.all_bg.clicked.connect(self.get_team)
        self.mine_bg.clicked.connect(self.get_team)
        self.team_bg.clicked.connect(self.get_team)
        self.mine_bg.setChecked(True)

        self.layout.addWidget(self.all_bg, 0, 0, 1, 1)
        self.layout.addWidget(self.mine_bg, 0, 1, 1, 1)
        self.layout.addWidget(self.team_bg, 0, 2, 1, 1)
        # 搜索功能
        self.search_input = QLineEdit()
        self.search_input.setMaximumWidth(200)
        self.search_input.setPlaceholderText('按Enter键搜索')
        self.search_label = QLabel()
        self.search_label.setPixmap(
            (qtawesome.icon('fa.search', color='red').pixmap(QSize(25, 25))))
        self.layout.addWidget(self.search_label, 0, 3, 1, 1, Qt.AlignRight)
        self.layout.addWidget(self.search_input, 0, 4, 1, 1)

        self.search_input.returnPressed.connect(self.search_click)

    def get_team(self):
        team_dict = {
            "所有的": "all",
            "我的": "mine",
            "团队的": "team"
        }
        self.team = team_dict[self.sender().text()]

    def search_click(self):
        search_key = self.sender().text()
        print(search_key, self.team)
        key_tasks = self.tasks.get_tasks_by_key(search_key)
        team_tasks = self.tasks.get_tasks_by_team(self.team)
        self.data['tasks'] = [i for i in key_tasks if i in team_tasks]
        html = render_html_str('tasks_show.html', self.data)
        self.tasks_broser.setHtml(html)

    def opration_ui(self):
        self.task_id = QLineEdit()
        self.task_id.setMaximumWidth(300)
        self.task_id.setPlaceholderText('输入ID')
        self.task_id.setValidator(QIntValidator(0, 1000))
        self.add_btn = QPushButton(
            qtawesome.icon('fa.plus', color='black'), '')
        self.add_btn.clicked.connect(self.add_task)
        self.del_btn = QPushButton(qtawesome.icon('fa.minus', color='red'), '')
        self.del_btn.clicked.connect(self.del_task)
        self.modify_btn = QPushButton(
            qtawesome.icon('fa.pencil', color='orange'), '')
        self.modify_btn.clicked.connect(self.modify_task)
        self.look_btn = QPushButton(
            qtawesome.icon('fa.eye', color='green'), '')
        self.look_btn.clicked.connect(self.look_task)

        self.tasks_broser = QTextBrowser()
        self.tasks_broser.setMinimumHeight(1000)
        self.layout.addWidget(self.tasks_broser, 2, 0, 10, 10)

        self.layout.addWidget(self.task_id, 1, 0, 1, 1)
        self.layout.addWidget(self.add_btn, 1, 1, 1, 1)
        self.layout.addWidget(self.del_btn, 1, 2, 1, 1)
        self.layout.addWidget(self.modify_btn, 1, 3, 1, 1)
        self.layout.addWidget(self.look_btn, 1, 4, 1, 1)

    def add_task(self):
        pass

    def del_task(self):
        if self.task_id.text():
            task_id = int(self.task_id.text())
            self.tasks.del_task(task_id)

    def modify_task(self):
        pass

    def look_task(self):
        if self.task_id.text():
            task = self.tasks.get_task_by_id(int(self.task_id.text()))
            html_name = task['html']
            html_editor = MyWeb(os.path.join(BASE_TASK_HTML_DIR, html_name))
            html_editor.show()
            html_editor.webview.showMaximized()

    def tasks_init(self):
        self.data['tasks'] = self.tasks.all_tasks
        html = render_html_str('tasks/tasks_show.html', self.data)
        self.tasks_broser.setHtml(html)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = UiToday()
    ui.show()
    sys.exit(app.exec_())

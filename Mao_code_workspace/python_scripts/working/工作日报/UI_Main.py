# *_*coding:utf-8 *_* 

import json
import os
import sys

from PyQt5 import sip
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QApplication, QFormLayout, QLabel, QLineEdit, QListWidget, QListWidgetItem, QMenu, \
    QProgressBar, QPushButton, QTextEdit, QVBoxLayout, QWidget, qApp

from UI_base import UiBase
from UI_mywidget import CompletionQLineEdit
from conf import products, versions, work_category


class UiMain(UiBase):
    def __init__(self):
        super(UiMain, self).__init__()
        self.setFixedSize(960, 700)
        self.left_widget = QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QVBoxLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格
        self.content = None
        self.right_widget = QWidget()  # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QVBoxLayout()
        self.right_layout.setSpacing(10)
        self.right_layout.setContentsMargins(0, 0, 0, 0)
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格

        self.main_layout.addWidget(self.left_widget, 0, 0, 9, 2)
        self.main_layout.addWidget(self.right_widget, 1, 2, 9, 10)
        self.init_ui()

    def init_ui(self):
        category_list = QListWidget()
        for category in work_category.values():
            item = QListWidgetItem()
            category_list.addItem(item)
            btn = QPushButton(str(category))
            func_str = "get_" + list(work_category.keys())[list(work_category.values()).index(category)]
            func = getattr(self, func_str)
            btn.clicked.connect(func)
            category_list.setItemWidget(item, btn)
        self.left_layout.addWidget(category_list)

    def contextMenuEvent(self, event):
        """右键关闭"""
        menu = QMenu(self)
        quit_action = menu.addAction("Quit")
        action = menu.exec_(self.mapToGlobal(event.pos()))
        if action == quit_action:
            qApp.quit()

    def get_all(self):
        pass

    def get_fail_analysis(self):
        if self.content:
            self.right_layout.removeWidget(self.content)
            sip.delete(self.content)
        self.content = QWidget()
        layout = QFormLayout()
        self.content.setLayout(layout)
        version = CompletionQLineEdit(versions)
        version.setPlaceholderText('请输入版本')
        product = CompletionQLineEdit(products)
        product.setPlaceholderText('请输入产品')
        finish = QLineEdit()
        finish.setPlaceholderText('已分析用例数:(条)')
        finish.setValidator(QIntValidator())
        no_finish = QLineEdit()
        no_finish.setValidator(QIntValidator())
        no_finish.setPlaceholderText('剩余失败用例数:(条)')
        percent = QProgressBar()
        other_text = QTextEdit()

        def value_change():
            finish_num = int(finish.text()) if finish.text().strip() else 0
            no_finish_num = int(no_finish.text()) if no_finish.text().strip() else 0
            percent.setValue(finish_num / (finish_num + no_finish_num) * 100)

        finish.textChanged.connect(value_change)
        no_finish.textChanged.connect(value_change)
        layout.addRow(QLabel('版本: '), version)
        layout.addRow(QLabel('产品: '), product)
        layout.addRow(QLabel('已分析: '), finish)
        layout.addRow(QLabel('剩余: '), no_finish)
        layout.addRow(QLabel('进度: '), percent)
        layout.addRow(QLabel('描述和备注: '), other_text)
        save = QPushButton('保存')
        layout.addRow(save)

        def save_click():
            path = 'data/tmp'
            result = {
                'version': version.text(),
                'product': product.text(),
                'finish': finish.text(),
                'no_finish': no_finish.text(),
                'percent': percent.value(),
                'other_text': other_text.toPlainText(),
            }
            if not os.path.exists(path):
                os.makedirs(path)
            with open(path + './fail_analysis.json', 'a+') as f:
                f.write(json.dumps(result))

        save.clicked.connect(save_click)
        self.right_layout.addWidget(self.content)
        # self.right_layout.addWidget(version)
        # self.right_layout.addWidget(product)
        # self.right_layout.addWidget(finish)
        # self.right_layout.addWidget(no_finish)
        # self.right_layout.addWidget(percent)
        # self.right_layout.addStretch(1)

    def get_requirements(self):
        pass

    def get_special_test(self):
        pass

    def get_board_owner(self):
        pass

    def get_DTS_pages(self):
        pass

    def get_others(self):
        pass

    def get_risks_problems(self):
        pass

    def get_improvements_suggestions(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    QApplication.processEvents()
    gui = UiMain()
    gui.show()
    sys.exit(app.exec_())

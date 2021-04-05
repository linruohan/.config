#- * - encoding: utf - 8 -*-
import json

import context
import requests
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton, QTextEdit, QWidget


class MainContent(QWidget):

    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setupUi()
        self.connect()

    def setupUi(self):
        self.grid_layout = QtWidgets.QGridLayout(self)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.grid_layout.setSpacing(0)

        self.text_edit = QTextEdit(self)
        self.info_btn = QPushButton("get tenant info", self)
        self.meta_btn = QPushButton("get metas", self)
        self.grid_layout.addWidget(self.info_btn, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.meta_btn, 1, 2, 1, 1)
        self.grid_layout.addWidget(self.text_edit, 2, 1, 1, 2)

    def connect(self):
        self.meta_btn.clicked.connect(self.get_metas)
        self.info_btn.clicked.connect(self.get_info)

    def http_get(self, url):
        return requests.get(url, headers={'x-token': context.cookies.get('_accessToken')}).json()

    def get_metas(self):
        res = self.http_get("https://crm.chengfayun.com/api/v1.0/one/all-metas")
        self.text_edit.setText(json.dumps(res, ensure_ascii=False, indent=4))

    def get_info(self):
        url = f"https://crm.chengfayun.com/api/v1.0/tenant-gateway/tenant/org/{context.cookies.get('_tenant_id')}"
        res = self.http_get(url)
        self.text_edit.setText(json.dumps(res, ensure_ascii=False, indent=4))

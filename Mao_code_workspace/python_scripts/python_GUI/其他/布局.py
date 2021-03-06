# *_*coding:utf-8 *_* 
__Author__ = 'xiaohan'
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout


# 垂直居中
def vcenter_layout(*widgets):
    vbox = QVBoxLayout()
    vbox.addStretch()
    for widget in widgets:
        vbox.addWidget(widget)
    vbox.addStretch()
    return vbox


# 水平居中
def hcenter_layout(*widgets):
    hbox = QHBoxLayout()
    hbox.addStretch()
    for widget in widgets:
        hbox.addWidget(widget)
    hbox.addStretch()
    return hbox


# 垂直水平居中
def center_layout(widget):
    hbox = QHBoxLayout()
    hbox.addStretch()
    hbox.addWidget(widget)
    hbox.addStretch()

    vbox = QVBoxLayout()
    vbox.addStretch()
    vbox.addLayout(hbox)
    vbox.addStretch()
    return vbox


# 居左
def left_layout(*widgets):
    hbox = QHBoxLayout()
    for widget in widgets:
        hbox.addWidget(widget)
    hbox.addStretch()
    return hbox


# 居右
def right_layout(*widgets):
    hbox = QHBoxLayout()
    hbox.addStretch()
    for widget in widgets:
        hbox.addWidget(widget)
    return hbox


# 向上靠齐
def top_layout(*widgets):
    vbox = QVBoxLayout()
    for widget in widgets:
        vbox.addWidget(widget)
    vbox.addStretch()
    return vbox


# 向下靠齐
def bottom_layout(*widgets):
    vbox = QVBoxLayout()
    vbox.addStretch()
    for widget in widgets:
        vbox.addWidget(widget)
    return vbox


# 正常垂直分布
def v_layout(*widgets):
    vbox = QVBoxLayout()
    for widget in widgets:
        vbox.addWidget(widget)
    return vbox


# 正常垂直分布
def h_layout(*widgets):
    vbox = QHBoxLayout()
    for widget in widgets:
        vbox.addWidget(widget)
    return vbox
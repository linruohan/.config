import sys
import os
sys.path.append(os.path.dirname(__file__))
from UI_main import UI_main
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox


class Main(UI_main):
    def __init__(self):
        super(Main, self).__init__()

    """ 文件 """

    def open_md(self):
        if self.ask_save():
            return
        self.frame_work.ipt.setPlainText('')
        path = QFileDialog.getOpenFileName(self, '选择文件', '', '*.md')
        if path[0]:
            with open(path[0], 'r', encoding='utf-8') as f:
                self.frame_work.ipt.setPlainText(f.read())
                self.opened_file = path[0]

    def new_md(self):
        if self.ask_save():
            return
        self.frame_work.ipt.setPlainText('新建成功,请输入md文档吧')
        self.opened_file = 'new_file'

    def save_md(self):
        if self.opened_file == 'new_file':
            f = QFileDialog.getSaveFileName(self, '新建MD文件', '', '*.md')
            if f[0]:
                path = f[0]
            else:
                return False
        elif self.opened_file:
            path = self.opened_file
        else:
            return False
        with open(path, 'w', encoding='utf-8') as f:
            f.write(self.frame_work.ipt.toPlainText())
            QMessageBox.information(self, '成功', '保存完成!', QMessageBox.Ok)
            return True

    def ask_save(self):
        if self.opened_file:
            r = QMessageBox.warning(self, "提醒", "是否保存当前文件?", QMessageBox.Ok | QMessageBox.No | QMessageBox.Cancel,
                                    QMessageBox.Cancel)
            if r == QMessageBox.Ok:
                if not self.save_md():
                    return True
            elif r == QMessageBox.Cancel:
                return True

    """ 设置 """

    def choose_theme(self):
        self.conf["choose_theme"] = self.sender().property("color")
        for c in self.color_actions:
            if c is not self.sender():
                c.setChecked(False)
        self.set_stylesheet()
        self.save_conf()

    def change_font(self):
        if self.sender().text() == '字体增':
            self.conf['font-size'] += 1
        else:
            self.conf['font-size'] -= 1
        self.set_stylesheet()
        self.save_conf()


if __name__ == '__main__':
    from sys import argv

    app = QApplication(argv)
    main = Main()
    main.show()
    app.exec_()

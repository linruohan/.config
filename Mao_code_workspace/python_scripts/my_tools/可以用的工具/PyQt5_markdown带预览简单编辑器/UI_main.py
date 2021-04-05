import os
from json import load, dump
from re import sub
from webbrowser import open_new_tab

from PyQt5.Qt import QAction, QFont, QFontDatabase, QIcon, QKeySequence, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QGridLayout, QMenu, QWidget

from utils import Head, Work, color_pix


class UI_main(QMainWindow):
    color_actions = []
    opened_file = 'default'
    css, conf = None, None
    color_dict = {
        'white': "白色",
        'dark': "黑色",
        'wheat': "小麦",
        'Fuchsia': "灯笼海棠(紫红色)",
        "Purple": "紫色",
        "DoderBlue": "道奇蓝",
        "DeepSkyBlue": "深天蓝",
        "Turquoise": "绿宝石",
        "NavajoWhite": "纳瓦霍白",
        "MistyRose": "薄雾玫瑰",
        "DimGray": "暗淡的灰色",
        "DarkCyan": "深青色"
    }
    def save_conf(self):
        with open('./conf.json', 'w', encoding='utf-8') as f:
            dump(self.conf, f, indent=4)    
    def __init__(self):
        super(UI_main, self).__init__()
        self.setWindowTitle("Markdown html Editor")
        self.setting_window_style()
        self.frame_head = Head(self)
        self.frame_work = Work(self)
        self.init_ui()

    def setting_window_style(self):
        """设置: 窗口/主题/字体/样式"""
        with open("conf.json", encoding="UTF-8") as f:
            self.conf = load(f)
        # 设置窗口居中显示
        desktop = QApplication.desktop().screenGeometry()
        size = self.conf['size']
        self.setGeometry(int(desktop.width() / 2 - size[0] / 2), int(desktop.height() / 2 - size[1] / 2), size[0],
                         size[1])
        # 设置样式和主题
        self.set_stylesheet()
        # css样式设置----暂时无用
        # with open("style.css", encoding="UTF-8") as f:
        #     self.css = f.read()
        # 设置字体  已加载,未设置
        self.ico_font = QFont(
            QFontDatabase.applicationFontFamilies(
                QFontDatabase.addApplicationFont(os.path.join(os.path.dirname(__file__), "iconfont.ttf")))[0], 30)

    def set_stylesheet(self):
        with open("style.qss", encoding="UTF-8") as f:
            s = sub(r'([\d.]*)rem', lambda m: str(int(float(m.group(1)) * self.conf['font-size'])) + 'px', f.read())
            s = sub('theme', self.conf['theme'][self.conf['choose_theme']], s)
            self.setStyleSheet(s)

    def init_ui(self):
        self.frame_head.initUI()
        self.init_menu()
        center_widget = QWidget(self)
        layout = QGridLayout(self)
        layout.setContentsMargins(0, 3, 0, 0)
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)
        layout.addWidget(self.frame_head, 0, 0)
        layout.addWidget(self.frame_work, 1, 0)
        center_widget.setLayout(layout)
        self.setCentralWidget(center_widget)

    def init_menu(self):
        menu = self.menuBar()
        file_menu = menu.addMenu('文件')
        set_menu = menu.addMenu('设置')
        about_action = menu.addAction('关于')
        about_action.triggered.connect(
            lambda: open_new_tab('https://github.com/yunyuyuan/PyQt5/tree/master/md-to-html'))
        for menu in [file_menu, set_menu]:
            menu.setCursor(Qt.PointingHandCursor)
        open_action = QAction('打开', self)
        open_action.setIcon(QIcon('imgs/file.png'))
        open_action.triggered.connect(self.open_md)
        new_action = QAction('新建', self)
        new_action.setIcon(QIcon('imgs/new.png'))
        new_action.triggered.connect(self.new_md)
        save_action = QAction('保存', self)
        save_action.setIcon(QIcon('imgs/save.png'))
        save_action.triggered.connect(self.save_md)
        file_menu.addActions([open_action, new_action, save_action])

        choose_color = QMenu('主题', self)
        choose_color.setObjectName('choose_color')
        choose_color.setIcon(QIcon('imgs/theme.png'))

        for color in self.color_dict.keys():
            theme = QAction(self.color_dict[color], self)
            theme.setProperty('color', color)
            theme.triggered.connect(self.choose_theme)
            theme.setCheckable(True)
            color = self.conf['theme'][theme.property('color')]
            icon = QIcon()
            icon.addPixmap(color_pix(color))
            theme.setIcon(icon)
            choose_color.addAction(theme)
            self.color_actions.append(theme)
            if self.conf['choose_theme'] == theme.property('color'):
                theme.setChecked(True)
        set_menu.addMenu(choose_color)
        font_big = QAction("字体增", self)
        font_big.setIcon(QIcon('imgs/big.png'))
        font_big.setShortcut(QKeySequence.ZoomIn)
        font_sma = QAction("字体减", self)
        font_sma.setIcon(QIcon('imgs/reduce.png'))
        font_sma.setShortcut(QKeySequence.ZoomOut)
        for f in [font_big, font_sma]:
            f.triggered.connect(self.change_font)
            set_menu.addAction(f)


if __name__ == '__main__':
    from sys import argv

    app = QApplication(argv)
    main = UI_main()
    main.show()
    app.exec_()

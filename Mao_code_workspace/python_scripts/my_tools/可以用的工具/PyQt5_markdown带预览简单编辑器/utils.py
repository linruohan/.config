from re import sub

from PIL.Image import new as new_im
from PIL.ImageDraw import ImageDraw
from PIL.ImageQt import toqpixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QGridLayout, QHBoxLayout, QLabel, QPushButton, QTextEdit
from markdown import markdown

from extension_makrdown import all_ext


def color_pix(color):
    im = new_im('RGB', (128, 128))
    draw = ImageDraw(im, 'RGB')
    draw.rectangle((0, 0, 128, 128), fill=(int(color[1:3], 16), int(color[3:5], 16), int(color[5:], 16)))
    return toqpixmap(im)


class ResizeLabel(QLabel):
    def __init__(self, f, left_e, right_e):
        super(ResizeLabel, self).__init__(f)
        self.f = f
        self.left, self.right = left_e, right_e
        self.setFixedWidth(5)
        self.setCursor(Qt.SizeHorCursor)
        self.attach = False
        self.start_x = 0

    def mousePressEvent(self, e):
        self.attach = True
        self.start_x = e.globalX()

    def mouseReleaseEvent(self, e):
        self.attach = False

    def mouseMoveEvent(self, e):
        if self.attach:
            delta = e.globalX() - self.start_x
            if (self.f.all_text[self.left].width() + delta) > 50 and (self.f.all_text[self.right].width() - delta) > 50:
                self.f.layout().setColumnStretch(self.left, self.f.all_text[self.left].width() + delta)
                self.f.layout().setColumnStretch(self.right, self.f.all_text[self.right].width() - delta)
            self.start_x = e.globalX()


class WorkEdit(QTextEdit):
    def __init__(self, work):
        super().__init__(work)
        self.work = work
        self.top = work.top
        self.setMinimumWidth(50)


class MdEdit(WorkEdit):
    def __init__(self, work):
        super(MdEdit, self).__init__(work)
        self.setPlainText('input something')
        self.ext_list = ['attr_list', 'tables', 'fenced_code', 'sane_lists', 'toc']
        self.ext_list.extend(all_ext)
        self.textChanged.connect(self.do_parse)

    def do_parse(self):
        content = self.toPlainText()
        content = markdown(content, extensions=self.ext_list)
        old_value = self.work.html.verticalScrollBar().value()
        self.work.html.setPlainText(content)
        self.work.html.verticalScrollBar().setValue(old_value)

    def setVisible(self, b):
        if not b:
            self.work.layout().setColumnStretch(0, 0)
        super().setVisible(b)


class HtmlEdit(WorkEdit):
    def __init__(self, work, rel_label):
        super(HtmlEdit, self).__init__(work)
        self.rel_label = rel_label
        self.textChanged.connect(self.do_parse)

    def setVisible(self, b):
        if not b:
            self.work.layout().setColumnStretch(2, 0)
        super().setVisible(b)
        self.rel_label.setVisible(b)

    def do_parse(self):
        old_value = self.work.md.verticalScrollBar().value()
        self.work.md.setText("<style>%s</style>" % self.top.css + sub(r'([\d.]*)rem', lambda m: str(
            int(float(m.group(1)) * self.top.conf['font-size'])) + 'px', self.toPlainText()))
        self.work.md.verticalScrollBar().setValue(old_value)


class MdShow(WorkEdit):
    def __init__(self, work, rel_label):
        super().__init__(work)
        self.setReadOnly(True)
        self.rel_label = rel_label
        self.setStyleSheet("QTextEdit{background: transparent}")

    def setVisible(self, b):
        if not b:
            self.work.layout().setColumnStretch(4, 0)
        super().setVisible(b)
        self.rel_label.setVisible(b)


class Head(QFrame):
    def __init__(self, top):
        super(Head, self).__init__(top)
        self.top = top
        self.setObjectName("head")

        self.md_list = []
        self.btn_list = [[0xe8f5, "h"],
                         [0xe60b, "b"],
                         [0xe60c, "i"],
                         [0xe929, "del_"],
                         [0xe790, "link"],
                         [0xebc5, "img"],
                         [0xe858, "code"],
                         [0xe600, "ul"],
                         [0xe60d, "ol"],
                         [0xe683, "table"]]
        self.work_ipt = None


    def initUI(self):
        layout = QHBoxLayout(self)
        layout.setAlignment(Qt.AlignLeft)
        for i in self.btn_list:
            btn = QPushButton(chr(i[0]), self)
            info = self.top.conf["md"][i[1]]
            btn.setToolTip(info["tip"])
            btn.content = info["content"]
            btn.type = info["type"]
            btn.setProperty("what", i[1])
            btn.setProperty("class", "md-btn")
            btn.setCursor(Qt.PointingHandCursor)

            self.md_list.append(btn)
            layout.addWidget(btn)
        layout.addStretch(100)
        frm = QFrame(self)
        frm.setObjectName('switch')
        f_layout = QGridLayout(self)
        f_layout.setSpacing(0)
        f_layout.setContentsMargins(0, 0, 0, 0)
        idx = 0
        for b in ['md', 'html', '预览']:
            btn = QPushButton(b, frm)
            f_layout.addWidget(btn, 0, idx)
            idx += 1
            btn.setCursor(Qt.PointingHandCursor)
            btn.clicked.connect(self.switch_frame)
            if b == '预览':
                btn.setProperty('class', 'deactive')
                btn.setObjectName('swt_pre')
            else:
                btn.setProperty('class', 'active')
                btn.setObjectName('swt_' + b)
        frm.setLayout(f_layout)
        layout.addWidget(frm)

        self.setLayout(layout)
        # 绑定事件
        for btn in self.md_list:
            if btn.type == "add":
                btn.clicked.connect(self.ipt_add)
            elif btn.type == "decorate":
                btn.clicked.connect(self.ipt_decorate)

        self.work_ipt = self.top.frame_work.ipt

    def ipt_add(self):
        content = self.sender().content
        self.work_ipt.insertPlainText(content)

    def ipt_decorate(self):
        content = self.sender().content
        text = self.work_ipt.toPlainText()
        start = min(self.work_ipt.textCursor().position(), self.work_ipt.textCursor().anchor())
        end = max(self.work_ipt.textCursor().position(), self.work_ipt.textCursor().anchor())
        if start == end:
            return
        middle = text[start:end]
        text = text[0:start] + sub(r"([^\\])%", "\\1" + middle, content) + text[end:]
        self.work_ipt.setText(text)

    def switch_frame(self):
        el = self.sender()
        if el.text() == 'html':
            e = self.top.frame_work.html
        elif el.text() == 'md':
            e = self.top.frame_work.ipt
        else:
            e = self.top.frame_work.md
        e.setVisible((True if el.property('class') != 'active' else False))
        el.setProperty('class', 'active' if el.property('class') != 'active' else 'deactive')
        self.top.setStyleSheet(self.top.styleSheet())


class Set(QFrame):
    def __init__(self, top):
        super(Set, self).__init__()
        self.top = top


class Work(QFrame):
    def __init__(self, top):
        super(Work, self).__init__(top)
        self.top = top
        self.setObjectName("work")

        self.ipt = MdEdit(self)
        self.label_1 = ResizeLabel(self, 0, 2)
        self.html = HtmlEdit(self, self.label_1)
        self.label_2 = ResizeLabel(self, 2, 4)
        self.md = MdShow(self, self.label_2)
        self.md.setVisible(True)

        self.all_text = [self.ipt, 0, self.html, 0, self.md]
        layout = QGridLayout(self)
        layout.setSpacing(0)
        layout.addWidget(self.ipt, 0, 0)
        layout.addWidget(self.label_1, 0, 1)
        layout.addWidget(self.html, 0, 2)
        layout.addWidget(self.label_2, 0, 3)
        layout.addWidget(self.md, 0, 1)
        self.setLayout(layout)

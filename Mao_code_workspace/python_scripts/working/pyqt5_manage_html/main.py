import json
import os
import sys


from PyQt5.QtCore import QObject, QUrl, pyqtSignal, pyqtSlot
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QMainWindow

from common import INDEX_HTML_PATH, file_read, file_write_or_save
from common_html import generate_html, render_html_str
from common_tasks import BASE_TASK_HTML_DIR, TASK_HEADERS, Tasks
from common_team_members import TEAM_MEMBERS

# 系统默认设置为自动寻找代理，而使用代理后延迟会变得非常大。
# 解决方法也非常简单，关掉使用系统代理设定即可。
# QtNetwork.QNetworkProxyFactory.setUseSystemConfiguration(False)

task_main = Tasks()
cur_task_id = None


def init_html():
    generate_html('index.html')
    # generate_html('app-contacts.html')
    generate_html('app-tasks.html',
                  {
                      'tasks': task_main.get_today_tasks(),
                      'task_info_headers': TASK_HEADERS,
                      'team_member': TEAM_MEMBERS
                  })
    generate_html('task_create.html', {'team_member': TEAM_MEMBERS})
    # generate_html('task_modify.html', {'task': {}})


init_html()


class TInteractObj(QObject):
    sig_send_to_js = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.receive_str_from_js_callback = None

    @pyqtSlot(result=str)
    def get_data(self):
        print('call received')
        return 'hello, Python'

    @pyqtSlot(str)
    def receive_str_from_js(self, str):
        print('INFO: 从js接受到信息...')
        self.receive_str_from_js_callback(str)

    @pyqtSlot(str, result=str)
    def get_task_html_data_with_id(self, task_id):
        print(f'INFO [html content]: 从js接受到taskid={task_id}')
        task_dict = task_main.get_task_by_id(int(task_id))
        html_content = file_read(os.path.join(
            BASE_TASK_HTML_DIR, task_dict['content']))
        if html_content:
            # print(html_content)
            return html_content
        return "还未添加任何任务描述"

    @pyqtSlot(str, result=str)
    def get_task_data_with_id(self, task_id):
        global cur_task_id
        print(f'INFO [task_info]:  从js接受到taskid={task_id}')
        task_info = task_main.get_task_by_id(int(task_id))
        cur_task_id = int(task_info['id'])
        if task_info:
            killers_id_str = ""
            if task_info['killers']:
                killers = task_info['killers'].split(',<br>')
                for killer in killers:
                    killers_id_str += str(list(TEAM_MEMBERS.keys())[list(TEAM_MEMBERS.values()).index(killer)]) + ","
            # print(killers_id_str)
            generate_html('task_modify.html',
                          {'task': task_info, 'team_ids': killers_id_str, 'team_member': TEAM_MEMBERS,
                           'task_html': file_read(os.path.join(
                               BASE_TASK_HTML_DIR, task_info['content']))})
            return "task_modify beginning"
        return "task info is empty"

    @pyqtSlot(str, result=str)
    def get_task_progress_data_with_id(self, task_id):
        print(f'INFO [task_progress]:  从js接受到taskid={task_id}')
        task_info = task_main.get_task_by_id(int(task_id))
        if task_info:
            task_progress = task_info['progress_detail']
            # print(task_progress)
            html_content = render_html_str(
                'tasks/task_progress.html', {'progress_detail': task_progress, 'team_member': TEAM_MEMBERS})
            if html_content:
                return html_content
        return "progress file is empty"

    @pyqtSlot(str, result=str)
    def add_mod_del_task_progress(self, res):
        json_dic = json.loads(res)
        print(json_dic)
        op_type = json_dic['type']
        task_progress = json_dic['task_progress']
        task_id = json_dic['id']
        print(f'INFO [operate tasks]: 从js接受到op_type={op_type}')
        if op_type == 'add':
            if len(task_progress['id']):
                return task_main.modify_progress(task_id, task_progress)
            else:
                return task_main.add_progress(task_id, task_progress)
        elif op_type == 'del':
            return task_main.del_progress(task_id, task_progress)

    @pyqtSlot(str, result=str)
    def get_tasks_by_type(self, task_type):
        print(f'INFO [tasks]: 从js接受到task_type={task_type}')
        tasks = None
        if task_type == 'today':
            tasks = task_main.get_today_tasks()
        elif task_type == 'all':
            tasks = task_main.all_tasks
        elif task_type == 'history':
            tasks = task_main.get_all_done_tasks()
        elif task_type == 'trash':
            tasks = task_main.get_trashed_tasks()
        elif task_type == 'mine':
            tasks = task_main.get_mine_all_tasks()
        print(tasks)
        html_content = render_html_str('tasks/tasks_table.html', {
            'tasks': tasks,
            'task_info_headers': TASK_HEADERS
        })
        return html_content

    @pyqtSlot(str, result=str)
    def add_mod_del_task(self, res):
        json_dic = json.loads(res)
        print(json_dic)
        op_type = json_dic['type']
        task_info = json_dic['task_info']
        task_id = json_dic['task_info']['id']
        print(f'INFO [operate tasks]: 从js接受到op_type={op_type}')
        if op_type == 'add':
            return task_main.add_task(task_info)
        elif op_type == 'mod':
            return task_main.modify_task(task_info)
        elif op_type == 'del':
            return task_main.del_task(task_id)
        elif op_type == 'trash':
            return task_main.trash_task(task_info)


class Main(QMainWindow):
    """使用froala editor编辑器打开html,修改后返回html"""

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setWindowTitle(u'<<蓝魔札记>> -- 小若之札')
        # ---------- 窗口居中显示 --------------
        self.setMinimumSize(800, 600)
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)
        # ---------- 窗口居中显示 --------------

        self.showMaximized()
        self.webview = QWebEngineView(self)
        self.webview.setMinimumWidth(400)
        self.setCentralWidget(self.webview)
        self.webview.load(QUrl.fromLocalFile(INDEX_HTML_PATH))
        # self.webview.load(QUrl.fromLocalFile(os.path.join(os.path.dirname(__file__),'web/templates/NotionEditor2.html')))
        self.init_channel()
        self.task_new_id = int(task_main.get_new_id()
                               ) if task_main.get_new_id() else 0

    def init_channel(self):
        """为webview绑定交互对象"""
        self.interact_obj = TInteractObj(self)
        self.interact_obj.receive_str_from_js_callback = self.receive_data

        channel = QWebChannel(self.webview.page())
        # interact_obj 为交互对象的名字,js中使用.
        channel.registerObject("interact_obj", self.interact_obj)
        self.webview.page().setWebChannel(channel)

    def receive_data(self, data):
        global cur_task_id
        if not cur_task_id and self.task_new_id:
            task_id = self.task_new_id
        else:
            task_id = cur_task_id
            cur_task_id = None
        filename = os.path.join(
            BASE_TASK_HTML_DIR, str(task_id) + '.html')

        file_write_or_save(filename, data)
        print('INFO: save data success !')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Main()
    ui.show()
    sys.exit(app.exec_())

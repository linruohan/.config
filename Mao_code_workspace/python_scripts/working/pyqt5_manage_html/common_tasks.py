# *_*coding:utf-8 *_* 
__Author__ = 'xiaohan'

# 任务管理相关类
import os
from datetime import datetime

from common import file_read, file_write_or_save
from common_date import get_remain_date
from common_html import generate_html
from common_team_members import TEAM_MEMBERS

BASE_TASK_DIR = os.path.join(os.path.dirname(__file__), 'data/tasks')
BASE_TASK_HTML_DIR = os.path.join(BASE_TASK_DIR, 'tasks_html')
ALL_TASKS_FILE_PATH = os.path.join(BASE_TASK_DIR, 'all.json')
ALL_TRASHED_TASKS_FILE_PATH = os.path.join(BASE_TASK_DIR, 'del.json')
WORK_NUM = "mwx637260"
WORK_NAME = "毛金涛"
MY_TEAM = 'rtos'
TASK_HEADERS = ["ID", "任务名", '剩余时间', "百分比", "进展详情", '状态', '任务详情', "创建时间",
                "完成时间", "任务执行Owner",
                "任务创建者", "Team", "操作"]


class Tasks:
    def __init__(self):
        self.all_tasks = self.get_all_tasks()
        self.trashed_tasks = self.get_trashed_tasks()

    def get_task_by_id(self, task_id):
        """根据任务id获取任务"""
        task_id = int(task_id)
        for task in self.all_tasks:
            if task['id'] == task_id:
                return task
        return []

    @property
    def task_ids(self):
        if self.all_tasks:
            return [int(task['id']) for task in self.all_tasks]
        return []

    def get_tasks_by_key(self, key_str):
        """查询 包含关键字 的任务list"""
        print("INFO: search key in tasks...")
        result_tasks = []
        for task in self.all_tasks:
            progress_detail = '\n'.join([record['text'] for record in task['progress_detail']])
            html_content = file_read(os.path.join(BASE_TASK_HTML_DIR, task['Content']))
            for item in [task['name'], progress_detail, html_content]:
                if key_str in item:
                    result_tasks.append(task)
                    break
        return result_tasks

    def del_task(self, task_id):
        """根据任务id删除任务"""
        task_id = int(task_id)
        ids = [task['id'] for task in self.all_tasks]
        trashed_ids = [task['id'] for task in self.trashed_tasks]
        if task_id in ids:
            task = self.all_tasks[ids.index(task_id)]
            self.all_tasks.remove(task)
            self.trashed_tasks.append(task)
            self.save_task()
            self.save_trashed_task()
            print(f"INFO: del {task['name']} ...")
            return 'INFO: delete success!'
        elif task_id in trashed_ids:
            self.trash_task(task_id)
            return "INFO: trash restore success !"
        else:
            print(f'WARNING: task with task_id: {task_id} is not exists ! ')
            return f'INFO: delete fail! WARNING: task with task_id: {task_id} is not exists ! '

    def get_new_id(self):
        if self.task_ids:
            return max(self.task_ids) + 1
        return 0

    def add_task(self, parse_task):
        if int(parse_task['id']) == 99999:
            task_id = self.get_new_id()
        else:
            task_id = int(parse_task['id'])
        print(task_id)
        parse_task['id'] = task_id
        parse_task['content'] = str(task_id) + '.html'
        parse_task['creator'] = WORK_NUM
        parse_task['left_time'] = get_remain_date(parse_task['end_date'],
                                                  '%Y-%m-%d %H:%M')
        self.all_tasks.append(parse_task)

        self.save_task()
        return 'INFO: Add success !'

    def save_task(self):
        generate_html('app-tasks.html',
                      {
                          'tasks': self.get_today_tasks(),
                          'task_info_headers': TASK_HEADERS,
                          'team_member': TEAM_MEMBERS
                      })
        file_write_or_save(ALL_TASKS_FILE_PATH, {
            'detail': self.all_tasks
        })

    def save_trashed_task(self):
        generate_html('app-tasks.html',
                      {
                          'tasks': self.get_today_tasks(),
                          'task_info_headers': TASK_HEADERS,
                          'team_member': TEAM_MEMBERS
                      })
        file_write_or_save(ALL_TRASHED_TASKS_FILE_PATH, {
            'detail': self.trashed_tasks
        })

    def modify_task(self, parse_task):
        """添加一条新任务/修改已有的任务"""
        if parse_task['id'] not in self.task_ids:
            print(f"INFO: modify {parse_task['name']}  task id is not existed, check...")
            return 'ERROR: task with id not existed ！'
        else:
            self.all_tasks.remove(self.get_task_by_id(int(parse_task['id'])))
            print(f"INFO: modify {parse_task['name']} ...")
            parse_task['left_time'] = get_remain_date(parse_task['end_date'],
                                                      '%Y-%m-%d %H:%M')
            self.all_tasks.append(parse_task)
            self.save_task()
            return 'INFO: modify success !'

    def trash_task(self, task_id):
        """从回收站删掉该任务"""
        parse_task = None
        for task in self.trashed_tasks:
            if task['id'] == task_id:
                parse_task = task
        if parse_task:
            self.add_task(parse_task)
            self.trashed_tasks.remove(parse_task)
            self.save_trashed_task()

    def get_task_records_by_filename(self, file_name):
        task_records = []
        file_path = os.path.join(BASE_TASK_DIR, file_name)
        if os.path.exists(file_path) and os.path.getsize(file_path):
            task_records = file_read(file_path)['detail']
        else:
            print(f'WARNING: {file_path} is empty or non exist !!')
        if task_records and len(task_records):
            for record in task_records:
                # print(record)
                record['left_time'] = get_remain_date(record['end_date'],
                                                      '%Y-%m-%d %H:%M')
            return task_records
        return []

    def get_all_tasks(self):
        return self.get_task_records_by_filename('all.json')

    def get_mine_all_tasks(self):
        """我创建的未完成的任务"""
        if self.all_tasks:
            result = [task for task in self.all_tasks if
                      (task['creator'] == WORK_NUM or task['team'] == 'mine') and task['state'] != 'done']
            return result
        return []

    def get_today_tasks(self):
        """属于我的未完成的任务"""
        if self.all_tasks:
            result = [task for task in self.all_tasks if WORK_NUM in str(task['killers']) and task['state'] != 'done']
            return result
        return []

    def get_doing_tasks(self, team):
        """团队未完成的任务"""
        if self.all_tasks:
            result = [task for task in self.all_tasks if task['team'] == team and task['state'] != 'done']
            return result
        return []

    def get_done_tasks(self, team):
        """团队已完成的任务"""
        if self.all_tasks:
            result = [task for task in self.all_tasks if task['team'] == team and task['state'] == 'done']
            return result
        return []

    def get_all_done_tasks(self):
        """所有已完成的任务"""
        if self.all_tasks:
            result = [task for task in self.all_tasks if task['state'] == 'done']
            return result
        return []

    def get_trashed_tasks(self):
        """所有删除的任务"""
        return self.get_task_records_by_filename('del.json')

    def add_progress(self, task_id, parse_progress):
        task = self.get_task_by_id(task_id)
        if task:
            progress_id = len(task['progress_detail']) if len(task['progress_detail']) else 0
            self.all_tasks.remove(task)
            now = datetime.strptime(":".join(str(datetime.now()).split('.')[0].split(":")[:-1]), '%Y-%m-%d %H:%M')
            parse_progress['time'] = str(now)
            parse_progress['id'] = progress_id
            task['progress_detail'].append(parse_progress)
            self.all_tasks.append(task)
            self.save_task()
            return 'INFO: add progress success !'

    def modify_progress(self, task_id, parse_progress):
        task = self.get_task_by_id(task_id)
        if task:
            print(task)
            for progress in task['progress_detail']:
                if int(progress['id']) == int(parse_progress['id']):
                    print("find it .................", progress)
                    self.all_tasks.remove(task)
                    task['progress_detail'].remove(progress)
                    print("12222222222222222222222")
                    task['progress_detail'].append(parse_progress)
                    self.all_tasks.append(task)
                    self.save_task()
                    return 'INFO: mod progress success !'

    def del_progress(self, task_id, parse_progress):
        task = self.get_task_by_id(task_id)
        if task:
            for progress in task['progress_detail']:
                print(progress['id'], int(parse_progress['id']))
                if int(progress['id']) == int(parse_progress['id']):
                    self.all_tasks.remove(task)
                    task['progress_detail'].remove(progress)
                    self.all_tasks.append(task)
                    self.save_task()
                    return 'INFO: del progress success !'
        return 'WARN: parse_progress is not existed !'


if __name__ == '__main__':
    t = Tasks()
    print(t.all_tasks)
    for i in t.all_tasks:
        # print(i)
        pass

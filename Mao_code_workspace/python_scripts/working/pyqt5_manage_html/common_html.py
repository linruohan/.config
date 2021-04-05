# *_*coding:utf-8 *_* 
__Author__ = 'xiaohan'

import os

from jinja2 import Environment, FileSystemLoader

from common import TEMPLATES_DIR, WEB_MAIN_DIR, file_write_or_save

RENDER_HTML_DIR = os.path.join(os.path.dirname(__file__), 'html_tmp')


def generate_html(filename, data={}):
    """使用jinja2 导入data生成html文件"""
    template = Environment(loader=FileSystemLoader(TEMPLATES_DIR)).get_template(filename)
    html = template.render(data)
    file_write_or_save(os.path.join(WEB_MAIN_DIR, filename), html)
    print(f'INFO: generate html={filename} success!')


def render_html_str(filename, data={}):
    """使用jinja2 导入data生成html字符串并返回"""
    template = Environment(loader=FileSystemLoader(RENDER_HTML_DIR)).get_template(filename)
    html = template.render(data)
    print(f'INFO: render html={filename} success!')
    return html


if __name__ == '__main__':
    print('')
    # html = render_html_str('tasks/tasks_show.html', {})
    # print(html)

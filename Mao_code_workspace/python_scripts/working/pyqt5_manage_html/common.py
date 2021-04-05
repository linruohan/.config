# *_*coding:utf-8 *_*
__Author__ = 'xiaohan'

import json
import os

WEB_TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), 'web/templates/')
WEB_MAIN_DIR = os.path.join(WEB_TEMPLATES_DIR, 'admin')
TEMPLATES_DIR = os.path.join(WEB_MAIN_DIR, 'tmp')
INDEX_HTML_PATH = os.path.join(WEB_MAIN_DIR, 'index.html')


def file_read(filename):
    if not os.path.exists(filename): return None
    with open(filename, 'r', encoding='utf-8') as f:
        print(f'INFO: read [{filename}] success !')
        return json.load(f) if filename.endswith('.json') else f.read()


def file_write_or_save(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        if filename.endswith('.json'):
            json.dump(data, f, ensure_ascii=False)
        else:
            f.write(data)
        print(f"INFO: write {filename} success !")

if __name__ == '__main__':
    pass

# *_*coding:utf-8 *_* 
__Author__ = 'xiaohan'

from jinja2 import Environment, FileSystemLoader

template = Environment(loader=FileSystemLoader('./')).get_template('./index.html')

if __name__ == '__main__':
    headers = [1, 2, 3]
    rows = [2, 2, 2]
    html = template.render(headers=headers, rows=rows)
    print(html)

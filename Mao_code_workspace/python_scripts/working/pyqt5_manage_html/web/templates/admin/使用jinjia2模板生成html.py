# *_*coding:utf-8 *_* 
__Author__ = 'xiaohan'

from jinja2 import Environment, FileSystemLoader


def create_html(tmp_dir, filename, data):
    template = Environment(loader=FileSystemLoader(tmp_dir)).get_template(filename)
    html = template.render(data)
    filename = filename.replace('tmp/', '')
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'created {tmp_dir}/{filename} success!')


if __name__ == '__main__':
    create_html('', 'tmp/task_create.html', {})

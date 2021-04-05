import eel
import json, os
import pathlib, shutil
import sys

eel.init('./web')


@eel.expose
def rename(path, old, new):
    if old == new: return
    newpath = path.replace(old, new)
    print(path, newpath)
    os.rename(path, newpath)


@eel.expose
def newdir(path):
    if os.path.exists(path): return
    os.mkdir(path)
    print(path + "  create success")


@eel.expose
def moveToTrash(filepath):
    newpath = './trash/' + filepath.replace('./', '/')
    if not os.path.exists(os.path.dirname(newpath)):
        os.makedirs(os.path.dirname(newpath))
    os.rename(filepath, newpath)


@eel.expose
def createFile(path):
    # pathlib.Path(path).touch()
    jsonDemo = {
        "time": 1589469898956,
        "blocks": [
            {
                "type": "paragraph",
                "data": {
                    "text": ""
                }
            }
        ],
        "version": "2.17.0"
    }
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(jsonDemo, f)
    print(f'create {path} success')


@eel.expose
def get_dirs():
    path = './data'
    result_list = []
    pid_index = 0
    ids = {}
    for root, dirs, files in os.walk(path):
        # print(root,dirs,files)
        ids[root] = pid_index
        key = root if root == path else os.path.dirname(root)
        for dir in dirs:
            ids[os.path.join(root, dir)] = pid_index
        result_list.append({
            'id': pid_index,
            'pId': ids[key],
            'name': root.split('\\')[-1].replace('./', ''),
            'path': root,
            'parrent': True,
            "open": True,
        })
        for i in range(len(files)):
            result_list.append({
                'id': (pid_index + 1) * 10000 + i + 1,
                'pId': ids[root],
                'name': files[i],
                'path': os.path.join(root, files[i]),
            })
        pid_index += 1

    return result_list


@eel.expose
def save(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(data)
        print(filename + ' 保存成功!')


@eel.expose
def openfile(filename):
    if not str(filename).endswith('.json'):
        filename += '.json'
    with open(filename, 'r', encoding='utf-8') as f:
        string = json.loads(f.read())
    return string


eel.start('web/templates/NotionEditor2.html')

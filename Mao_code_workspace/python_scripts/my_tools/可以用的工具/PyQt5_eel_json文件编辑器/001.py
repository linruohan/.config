# coding=utf-8
import os


def get_dirs():
    path = './data'
    result_list = []
    pid_index = 0
    ids = {}
    for root, dirs, files in os.walk(path):
        print(root, dirs, files)
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
        })
        for i in range(len(files)):
            result_list.append({
                'id': (pid_index+1)*10000+i+1,
                'pId': ids[root],
                'name': files[i],
                'path': os.path.join(root, files[i]),
            })
        pid_index += 1
    print(ids)
    for i in result_list:
        print(i)


def get_dirs2():
    path = './data'
    nodes = []
    id = 0
    for root, dirs, files in os.walk(path):
        children = []
        if len(dirs):
            for dir in dirs:
                children.append({
                    "id": id,
                    "name": dir,
                    "path": os.path.join(root, dir),
                    "parrent": True
                })
                id += 1
        if len(files):
            for file in files:
                children.append({
                    "id": id,
                    "name": file,
                    "path": os.path.join(root, file),
                })
                id += 1

        root_nodes = {
            "id": id,
            "name": root,
            "path": root,
            "open": True,
            "children": children
        }
        nodes.append(root_nodes)
    for i in nodes:
        print(i, '\n', "="*100)
        for k, v in i.items():
            print(k, v)


def get_dirs3(root):
    file_list = []
    for i in os.listdir(root):
        if os.path.isdir(os.path.join(root, i)):
            dir = os.path.join(root, i)
            get_dirs3(dir)
        else:
            file_list.append(os.path.join(root, i))
    return file_list


if __name__ == '__main__':
    get_dirs()
    print("hello 我的")
    # # print(os.listdir('./data'))
    # for i in get_dirs3('./data'):
    #     print(i)

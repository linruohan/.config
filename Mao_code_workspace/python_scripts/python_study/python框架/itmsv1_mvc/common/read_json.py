# -*- coding:utf-8 -*-
import json
# loads: 将 字符串 转换为 字典
def loads(path):
    with open(path) as f:
        data = json.load(f)
        print(data)
        return data
def store(path,data):
    with open (path, 'w') as f:
        f.write (json.dumps (data))
    return None
if __name__ == '__main__':
    data={'bigberg': [7600, {1: [['iPhone', 6300], ['Bike', 800], ['shirt', 300]]}]}
    path='001.json'
    store (path, data)
    loads (path)
# test_dict = {'bigberg': [7600, {1: [['iPhone', 6300], ['Bike', 800], ['shirt', 300]]}]}
# son_str = json.dumps (test_dict)
# new_dict = json.loads(json_str)

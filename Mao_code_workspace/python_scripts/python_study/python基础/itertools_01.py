import itertools

#无限迭代器
'''因为count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来，只能按Ctrl+C退出。

cycle()会把传入的一个序列无限重复下去：'''
# natuals=itertools.count(2)
# for i in natuals:
#     print(i)

# cs=itertools.cycle('acd')
# for i in cs:
#     print(i)

# ns=itertools.repeat('S',4)
# for i in ns:
#     print(i)

# for i in itertools.chain('Ssdf','fdsf'):
#     print(i)

# for key,group in itertools.groupby('sadddssaaaggdd'):
#     print(key,list(group))

for key,group in itertools.groupby('sadddssaaaGgdd',lambda x:x.upper()):
    print(key,list(group))

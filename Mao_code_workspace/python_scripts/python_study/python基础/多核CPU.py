# -*- coding: utf-8 -*-
import sys,io

sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
import multiprocessing,threading

print(multiprocessing.cpu_count())
import threading
from time import sleep, ctime

# 买票的人
users = {'小王': 2, '小李': 1, '小赵': 4, '小刘': 5, '小周': 8, '小吴': 4, '小郑': 3, '小钱': 6,}


# 站台窗口

def buy_ticket(name, time):
    print('%s 开始买票 ，run>>>，时间：%s' % (name, ctime()))
    sleep(time)
    print('%s 买完票了,走了end <<<，时间：%s' % (name, ctime()))

# 写数据进程执行的代码:
threads = []

# 创建线程
for name, time in users.items():
    t = threading.Thread(target= buy_ticket, args=(name,time))
    threads.append(t)

if __name__ == '__main__':

    # 启动线程
    count = range(len(users))
    for i in count:
        threads[i].start()
    for i in count:
        threads[i].join()

    # 主线程
    print('All end:%s' % ctime())

# *_*coding:utf-8 *_* 
__Author__ = 'xiaohan'
import datetime
import time
from threading import Timer

import psutil
import schedule
from apscheduler.schedulers.blocking import BlockingScheduler

'''
=======================================================
========            定时任务 4种方法      
简单总结上面四种定时定点任务实现：
1：循环 + sleep 方式适合简答测试，
2：timer 可以实现定时任务，但是对定点任务来说，需要检查当前时间点；
3：schedule 可以定点定时执行，但是需要在循环中检测任务，而且存在阻塞；
4：APScheduler 框架更加强大，可以直接在里面添加定点与定时任务；

综合考虑，决定使用 APScheduler 框架，实现简单，只需要直接创建任务，并将添加到调度器中即可。              
=======================================================
'''
# psutil:获取系统信息模块，可以获取CPU，内存，磁盘等的使用情况
# logfile：监测信息写入文件
# ========================sleep==========================================
'''
def MonitorSystem(logfile=None):
    # 获取cpu使用情况
    cpuper = psutil.cpu_percent()
    # 获取内存使用情况：系统内存大小，使用内存，有效内存，内存使用率
    mem = psutil.virtual_memory()
    # 内存使用率
    memper = mem.percent
    # 获取当前时间
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    line = f'{ts} cpu:{cpuper}%, mem:{memper}%'
    print(line)
    if logfile:
        logfile.write(line)
def MonitorNetWork(logfile=None):
    # 又来了新任务：需要每秒监测网络收发字节，代码实现如下：
    netinfo = psutil.net_io_counters()  # 获取网络收信息
    now = datetime.datetime.now()  # 获取当前时间
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    line = f'{ts} bytessent={netinfo.bytes_sent}, bytesrecv={netinfo.bytes_recv}'
    print(line)
    if logfile:
        logfile.write(line)

def loopMonitor():
    # 只能处理单个定时任务。
    while True:
        MonitorSystem()
        # 3s检查一次
        time.sleep(3)
'''

# ========================Timer==========================================
# 从时间中可以看到，这两个任务可以同时进行不存在等待问题。
# Timer 的实质是使用线程方式去执行任务，每次执行完后会销毁，所以不必担心资源问题。
def MonitorSystem(logfile=None):
    cpuper = psutil.cpu_percent()
    mem = psutil.virtual_memory()
    memper = mem.percent
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    line = f'{ts} cpu:{cpuper}%, mem:{memper}%'
    print(line)
    if logfile:
        logfile.write(line)
    # 启动定时器任务，每三秒执行一次
    Timer(3, MonitorSystem).start()
def MonitorNetWork(logfile=None):
    netinfo = psutil.net_io_counters()
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    line = f'{ts} bytessent={netinfo.bytes_sent}, bytesrecv={netinfo.bytes_recv}'
    print(line)
    if logfile:
        logfile.write(line)
    # 启动定时器任务，每秒执行一次
    Timer(1, MonitorNetWork).start()

# =============================Timer=====================================
# 从时间中可以看到，这两个任务可以同时进行不存在等待问题。
# Timer 的实质是使用线程方式去执行任务，每次执行完后会销毁，所以不必担心资源问题。
# =============================schedule=====================================
def func():
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    print('do func time :', ts)
def func2():
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    print('do func2 time：', ts)
def tasklist():
    # 清空任务
    schedule.clear()
    # 创建一个按秒间隔执行任务
    schedule.every(1).seconds.do(func)
    schedule.every(1).minutes.do(func)
    schedule.every(1).days.do(func)
    schedule.every(1).weeks.do(func)
    schedule.every(1).monday.do(func)
    schedule.every(1).monday.at('12:00').do(func)
    # 创建一个按2秒间隔执行任务
    schedule.every(2).seconds.do(func2)
    # 执行10S
    for i in range(10):
        schedule.run_pending()
        time.sleep(1)

# 这种方式局限性：如果工作任务回非常耗时就会影响其他任务执行。我们可以考虑使用并发机制配置这个模块使用。
# =============================schedule=====================================


# =============================apscheduler=====================================
# apscheduler组件及简单说明：
# 1 > triggers（触发器）：触发器包含调度逻辑，每一个作业有它自己的触发器
# 2 > job stores（作业存储）: 用来存储被调度的作业，默认的作业存储器是简单地把作业任务保存在内存中, 支持存储到 MongoDB，Redis数据库中
# 3 > executors（执行器）：执行器用来执行定时任务，只是将需要执行的任务放在新的线程或者线程池中运行
# 4 > schedulers（调度器）：调度器是将其它部分联系在一起, 对使用者提供接口，进行任务添加，设置，删除。

def func():
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    print('do func time :', ts)
def func2():
    # 耗时2S
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    print('do func2 time：', ts)
    time.sleep(2)
def dojob():
    # 创建调度器：BlockingScheduler
    scheduler = BlockingScheduler()
    # 添加任务,时间间隔2S
    scheduler.add_job(func, 'interval', seconds=2, id='test_job1')
    # 添加任务,时间间隔5S
    scheduler.add_job(func2, 'interval', seconds=3, id='test_job2')
    scheduler.start()
# =============================apscheduler=====================================
if __name__ == '__main__':
    dojob()

import time,random,queue
from  multiprocessing.managers import BaseManager

# 发送任务的队列:
task_queue = queue.Queue()
# 接收结果的队列:
result_queue=queue.Queue()

class QueueMannager(BaseManager):
    pass

# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
QueueMannager.register('get_task_queue')
QueueMannager.register('get_result_queue')

#连接到服务器，也就是运行task_master.py的机器：
server_addr='127.0.0.1'
print('connect to server %s'% server_addr)

#端口和验证码注意保持和task——master。py中完全一致：

m=QueueMannager(address=(server_addr,5000),authkey=b'abc')

#从网络连接
m.connect()

#接受queue的对象：
task=m.get_task_queue()
task=m.get_result_queue()
#从task队列取任务，并把结果写入result队列
for i in range(10):
    try:
        n=task.get(timeout=1)
        print('run task %d * %d...'%(n,n))
        r='%d * %d = %d' %(n,n,n*n)
        time.sleep()
        result.put(r)
    except Queue.Empty:
        print('task queue is empty.')
#处理结束
print('worker exit.')

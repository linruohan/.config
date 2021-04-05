#coding==utf-8
import psutil
import sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
#cpu逻辑数量
cpu_count=psutil.cpu_count()
#cpu物理核心
physical_cpu_count=psutil.cpu_count(logical=False)


print('cpu逻辑数量:',cpu_count)
print('cpu物理核心:',physical_cpu_count)


# 统计cpu的用户、系统、空闲时间
print(psutil.cpu_times())


#cpu使用率，没秒刷新一次

# for x in range(10):
#     print(psutil.cpu_percent(interval=1,percpu=True))

#获取内存信息
#物理内存信息
print(psutil.virtual_memory())
# 交换内存信息
print(psutil.swap_memory())


# 获取磁盘信息

print('磁盘分区信息',psutil.disk_partitions())
print('磁盘使用情况',psutil.disk_usage('/'))
print('磁盘IO',psutil.disk_io_counters())

#获取网络信息
print('网络读写字节/包的个数',psutil.net_io_counters())
print('网络接口信息',psutil.net_if_addrs())
print('网络接口状态',psutil.net_if_stats())
print('当前网络连接信息',psutil.net_connections())


#获取进程信息
# print('所有进程ID信息',psutil.pids())
# p=psutil.Process(11196)
# print('指定进程名称信息',p.name())
# print('指定进程exe路径',p.exe())
# print('指定进程工作目录',p.cwd())
# print('指定进程启动的命令行',p.cmdline())
# print('指定进程的父进程ID',p.ppid())
# print('指定进程的父进程',p.parent())
# print('指定进程的子进程列表',p.children())
# print('指定进程的状态',p.status())
# print('指定进程的用户名',p.username())
# print('指定进程的创建时间',p.create_time())
# # print('指定进程的终端',p.terminal())
# print('指定进程使用的cpu时间',p.cpu_times())
# print('指定进程使用的内存',p.memory_info())
# print('指定进程打开的文件',p.open_files())
# print('指定进程相关网络连接',p.connections())
# print('指定进程线程数',p.num_threads())
# print('指定进程线程信息',p.threads())
# print('指定进程环境变量',p.environ())
# print('指定 结束进程',p.terminate())


print(psutil.test())

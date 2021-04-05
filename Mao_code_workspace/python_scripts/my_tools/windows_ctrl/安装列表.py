import winreg
import wmi
from win32com.client import GetObject

# wmi的名称空间，获取当前计算机的名称空间：
from win32com.client import GetObject
import pywintypes


def enum_namespace(name):
    try:
        wmi = GetObject('winmgmts:/' + name)
        namespaces = wmi.InstancesOf('__Namespace')
        for namespace in namespaces:
            enum_namespace('{name}/{subname}'.format(name=name, subname=namespace.Name))
    except pywintypes.com_error:
        print(name, 'limit of authority')
    else:
        print(name)


enum_namespace('root')
# 获取硬盘信息
c = wmi.WMI()
i = 0

for disk in c.Win32_LogicalDisk(DriveType=3):
    # print(disk)
    b = disk.Caption
    a = round(int(disk.Size) / (1024 * 1024 * 1024), 2)
    i = round(i + a, 2)
    print(b, '容量为:', a, 'GB', end='\n')

print('硬盘的总容量为:', i, 'GB')
# 获取CPU信息与内存信息, 操作系统版本, 计算机序列号
c = wmi.WMI()
for cpu in c.Win32_Processor():
    aa = cpu.Name
print('CPU型号为：', aa)
for memory in c.CIM_Chip():
    bb = round(int(memory.Capacity) / (1024 * 1024 * 1024))
print('内存大小为:', bb, "GB")
for sy in c.CIM_OperatingSystem():
    cc = sy.Caption
print("操作系统版本为:", cc)
cc1 = sy.CSName
print('计算机名为:', cc1)
for sn in c.Win32_BIOS():
    dd = sn.SerialNumber
print('计算机产品编号为:', dd)
# 查看本地连接网卡（有线网卡）MAC地址
c = wmi.WMI()
for zz in c.Win32_NetworkAdapter():
    zz1 = '本地'
    zz2 = zz.NetConnectionID
    if zz2 == None:  # python中单等号为赋值，双等号为条件判断. python if语句不允许赋值再判断.
        continue  # none,continue 是为了空值时可以继续执行，否则为出错。
    elif zz1 in zz2:
        zz3 = zz.MACAddress
print('本地网卡物理地址为:', zz3)
# 获取本地网卡MAC地址的另一种写法。(更为友好一些。)
from win32com.client import GetObject

wmi = GetObject('winmgmts:/root/cimv2')
# wmi = GetObject('winmgmts:') #更简单的写法
pro = wmi.ExecQuery('Select * from Win32_NetworkAdapter where NetConnectionID like "本地%"')  # WQL语句中like用%匹配后面的字符
for p in pro:
    print('本地网卡MAC地址为:', p.MACAddress)

# 查看系统进程列表：
c = wmi.WMI()
for zz in c.Win32_Process():
    cap = zz.Caption
    print(cap)
# 查看已安装软件列表：
c = wmi.WMI()
for zz in c.Win32_Product():
    cap = zz.Caption
    print(cap)
# 查看已安装补丁列表：
c = wmi.WMI()
for zz in c.Win32_QuickFixEngineering():
    na = zz.HotFixID

    print(na)

#!/usr/bin/env python
# coding:utf-8

import winreg
import wmi
import os
import sys
import platform
import time
import wmi
from winreg import (HKEY_LOCAL_MACHINE, KEY_ALL_ACCESS, OpenKey, EnumValue, QueryValueEx)


def sys_version():
    c = wmi.WMI()
    # 获取操作系统版本
    for sys in c.Win32_OperatingSystem():
        print("Version:%s" % sys.Caption.encode("UTF8"), "Vernum:%s" % sys.BuildNumber)
        print(sys.OSArchitecture.encode("UTF8"))  # 系统是32位还是64位的)
        print(sys.OSArchitecture)  # 系统是32位还是64位的)
        print(sys.NumberOfProcesses)  # 当前系统运行的进程总数


def cpu_mem():
    c = wmi.WMI()
    print(c._wmi_namespace.__name__)
    # CPU类型和内存
    for processor in c.Win32_Processor():
        # print( "Processor ID: %s" % processor.DeviceID)
        print("Process Name: %s" % processor.Name.strip())
    for Memory in c.Win32_PhysicalMemory():
        print("Memory Capacity: %.fMB" % (int(Memory.Capacity) / 1048576))


def cpu_use():
    # 5s取一次CPU的使用率
    c = wmi.WMI()
    while True:
        for cpu in c.Win32_Processor():
            timestamp = time.strftime('%a, %d %b %Y %H:%M:%S', time.localtime())
            print('%s | Utilization: %s: %d %%' % (timestamp, cpu.DeviceID, cpu.LoadPercentage))
            time.sleep(5)


def disk():
    c = wmi.WMI()
    # 获取硬盘分区
    for physical_disk in c.Win32_DiskDrive():
        for partition in physical_disk.associators("Win32_DiskDriveToDiskPartition"):
            for logical_disk in partition.associators("Win32_LogicalDiskToPartition"):
                print(physical_disk.Caption.encode("UTF8"), partition.Caption.encode("UTF8"), logical_disk.Caption)

    # 获取硬盘使用百分情况
    for disk in c.Win32_LogicalDisk(DriveType=3):
        print(disk.Caption, "%0.2f%% free" % (100.0 * float(disk.FreeSpace) / float(disk.Size)))


def services():
    wmiobj = wmi.WMI()
    services = wmiobj.Win32_Service()
    for i in services:
        print("%d:%s -> %s [%s]" % (services.index(i) + 1, i.Name, i.Caption, i.State))


def network():
    c = wmi.WMI()
    # 获取MAC和IP地址
    for interface in c.Win32_NetworkAdapterConfiguration(IPEnabled=1):
        print("MAC: %s" % interface.MACAddress)
    for ip_address in interface.IPAddress:
        print("ip_add: %s" % ip_address)
    print()

    # 获取自启动程序的位置
    for s in c.Win32_StartupCommand():
        print("[%s] %s <%s>" % (s.Location.encode("UTF8"), s.Caption.encode("UTF8"), s.Command.encode("UTF8")))

    # 获取当前运行的进程
    for process in c.Win32_Process():
        print(process.ProcessId, process.Name)


def get_installed_app_in_window():
    # 获取应用程序安装列表

    HKEY_CLASSES_ROOT = 2147483648
    HKEY_CURRENT_USER = 2147483649
    HKEY_LOCAL_MACHINE = 2147483650
    HKEY_USERS = 2147483651
    HKEY_CURRENT_CONFIG = 2147483653

    REG_SZ = 1
    REG_EXPAND_SZ = (2)
    REG_BINARY = (3)
    REG_DWORD = (4)
    REG_MULTI_SZ = (7)
    REG_QWORD = (11)

    oReg = wmi.WMI(
        moniker=r"winmgmts:{impersonationLevel=impersonate}!\\" + '.' + r"\root\default:StdRegProv",
    )
    # 需要遍历的两个注册表
    sub_key = [r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall',
               r'SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall']

    sSubKeyName = r"Software\Microsoft\Windows\CurrentVersion\Uninstall"

    result, keys = oReg.EnumKey(
        hDefKey=HKEY_LOCAL_MACHINE,
        sSubKeyName=sSubKeyName)
    sPossibleValues = []
    listResult = []

    if result == 0:

        intTotalNumberOfInstalledApps = len(keys)

        # Each key is a single application.
        for key in keys:
            __singleApplicationData = []

            # print key
            path = sSubKeyName + '\\' + key
            subResult, sNames, sIntType = oReg.EnumValues(
                hDefKey=HKEY_LOCAL_MACHINE,
                sSubKeyName=path,
            )

            if "DisplayName" not in sNames:
                __singleApplicationData.append(["DisplayName", key])
            for x in range(0, len(sNames)):
                if sIntType[x] == REG_SZ or sIntType[x] == REG_EXPAND_SZ or sIntType[x] == REG_MULTI_SZ:
                    if [sNames[x], sIntType[x]] not in sPossibleValues:
                        sPossibleValues.append([sNames[x], sIntType[x]])

                    subResult, strValueName = oReg.GetStringValue(
                        hDefKey=HKEY_LOCAL_MACHINE,
                        sSubKeyName=sSubKeyName + '\\' + key,
                        sValueName=sNames[x],
                    )

                    # Only insert to result if the value & name is of len > 0
                    if subResult == 0 and (
                            (len(sNames[x]) > 0 and len(strValueName) > 0) or (sNames[x] == "DisplayName")):
                        __singleApplicationData.append([sNames[x], strValueName])

            if (len(__singleApplicationData) > 0):
                listResult.append(__singleApplicationData)
    for i in listResult: print(i)


def main():
    # sys_version()
    cpu_mem()
    # disk()
    # network()
    # cpu_use()


if __name__ == '__main__':
    main()
# print(platform.system())
# print(platform.release())
# print(platform.version())
# print(platform.platform())
# print(platform.machine())

# r = wmi.WMI(namespace='DEFAULT').StdRegProv
# r = wmi.GetObject("winmgmts:/root/default:StdRegProv")
# print(r)
# print('*'*100)
# print(winreg.HKEY_LOCAL_MACHINE)
# # r=r.StdRegProv
# result,values = r.EnumKey(
#     hDefKey=winreg.HKEY_LOCAL_MACHINE, sSubKeyName="Software")
# for key in values:
#     print(key)

# c = wmi.WMI(computer="DESKTOP-RUN5M82",user="xiaohan",password="1",namespace="root/default").StdRegProv

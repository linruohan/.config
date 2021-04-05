# coding=utf-8
import os
import socket
import winreg

#将软件安装列表输出到网盘上
# os.system(r'net use p: \\10.0.0.6\public password /user:Lc\tanjun')

#使用主机名命名软件安装列表
# hostname = socket.gethostname()
hostname='localhost'
file = open(r'%s.txt' % hostname, 'a')

#需要遍历的两个注册表
sub_key = [r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall', r'SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall']

software_name = []

for i in sub_key:
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, i, 0, winreg.KEY_ALL_ACCESS)
    for j in range(0, winreg.QueryInfoKey(key)[0]-1):
        try:
            key_name = winreg.EnumKey(key, j)
            key_path = i + '\\' + key_name
            each_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_ALL_ACCESS)
            DisplayName, REG_SZ = winreg.QueryValueEx(each_key, 'DisplayName')
            DisplayName = DisplayName.encode('utf-8')
            software_name.append(DisplayName)
            print(DisplayName)
        except WindowsError:
            pass

#去重排序
software_name = list(set(software_name))
software_name = sorted(software_name)

for result in software_name:
    file.write(result + '\n')
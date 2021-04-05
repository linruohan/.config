# -*- coding: gbk -*-
import winreg
import sys


# python有内置的注册表操作库--winreg（在33版本中为winreg，在2x版本为_winreg).

def all():
    # 1.打开键，枚举键值
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                         r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\{166AFB9D-6834-49CA-90AA-AA18F924ADA7}",
                         reserved=0, access=winreg.KEY_READ)
    try:
        i = 0
        while 1:
            k, v, t = winreg.EnumValue(key, i)
            print(k, v)
            i += 2
    except OSError:
        print("打开键失败")
    winreg.CloseKey(key)


def create_set():
    # 2.创建键，以及设置键值
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE", access=winreg.KEY_READ | winreg.KEY_SET_VALUE)
    try:
        handle = winreg.CreateKey(key, r"test")
        winreg.SetValue(key, r"test", winreg.REG_SZ, "199999")
    except OSError:
        print("创建键失败")
    winreg.CloseKey(key)


def delete():
    # 3.删除键
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE",
                         access=winreg.KEY_READ | winreg.KEY_SET_VALUE | winreg.KEY_QUERY_VALUE)
    try:
        if winreg.CreateKey(key, r"test"):
            print("test键创建成功")
        else:
            sys.exit(1)
        winreg.SetValue(key, r"test", winreg.REG_SZ, "199999")
        winreg.DeleteKey(key, r"test")
    except OSError:
        print("faied!!")
    winreg.CloseKey(key)

if __name__ == '__main__':
    all()
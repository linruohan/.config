# 改写注册表文件开机自启
import win32con
import win32api
import os


def addfile2autorun(path):
    "注册到启动项"
    runpath = "Software\Microsoft\Windows\CurrentVersion\Run"
    hKey = win32api.RegOpenKeyEx(
        win32con.HKEY_CURRENT_USER, runpath, 0, win32con.KEY_SET_VALUE)
    (filepath, filename) = os.path.split(path)
    win32api.RegSetValueEx(hKey, "WindowsInit", 0, win32con.REG_SZ, path)
    win32api.RegCloseKey(hKey)


addfile2autorun('D:\\Python源码\\Django.py')

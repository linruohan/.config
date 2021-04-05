from cx_Freeze import Executable, setup

'''使用cx_Freeze 将Python打包成exe文件
Python setup.py  build

'''
import os, sys

os.environ['TCL_LIBRARY'] = "C:\\Python36\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Python36\\tcl\\tk8.6"
base = 'Win32GUI' if sys.platform == 'win32' else None
includes = []
include_files = ["C:\\Python36\\DLLs\\tcl86t.dll",
                 "C:\\Python36\\DLLs\\tk86t.dll"]
# Dependencies are automatically detected, but it might need
# fine tuning.
# buildOptions = dict(packages = [], excludes = [])

# base = 'Console'

executables = [
    Executable('E:\\atom\\mytool\\fanyi.py', base=base, targetName='123.exe')
]

setup(name='123',
      version='1.0',
      description='fanyi ruanjian',
      options={"build_exe": {"includes": includes, "include_files": include_files}},
      executables=executables)

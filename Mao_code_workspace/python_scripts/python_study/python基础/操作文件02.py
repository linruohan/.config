import os
class FileWatcher(object):

    def __init__(self):
        super(FileWatcher, self).__init__()

    def watcher(self, text):
        relpaths = []#绝对路径
        path = os.path.relpath('./')#相对路径
        self.__find(path, relpaths, text)
        return relpaths

    def __find(self, path, relpaths, text):
        for p in os.listdir(path):
            if os.path.isfile(os.path.join(path, p)):
                if p.find(text) != -1:
                    relpaths.append(os.path.join(path, p))
            else:
                self.__find(os.path.join(path, p), relpaths, text)

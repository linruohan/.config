import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import os
import shutil

subdir = "/7"
homedir = os.getcwd() + subdir
import os

def walk_dir(dir, fileinfo, topdown=True):
    for root, dirs, files in os.walk(dir, topdown):
        for name in files:
            print(os.path.join(name))
            fileinfo.write(os.path.join(root, name) + '\n')
        for name in dirs:
            print(os.path.join(name))
            fileinfo.write(' ' + os.path.join(root, name) + '\n')
            fileinfo = open(homedir + '/list.txt', 'w')
            walk_dir(homedir, fileinfo)

f = open(homedir + "/list.txt", "r")
while True:
    for i in range(1, 101):
        line = f.readline()
        if line:
            line = line.strip()
            plt.subplot(10, 10, i)
            lena = mpimg.imread(line)
            plt.imshow(lena, cmap='gray')
            plt.axis('off')
        else:
            break

plt.show()
# for line in f:
# #pass # do something here
# line=line.strip()
# print(line)
# lena = mpimg.imread(line)


f.close()
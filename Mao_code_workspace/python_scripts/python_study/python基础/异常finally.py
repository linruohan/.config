#coding=utf-8
import time


try:
    f=open('D:/Python/pdf/poem.txt')
    while True:
        line=f.readline()
        if len(line)==0:
            break
        time.sleep(2)
        print (line),
finally:
    print('Cleaning up ....closed the file')

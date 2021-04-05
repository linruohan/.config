# -*- coding:utf-8 -*-
import mammoth,os
from win32com import client as wc

def all_path(path):
    result = []
    for maindir, subdir, file_name_list in os.walk(path):
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)
            result.append(apath)
    print(result)
    # print(len(result))
    return result
def chuli(docName):
    filename=docName.split('.')[0]+'.rtf'
    word = wc.Dispatch ('Word.Application')
    doc = word.Documents.Open (docName)
    doc.SaveAs (filename, 6)  # 17对应于下表中的pdf文件
    doc.Close ()
    word.Quit ()
    print('已处理：%s'%filename)
if __name__ == '__main__':
    # chuli()
    path='E:\\003'
    names=all_path(path)
    for i in names:
        chuli(i)
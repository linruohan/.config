# -*- coding:utf-8 -*-
import mammoth
import os

# docName = 'E:\\s\\1\\appium - 副本.doc'
# 将word文档从docx转换为简单、干净的html和标记

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
    filename = docName.split('.')[0]+'.rtf'
    with open(docName, "rb") as docx_file:
        style_map = """ 
        p[style-name='Section Title'] => h1:fresh 
        p[style-name='Subsection Title'] => h2:fresh 
        """
        result = mammoth.convert_to_html(docx_file, style_map=style_map)
        html = result.value  # The generated HTML
        html = " "+html + ""
        print(html)
        list = [u'\xa0', u'\xa5', u'\xa8', u'\xa9', u'\xbb', u'\u2666', u'\u200b',
                u'\u2022', u'\U0001f4a1', u'\xf8', u'\xd8', u'\xc9', u'\xab', u'\u201e',
                u'\xe5', u'\u20ac', u'\xe4', u'\xe6', u'\xdc', u'\xf6', u'\xc5', u'\u0131',
                u'\u011f']
        for i in list:
            html = html.replace(i, '')
        messages = result.messages
        fs = open(filename, 'w')
        fs.write("%s" % html)
        fs.close()
        print('已处理：%s' % filename)


if __name__ == '__main__':
    path = 'E:\\003'
    names = all_path(path)
    for i in names:
        chuli(i)

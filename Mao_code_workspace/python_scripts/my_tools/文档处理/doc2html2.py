# -*- coding:utf-8 -*-
import mammoth
import os

# docName = 'E:\\s\\1\\appium - 副本.doc'


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
    filename = docName.split('.')[0]+'.html'
    with open(docName, "rb") as docx_file:
        style_map = """ 
        p[style-name='Section Title'] => h1:fresh 
        p[style-name='Subsection Title'] => h2:fresh 
        """
        result = mammoth.convert_to_html(docx_file, style_map=style_map)
        html = result.value  # The generated HTML
        html = " "+html + ""
        print(html)

        messages = result.messages
        fs = open(filename, 'w', encoding='utf-8')
        fs.write("%s" % html)
        fs.close()
        print('已处理：%s' % filename)


if __name__ == '__main__':
    path = 'E:\\s1'
    names = all_path(path)
    for i in names:
        chuli(i)

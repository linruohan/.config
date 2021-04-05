# coding=utf-8
from lxml import etree


class Parse_html_element():
    def __init__(self, path):
        self.path = path
        self.chuli()

    # 字典中有特定的key
    def has_attr(self, dic1, str):
        list = [k for k, v in dic1.items() if str in k]
        if len(list): return True
        return False

    # 字典value中有中文

    def chinese_contain(self, str1):
        for i in list(str1):
            if u'\u4e00' <= i <= u'\u9fff':
                return True
        return False

    def chuli(self):
        with open(self.path, 'r', encoding='utf-8')as f:
            doc = f.read()
            # print(doc)

        data = {}
        html = doc.replace(u'\xa9', u'').encode('utf-8', 'ignore')
        html = doc.replace(u'\xa0', u'').encode('utf-8', 'ignore')
        page = etree.HTML(html)
        htree = etree.ElementTree(page)
        n = 0
        for t in page.iter():
            attr = t.attrib
            text = t.text
            xpath = htree.getpath(t)
            discription = ''
            dic = dict(attr)
            # print(dic.keys())
            key = [k for k, v in dic.items() if self.chinese_contain(v)]

            if text and self.chinese_contain(text[:10]):
                discription = text[:10]
            elif len(key):
                discription = dic[key[0]]
            elif self.has_attr(dic, 'name'):
                discription = dic['name']
            elif self.has_attr(dic, 'value'):
                discription = dic['value']
            # elif self.has_attr(dic, 'id'):
            #     discription = dic['id']
            elif self.has_attr(dic, 'class'):
                discription = dic['class']
            else:
                discription = ''
            data[n] = {'discription': discription, 'key': key, 'attr': dict(attr), 'xpath': xpath, 'text': text}
            n += 1
        m = 0
        for k, v in data.items():
            if v['discription']:
                m += 1
                name = (v['discription']).strip()
                xpath = v['xpath'].strip()
                element = 'xpath=>%s' % xpath.strip()
                # print(name, xpath, element)
                data = str(m) + ':\n' + name + element + '\n'
                newfile = self.path.split('.')[0] + '.txt'
                with open(newfile, 'a',encoding='utf-8') as f:
                    f.write(data)
        print('成功将element写入%s文件！'%newfile)


if __name__ == '__main__':
    path = 'html\\cross\\卡口设备\\08第一条道路下卡口设备添加.html'
    Parse_html_element(path)

from lxml import etree
class s():
    def __init__(self,path):
        self.path=path
        self.chuli()
    def chuli(self):
        with open (self.path, 'r', encoding='utf-8')as f:
            doc = f.read ()
        data = {}
        html = doc.replace (u'\xa9', u'').encode ('utf-8', 'ignore')
        html = doc.replace (u'\xa0', u'').encode ('utf-8', 'ignore')
        page = etree.HTML (html)
        htree = etree.ElementTree (page)
        print ('*' * 100)
        n = 0
        # # 依次打印出hdoc每个元素的文本内容和xpath路径
        for t in page.iter ():
            attr = t.attrib
            text = str(t.text).strip()
            xpath = htree.getpath (t)
            # print('attr==',attr)
            # print('text==',text)
            print('xpath=>%s'%xpath)
            n+=1
        print(n)
if __name__=='__main__':
    s('卡口设备状态.html')
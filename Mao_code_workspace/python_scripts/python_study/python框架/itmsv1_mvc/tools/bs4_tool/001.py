from bs4 import BeautifulSoup as bs
doc = '''
<html>
    <head>
        <title>The Dormouse's story </title>
    </head> 
    <body> 
        <p id="p1">p1p1p1
            <b id='b1'>b1b1b1</b>
        </p> 
        <p id="p2">p2p2p2</p>
        <div id='d1'>
            <ul id='u1'>u1u1u1</ul>
            <a id="a1">a1a1a1</a>
            <div id='d2'>
                <a id="a2">a2a2a2 </a>
                <b id='b2'>b2b2b2</b>
                <p id='p3'>p3p3p3</p>
            </div>
            <a id="a3">a3a3a3 </a>
        </div> 
        <p id="p4">p4p4p4</p>
    </body>
</html>
'''

def dropAllNextEle(eleOfBS, returnTrueOrFalseToKeepOrDropEleFunc=None):
    # 删除ele元素之后的所有节点元素(其实就是递归删除eleOfBS及由近及远历代父元素的兄弟元素);第二个参数是个函数,以第一个参数的各级兄弟元素为参数,返回true,保留ele,否则删除ele.
    if eleOfBS is None: return
    if eleOfBS.name == 'body': return
    next_siblings = eleOfBS.next_siblings
    if next_siblings:
        next_siblings_list = []
        for item in next_siblings:
            if item:
                next_siblings_list.insert (0, item)

        for item in next_siblings_list:
            if returnTrueOrFalseToKeepOrDropEleFunc:
                if not returnTrueOrFalseToKeepOrDropEleFunc (item):
                    item.replace_with ('')
            else:
                item.replace_with ('')

        dropAllNextEle (eleOfBS.parent, returnTrueOrFalseToKeepOrDropEleFunc)
    else:
        dropAllNextEle (eleOfBS.parent, returnTrueOrFalseToKeepOrDropEleFunc)


soup = bs (doc, 'html5lib')
a1_ele = soup.find ('a', id='a1')
dropAllNextEle (a1_ele, lambda item: type (item) == type (soup.new_string ('strstr')))
print(soup)
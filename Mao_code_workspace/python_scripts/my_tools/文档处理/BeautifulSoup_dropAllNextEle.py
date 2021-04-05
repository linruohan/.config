from bs4 import BeautifulSoup as bs


# bs处理html中,删除所有的后面的元素

def drop_all_next_ele(ele_of_bs, return_true_or_false_to_keep_or_drop_ele_func=None):
    # 删除ele元素之后的所有节点元素(其实就是递归删除eleOfBS及由近及远历代父元素的兄弟元素);第二个参数是个函数,以第一个参数的各级兄弟元素为参数,返回true,保留ele,否则删除ele.
    if ele_of_bs is None:
        return
    if ele_of_bs.name == 'body':
        return
    next_siblings = ele_of_bs.next_siblings
    if next_siblings:
        next_siblings_list = []
        for item in next_siblings:
            if item:
                next_siblings_list.insert(0, item)

        for item in next_siblings_list:
            if return_true_or_false_to_keep_or_drop_ele_func:
                if not return_true_or_false_to_keep_or_drop_ele_func(item):
                    item.replace_with('')
            else:
                item.replace_with('')

        drop_all_next_ele(ele_of_bs.parent, return_true_or_false_to_keep_or_drop_ele_func)
    else:
        drop_all_next_ele(ele_of_bs.parent, return_true_or_false_to_keep_or_drop_ele_func)


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
soup = bs(doc, 'html5lib')
a1_ele = soup.find('a', id='a1')
print(a1_ele)
drop_all_next_ele(a1_ele, lambda item: type(item) ==
                                       type(soup.new_string('strstr')))
print(soup)

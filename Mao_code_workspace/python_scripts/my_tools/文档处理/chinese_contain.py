# 判断字典dict的key和value中字符串中师傅包含汉字
def chinese_contain(dic1):
    for k, v in dic1.items():
        for i in k:
            if u'\u4e00' <= i <= u'\u9fff':
                return k
        for j in v:
            if u'\u4e00' <= j <= u'\u9fff':
                return v
    return False


if __name__ == '__main__':
    dic = {'type': 'submit', 'value': '登 录', 'class': 'btn btn-info'}
    dic2 = {'小寒': 'reset', 'value': '重 置', 'class': 'btn', 'onclick': 'reset()',
            'style': 'margin-left:20px;border:1px solid #ccc;'}

    s = chinese_contain(dic)
    s1 = chinese_contain(dic2)
    print(s)
    print(s1)

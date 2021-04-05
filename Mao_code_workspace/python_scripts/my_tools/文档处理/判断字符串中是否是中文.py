# coding=utf-8

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def chinese_contain(str1):
    for i in str1:
        if u'\u4e00' <= i <= u'\u9fff':
            return True
    return False


if __name__ == '__main__':
    print(chinese_contain('小寒'))
    print(chinese_contain('小寒shi'))
    print(chinese_contain('shi小寒'))
    print(chinese_contain('xiaohan'))

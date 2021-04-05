#!/usr/bin/env python
# -*- coding:utf-8 -*-
__version__ = '0.9'
__all__ = ["PinYin2HanZi"]

import os.path


class PinYin2HanZi (object):
    def __init__(self, dict_file='word.data'):
        self.word_dict = {}
        self.dict_file = dict_file

    def load_word(self):
        if not os.path.exists (self.dict_file):
            raise IOError ("NotFoundFile")

        with open (self.dict_file) as f_obj:
            for f_line in f_obj.readlines ():
                try:
                    line = f_line.split ('    ')
                    self.word_dict[line[0]] = line[1]
                except:
                    line = f_line.split ('   ')
                    self.word_dict[line[0]] = line[1]

    # 修改后的hanzi2pinyin函数可以避免中英文混合的情况下,英文丢失.
    def hanzi2pinyin(self, string=""):
        result = []
        if not isinstance (string, str):
            string = string.decode ("utf-8")
        for char in string:
            key = '%X' % ord (char)
            if not self.word_dict.get (key):
                result.append (char)
            else:
                result.append (self.word_dict.get (key, char).split ()[0][:-1].lower ())
        return result

    # 修改后的hanzi2pinyin_split函数 (不论split参数是否为空, hanzi2pinyin_split均返回字符串):
    def hanzi2pinyin_split(self, string="", split=""):
        result = self.hanzi2pinyin (string=string)
        # if split == "":
        #    return result
        # else:
        return split.join (result)


if __name__ == "__main__":
    test = PinYin2HanZi ()
    test.load_word ()
    string = "钓鱼岛是中国的ewerw"
    print ("in: %s" % string)
    print ("out: %s" % str (test.hanzi2pinyin (string=string)))
    print ("out: %s" % test.hanzi2pinyin_split (string=string, split=" "))

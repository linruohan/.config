# /usr/bin/env python3
# coding=utf-8
import os.path as path
import jieba
import unicode_tool

pwd_dir = path.dirname(__file__)
pa_dir = path.abspath(path.join(pwd_dir, '..'))


class Pinyin:
    def __init__(self, sentence):
        self.sentence=sentence
        self.pydict = {}
        self.dict_path = pwd_dir + '/dict/jieba_zh_pinyin.txt'
        self.jieba_dict_path = pwd_dir + '/dict/jieba_dict.txt'
        self.load()

    def __str__(self):
        return self.get_pinyin(self.sentence)

    def load(self):
        """加载和同步jieba分词的用户字典"""
        jieba.set_dictionary(self.jieba_dict_path)
        jieba.initialize()  # 手动初始化触发词典的加载
        with open(self.dict_path, encoding='utf-8') as f:
            for line in f.readlines():
                zh_str, pinyin_str, freq = line.strip().split('\t')  # 中文/拼音/使用频率
                self.pydict[zh_str] = [pinyin_str, freq]

    def get_pinyin(self, sentence):
        sentence = unicode_tool.uniform(sentence)
        segs = jieba.cut(sentence)
        pyInfoList = []  # 所有记录
        for seg in segs:
            if unicode_tool.is_chinese(seg[0]):
                if seg in self.pydict:
                    pyInfoList.append(self.pydict[seg])
            elif unicode_tool.is_number(seg):
                pyInfoList.append([chr(int(seg)), 1])
            else:
                pyInfoList.append([seg, 1])
        results = []
        for i in range(len(pyInfoList)):
            results.append([' ' + pyInfoList[i][0], pyInfoList[i][1]])
        return str(''.join(i[0] for i in results)).strip()


if __name__ == '__main__':
    sentence='wo今天要抢红米，重庆是个好地方，我热爱江西'
    sentence1='我是中国人，我热爱我的祖国，遇到重大事情，请报告组织'
    s=Pinyin(sentence1)
    print(s)
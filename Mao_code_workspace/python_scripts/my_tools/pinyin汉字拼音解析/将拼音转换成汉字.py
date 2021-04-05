def pinyin_2_hanzi(pinyinList):
    from Pinyin2Hanzi import DefaultDagParams
    from Pinyin2Hanzi import dag

    dagParams = DefaultDagParams()
    # 10个候选值
    result = dag(dagParams, pinyinList, path_num=10, log=True)
    for item in result:
        socre = item.score # 得分
        res = item.path # 转换结果
        print(socre, res)

if __name__ == '__main__':
    lists = ['wu', 'you', 'yi', 'zhi', 'xiao', 'mao', 'lv']
    pinyin_2_hanzi(lists)
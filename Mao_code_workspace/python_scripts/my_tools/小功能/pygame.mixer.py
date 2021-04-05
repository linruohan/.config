# coding=utf-8
import pygame
from Mypinyin import Pinyin


def chinese2pinyin(zh_str):
    dic = {}
    pinyin = ''
    with open('./dict/zh_pinyin_unicode.txt') as f:
        for i in f.readlines():
            dic[i.split()[0]] = i.split()[1]
    for i in zh_str:
        i = str(i.encode('unicode_escape'))[-5:-1].upper()
        try:
            pinyin += dic[i]+' '
        except:
            pinyin += 'xxxxx'  # 非法字符
    print(u'【%s】汉字转为拼音为：%s' % (zh_str, pinyin))
    return pinyin


def changeup2lower():
    with open('./dict/zh_pinyin_unicode.txt') as f:
        with open('./dict/zh_pinyin_unicode_lower.txt', 'w') as f1:
            for line in f.readlines():
                old = line.split(maxsplit=1)[1]
                new = old.lower()
                f1.write(line.replace(old, new))



def make_voice(x):
    pygame.mixer.init()  # 初始化混音器模块
    voi = chinese2pinyin(x).split(maxsplit=1)
    for i in voi:
        if i == 'xxxxx':
            continue
        pygame.mixer.music.load('./voice/'+'阿里山龙胆'+'.wav')
        pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        pass
        # pygame.mixer.stop()
       # pygame.mixer.quit()


if __name__ == '__main__':
    p = u'厦门'
    # make_voice(p)


'''
pygame.mixer.init  —  初始化混音器模块
pygame.mixer.pre_init  —  预设混音器初始化参数
pygame.mixer.quit  —  卸载混音器模块
pygame.mixer.get_init  —  测试混音器是否初始化
pygame.mixer.stop  —  停止播放所有通道
pygame.mixer.pause  —  暂停播放所有通道
pygame.mixer.unpause  —  恢复播放
pygame.mixer.fadeout  —  淡出停止
pygame.mixer.set_num_channels  —  设置播放频道的总数
pygame.mixer.get_num_channels  —  获取播放频道的总数
pygame.mixer.set_reserved  —  预留频道自动使用
pygame.mixer.find_channel   —  找到一个未使用的频道
pygame.mixer.get_busy  —  测试混音器是否正在使用
'''

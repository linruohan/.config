# *_*coding:utf-8 *_*
__Author__ = 'xiaohan'
import pyttsx3


class Speek:
    def __init__(self):
        self.engine = pyttsx3.init()  # 初始化
        self.engine.setProperty('rate', self.engine.getProperty('rate') - 50)
        self.engine.setProperty(
            'volume', self.engine.getProperty('volume') + 0.25)

    def say(self, word):
        self.engine.say(word)
        self.engine.runAndWait()

    def readfile(self, filepath):
        """朗读文本"""
        with open(filepath, 'r', encoding='utf-8') as f:
            line = f.read()  # 文件不大，一次性读取
            self.engine.say(line)
            self.engine.runAndWait()


if __name__ == '__main__':
    v = Speek()
    v.say('君不见，高堂明镜悲白发，朝如青丝暮成雪。')
    v.readfile('test.txt')

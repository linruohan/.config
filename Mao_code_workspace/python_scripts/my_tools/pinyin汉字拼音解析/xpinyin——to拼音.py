import faker
from xpinyin import Pinyin

init = faker.Faker (locale='zh-cn')
pinyin = Pinyin ()

for i in range (10):
    name = init.name ()
    print (name, '\t', pinyin.get_pinyin (name, show_tone_marks=True))
    print (name, '\t', pinyin.get_pinyin (name, show_tone_marks=True, splitter=' '))



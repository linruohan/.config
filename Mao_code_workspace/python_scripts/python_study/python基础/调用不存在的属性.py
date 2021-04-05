# class Student(object):
#
#     def __init__(self):
#         self.name = 'Michael'
#
#     def __getattr__(self, attr):
#         if attr=='score':
#             return 99
#
#
# s=Student()
# print(s.name)
# print(s.score)


class Chain(object):

    def __init__(self, path=''):
        super(Chain, self).__init__()
        self.__path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self.__path, path))

    def __str__(self):
        return self.__path

    def __call__(self, value):
        return Chain('%s/%s' % (self.__path, value))

m=Chain()
print(m.path)
print(m.path.s.m)
print(Chain().users('xiaohan').repos)

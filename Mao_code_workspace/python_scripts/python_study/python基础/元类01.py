'''
type()函数既可以返回一个对象的类型，又可以创建出新的类型，
比如，我们可以通过type()函数创建出Hello类，而无需通过
class Hello(object)...的定义：
'''
def fn(self,name='World'):
    print('hello,%s.' %name)



Hello = type('Hello', (object,), dict(hello=fn))

h=Hello()
h.hello()
print(type(Hello))
print(type(h))

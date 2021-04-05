class MyClass:
    def __init__(self):
        self.key='123'
    def a(self):
        self.key=2
        return self.key
    def b(self):
        self.a()
        print(self.key)

s=MyClass()
s.b()

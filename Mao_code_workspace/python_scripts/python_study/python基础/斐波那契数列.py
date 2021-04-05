# 斐波那契数列
class Fib(object):
    """docstring for Fib."""
    def __init__(self):
        self.b,self.a = 0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.b>1000:
            raise StopIteration()
        return self.b
    def __getitem__(self,n):
        if isinstance(n,int):# n是索引
            a,b,=0,1
            for x in range(n):
                a,b=b,a+b
            return b
        if isinstance(n,slice):# n是切片
            start=n.start
            stop=n.stop
            if start is None:
                start=0
            a,b=0,1
            L=[]
            for x in range(stop):
                if x>start:
                    L.append(a)
                a,b=b,a+b
            return L



m=Fib()[:10]
print(m)

s=list(Fib())[0:12]
print(s)

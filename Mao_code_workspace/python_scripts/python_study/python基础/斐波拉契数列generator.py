def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    print('end')


for i in fib(9):
    print(i)

f=fib(2)
print(f)
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

o=odd()
next(o)
next(o)
next(o)

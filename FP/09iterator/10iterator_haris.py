def foo(a: list, size:int) -> list:
    yield a[:size]
    yield a[:size]

a = [1,2,3,4]



for i in iter(foo(a,2)):
    print(i)

for i in iter(a):
    print(i)


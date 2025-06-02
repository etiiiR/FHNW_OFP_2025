def simple_function(a):
    def line(b=0):
        def compute(x):
            return [a + (b * xi) for xi in x]
        return compute
    return line

a = simple_function(10)
print(a)
b = a()
print(b)
c = b([1,2])
print(c)



def curry(num):
    def add(num2):
        def add2(num3):
            return num * num2 * num3
        return add2
    return add

var1 = curry(5)
print(type(var1))

var2 = var1(7)
result = var2(1)
print(result)

def curry(num):
    def add(num2):
        return num * num2
    return add

times = curry(7)
result = times(5)
print(result)


def curry():
    def times(num1, num2):
        return num1 * num2
    return times

times = curry()
result = times(5,7)
print(result)
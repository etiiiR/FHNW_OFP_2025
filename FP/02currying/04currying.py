def add_three_numbers(x, y, z):
    return x + y + z

def subtract_two_numbers(x, y):
    return x - y

def curry(func, first):
    def call_func(*args):
        return func(first, *args)
    return call_func


add_to_10 = curry(add_three_numbers, 10)
add_to_10(4, 2)
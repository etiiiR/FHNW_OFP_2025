# Currying - Man versucht Funktionen mit vielen Paramatern kleiner zu machen, dass weniger Parameter fuer eine Funktion
# Benoetigt wird.

def summe(x):
    def f(a,b):
        return x + a + b
    return f

foo = summe(2)
print(foo(4,5))






# ax + ax^2 + ax^3

def multiply(x):
    def factora(a):
        return (a*x + a*x**2 + a*x**3)
    return factora

faca = multiply(5)
result = faca(2)

print(result)


def add_first(a:int):
    def add_second(b:int):
        def add_third(c:int):
            return a + b + c
        return add_third
    return add_second

first_num = add_first(10)
second_num = first_num(20)
result = second_num(30)
print(result)

print(len(first_num.__closure__))
print(first_num.__closure__[0].cell_contents)
liste = [second_num.__closure__[x].cell_contents for x in range(len(second_num.__closure__))]

print(liste)
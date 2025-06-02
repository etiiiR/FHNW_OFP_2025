# Iteratoren geben

liste = [40,30,20,10]
iterator = liste.__iter__()
# print(iterator)
# output: <list_iterator object at 0x000002C159C0EFD0>

# print(next(iterator))
# output: 40
# print(iterator.__next__())
# output: 30

# Beide Varianten sind das gleiche!

liste2 = [1,2,3,4]
for i in iter(liste2):
    print(i)

# Analog zu
for i in liste2:
    print(i)


"""
Sehr aehnlich wie List Comprehension. Statt [] nimmt man ()

"""
# bsp:

import itertools

# generator erstellen
squares = (x ** 2 for x in itertools.count(1))

print(type(squares))
# Ist ein generator!

for x in squares:
    print(x)
    if x > 50:
        squares.close()
        # .close() ist eine Methode speziell fuer Generators
        # Alternativ break

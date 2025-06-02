# Modul importieren
import itertools

# itertools.cycle(iter) iteriert unendlich lange im Kreis

l = [1,2,3,4,5]
it = l.__iter__()

elements = []
for x in itertools.cycle(it):
    elements.append(x)
    # print(x) # 1, 2, 3, 4, 5, 1, 2, 3, ..........
    if len(elements) == 14:
        break

print(elements)

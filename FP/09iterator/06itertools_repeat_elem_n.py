# Modul importieren
import itertools

# itertools.repeat(element, n) => Element kann ein int, str, list etc.. sein
# mit n ist die Anzahl wiederholungen des Elementes gemeint.

it = itertools.repeat("100").__iter__() # Unendlich langer Iterator der nur 100 zurueckgibt.

cnt = 0
for x in it:
    cnt += 1
    if cnt == 4:
        break
    print(x)


it2 = itertools.repeat("ABC", 5).__iter__() # Endlich langer Iterator der sich 5x wiederholt
cnt = 0
for x in it2:
    if cnt == 10:
        break
    print(x)
    cnt += 1
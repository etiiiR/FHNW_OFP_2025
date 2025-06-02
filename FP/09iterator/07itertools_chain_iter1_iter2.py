# modul importieren
import itertools

# itertools.chain(iterator1, iterator2)
# gibt mir zuerst alle endlichen Werte aus Iterator 1 und anschliessend alle aus Iterator 2

it1 = [1,2,3].__iter__()
it2 = ("a","b").__iter__()

for x in itertools.chain(it1, it2):
    print(x)

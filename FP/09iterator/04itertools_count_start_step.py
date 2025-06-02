import itertools

# Um einen unendlich langen Iterator zu bauen, benoetigen wir das Modul itertools.
# itertools.count(start, step) wird mit verschiedenen Parameter gezeigt.

print("Teil 1")
# itertools.count() ist ein unendlich langer Iterator Objekt der von 0 Startet
for x in itertools.count():
    print(x) # 1, 2, 3, ...........
    if x == 2:
        break

print("Teil 2")
# itertools.count(5) ist ein unendlich langer Itertator Objekt der von 5 Startet!
for x in itertools.count(5):
    print(x) # 5, 6, 7, ..........
    if x == 7:
        break

print("Teil 3")
# itertool.count(10, 5) ist ein unendlich langer Iterator Objekt der von 5 Startet in 10er Schritten!
for x in itertools.count(10,5):
    print(x) # 10, 15, 20, .........
    if x == 20:
        break
"""
Generator vs Iterator
Generator => Funktioniert wie ein Iterator
Generator => Generiert die Elemente in einer Schleife
Generator => "Auf Nachfrage" ein Iterator

Iterator => Loop ueber ein Objekt im Speicher
"""

def f():
    return 1
    return 2
    return 3

print(f())
# Sobald die Funktion ein Return macht, ist der Job beendet.

def g():
    yield 1
    yield 2
    yield 3

print(g())
# gibt mir einen Genrator Objekt zurueck.
# Weil der Generator ein Typ eines Iterator ist,
# koennen wir darueber loopen.

for x in g():
    print(x)


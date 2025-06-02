# Generator ist eine Implementierung des Iteratrs
# Generator ist eine Funktion der einen Iterator zurueckgibt, und der Iterator gibt den Wert zurueck.

x = [10,20,304,503]

def fun(liste):
    for x in liste:
        yield x

a = fun(x)
print(a)

# gibt mit das naechste Elemente zurueck
#print(a.__next__())

# Weil das erste Element schon zurueck gegeben wurde, werden nur die letzten 3 Elemente ausgegeben
for i in a:
    print(i)






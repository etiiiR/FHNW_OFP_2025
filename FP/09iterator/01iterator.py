# Ein Iterator ist ein Objekt, dass ein Datenstrom darstellt
# Ein Iterator Objekt gibt ein Element nach dem anderen zurueck bis keine mehr vorhanden sind.
# Ein Iterator Objekt kann endlich oder unendlich lang sein
# Ein Iterator Objekt kann nur die naechsten Werte ausgeben, aber nicht die vorherigen!

t = [10,20,304,50]
it = t.__iter__()
print(it) # Iterator Objekt

print(it.__next__()) # 10
print(it.__next__()) # 20
print(it.__next__()) # 304
print(it.__next__()) # 50
print(it.__next__()) # Out of 






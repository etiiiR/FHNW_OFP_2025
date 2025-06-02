import itertools

# Funktion definieren
def prime_numbers():
    # Umgang mit der ersten Primzahl
    yield 2
    prime_chache = [2] # Speicherung der Primzahlen

    # Loopen ueber positive, gerade Zahlen
    for n in itertools.count(3, 2):
        # itertools.count(3, 2) => Startwert = 3, Increment Schritt = 2, -> 3,5,7 etc....
        is_prime = True # Auf True gesetzt (Schranken - Ampelsystem)

        # Checken, ob n teilbar durch primzahl ist
        for p in prime_chache:
            if n % p == 0: # Zahl n dividert durch primzahl ergibt 0 -> Kein Rest
                is_prime = False # Schranke zu machen, da teilbar und somit kein Primzahl!
                break
        # ist es ein Prime?
        if is_prime: # Ist True
            prime_chache.append(n) # Wird dem prime_chache hinzugefuegt
            yield n # Primzahl wird ausgegeben

# Loopen ueber primzahlen nummer:
for num in prime_numbers():
    print(num)
    if num > 100:
        break


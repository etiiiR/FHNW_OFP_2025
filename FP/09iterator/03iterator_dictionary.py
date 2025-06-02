# Dictionary unterstuetzt den Iterator
L = [('Italy', 'Rome'), ('France', 'Paris'), ('US', 'Washington DC')]

iter = dict(iter(L))

# Variante 1
for key in iter:
    print(key, iter[key])

# Variante 2
for key, value in iter.items():
    print(key, value)



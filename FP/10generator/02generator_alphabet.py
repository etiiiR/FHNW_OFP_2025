import string

# generiere buchstaben des alphabet
def letters():
    for c in string.ascii_lowercase:
        yield c

# Gibt uns einen Generator zueruck,
# darueber koennen wir loopen
print(letters())

for x in letters():
    print(x)


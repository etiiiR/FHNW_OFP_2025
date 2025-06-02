import itertools

# itertools.tee(Iterator, n)
# duppliziert mir den Iterator n-male.

iterA = [10,20,30].__iter__()
print(iterA)

for x in itertools.tee(iterA, 2):
    for y in x:
        print(y)


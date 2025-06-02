# modul importieren
import itertools

# itertools.islice(iter, [start], stop, [step])
# Unendlicher/Endlicher Iterator den man selbst definieren kann, wo er stoppen sollte und mit welchen
# schrittgroessen

for x in itertools.islice(range(10), 2, 12, 3):
    print(x)


def adder(i, *args):
    print(type(args))
    print(type(i))
    sum = 0
    for n in args:
        sum += n
    print("Summe ist:", sum)


adder(3,2,5,2,4,1,2,45,1,1,1,2,4,12,2,41,1,124,21,43)
adder(2,5,3,3,5,3)

# *args sind spezielle keyword Argumente fuer Funktionen
# *args Argumente werden in Form von **Tupple** weiter gegeben
# *args Argumente koennen beliebige lang sein
# *args Argumente machen die Funktion flexibler
def intro(**kwargs):
    print(type(kwargs))

    for key, value in kwargs.items():
        print(key, type(key), value, type(value))

intro(Firstname = "Ben", Lastname="Tran")
intro(Modul="ofp", Semester=2, Jahr=2022, Schule="FHNW")

# **kwargs sind spezielle keyword Argumente fuer Funktionen
# **kwargs Argumente werden in Form von **Dictionary** weiter gegeben
# **kwargs Argumente koennen beliebige lang sein
# **kwargs Argumente machen die Funktion flexibler
# **kwargs kann ich als Variabel betrachten. (Variabel = key, Wert = Value)

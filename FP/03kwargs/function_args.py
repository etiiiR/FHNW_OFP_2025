def f(x, *args):
    args[0] # *args verpackt alle weitere Parameter in ein Tuppel  # Hier habe ich eine Sequenz von Werten



def g(x, **args): # **args = Key words Arguments bsp: a = 5, b = 4, c = 2 # Diese wird als Dictionary verpackt

def start():
    dane = "x, y"
    x = 1
    y = 2
    zmienne(dane)
def zmienne(dane):
    x = x + 1
    y = x + y
    dalej(dane)
    
def dalej(dane):
    x = x + 1
    print x
    print y
    

start()

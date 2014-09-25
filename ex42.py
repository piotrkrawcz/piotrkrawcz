import os
os.system('clear')



class Zwierze():

    def __init__(self, waga, dl_zycia, predkosc):
        
        self.waga = waga
        self.dl_zycia = dl_zycia
        self.predkosc = predkosc

        
class Pies(Zwierze):

    def dane(self):
        print "to jest klasa pieska\n"
        if self.waga > 10:
            print "piesek jest ciezki"
        if self.predkosc < 5 and self.waga >10:
            print "spasione bydle"
        
                
        print self.waga, self.dl_zycia, self.predkosc    
    

class Kot(Zwierze):
    def dane(self):
        print "kotek wazy %s, zyje %s lat, zapierdala %d " % (self.waga, self.dl_zycia, self.predkosc)
        
burek = Pies(14,5,2)
filemon = Kot (200, 150, 5)  

burek.dane()
filemon.dane()

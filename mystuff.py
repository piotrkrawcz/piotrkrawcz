import os
os.system('clear')

class Piosenka(object):
    
    def __init__(self, lyrics):
        self.lyrics = lyrics
        
    def naqrwiaj(self):
        for x in self.lyrics:
            print x
            
            
wiadro = [" oa pierdole"]

ochuju2 = Piosenka(wiadro)



ochuju2.naqrwiaj()



from sys import exit

def start():
    imie = raw_input("Podaj swoje imie: > ")
    zmijosalawybita = False
    zagadkawybita = False
    pajakwybita = False
    przedbosemwybita = False
    sprochnialawybita = False
    gargulecwybita = False
    swiniosalawybita = False
    przedbosemwyzbierana = 0 # po zebraniu trzech starta 5pz
    swiniawyzbierana = False
    gargulecwyzbierany = False
    lokalizacja = hall
    miecz = 0
    pz = 5

    for i in range(0,20):
        print "\n"
        i = i+1
        
    print "Podczas podrozy po Hrubieszowie straciles przytomnosc i budzisz sie nagle w bardzo ciemny korytarzu, dookola widzisz martwe ciala roznych gigantycznych insektow, robali, dziwnych swini afrykanskich itp. Mroczna wizja przyszlosci roztacza sie w otchlaniach twojego szalonego umyslu"
    print "podnosisz sie i rozgladasz wokol > ENTER"
    raw_input()
    
    hall(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie)
    
    
    
def hall(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie):
    lokalizacja = hall
     
    for i in range(0,20):
        print "\n"
        i = i+1
    print "jestes w Hallu, w miejscu ktorym sie znajdujesz widac 2 korytarze"
    print "na koncu pierwszego widac drzwi z narysowanym dziwnym wezem"
    print "na koncu drugiego prochniejace drewniane drzwi bez zadnych symboli"
    print "co robisz?"
    print "1. postac" 
    print "2. ide do drzwi z narysowanym dziwnym wezem"
    print "3. przechodze przez sprochniale drzwi"
    while True:    
        wybor = raw_input("> ")
        if wybor == "1" or wybor == "kieszen":
            kieszen(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie)
        elif wybor == "2":
            zmijosala(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie)
        elif wybor == "3":
            zagadka(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie) 
        else:
            print "wybierz 1 2 lub 3" 


def zmijosala(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie):
    lokalizacja = zmijosala
    
    for i in range(0,20):
        print "\n"
        i = i+1
    print "jestes w sali o ponurych ociekajacych woda scianach"
    print "z prawej strony drzwi do hallu, na dole drabina"
    
    if zmijosalawybita is False:
        
        print "przed Toba pelza wielki waz ktora zagradza Ci droge"
        print "do drabiny prowadzacej w dol"
        print "co robisz?"
        print "1. postac"
        print "2. atakuje bestie"
        print "3. boje sie uciekam"
        while True:
            wybor = raw_input("> ")
            
            if wybor == "1":
                kieszen(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie)
            elif wybor == "2":
                if miecz < 1:
                    print "zaatakowales piesciami zmije"
                    pz = pz - 3
                    if pz > 0:
                        print "zatlukles zmije piesciami, ale zdazyla Cie pokasac i straciles 3PZ"
                        pz = pz + 1
                        zmijosalawybita = True
                        while True:
                            print "obok Ciebie martwa bestia, co robisz?"
                            print "1. postac"
                            print "2. schodze na dol"
                            print "3. ide do hallu"
                            wybor = raw_input("> ")
                            if wybor == "1":
                                kieszen(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie)
                            elif wybor == "2":
                                pajak(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie)
                            elif wybor == "3":
                                hall(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie)
                    else:
                        smierc("zmija zagryzla Cie i umarles w meczarniach")
                    
                elif miecz > 0:
                    print "zwinnie zaatakowales podlego gada, ktory nawet sie nie bronil"
                    print "zdechl w konwulsjach, jestes z siebie dumny"
                    print "straciles miecz ale czujesz sie silniejszy"
                    zmijosalawybita = True
                    pz = pz + 1
                    miecz = miecz - 1
                    
                    while True:
                        print "obok Ciebie martwa bestia, co robisz?"
                        print "1. postac"
                        print "2. schodze na dol"
                        print "3. ide do hallu"
                        wybor = raw_input("> ")
                        if wybor == "1":
                            kieszen(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie)
                        elif wybor == "2":
                            pajak(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie)
                        elif wybor == "3":
                            hall(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie)
                            
                            
            elif wybor == "3":
                hall(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie)
            else:
                print "wybierz 1 2 lub 3"
    else:
        while True:
            print "obok Ciebie martwa bestia, co robisz?"
            print "1. postac"
            print "2. schodze na dol"
            print "3. ide do hallu"
            wybor = raw_input("> ")
            if wybor == "1":
                kieszen(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie)
            elif wybor == "2":
                print "schodzisz po drabinie na dol..."
                raw_input(" ... enter")
                pajak(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie)
            elif wybor == "3":
                hall(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie)         
            else:
                print "sprobuj wybrac poprawnie"
                
                
                                  

def zagadka(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie):
    lokalizacja = zagadka
    
    for i in range(0,20):
        print "\n"
        i = i+1
    
    if zagadkawybita is False:
        while True:
            print "znajdujesz sie w pomieszczeniu gdzie na srodku jest widoczna ogromna glowa"
            print "jest tez miejsce na polozenie dloni oraz drabina na dol"
            print "co robisz teraz?"
            print "1. ide do hallu"
            print "2. schodze na dol po drabinie"
            print "3. ta glowa jest podejrzana sprawdzam czy cos za nia sie nie znajduje"
            print "4. klade dlon w miejscu na polozenie dloni"
            print "5. postac"
            wybor = raw_input("> ")
            if wybor == "1":
                hall(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie)
            elif wybor == "2":
                sprochniala(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie)
            elif wybor == "3":
                print "postanowiles obejsc glowe, kierujesz sie od lewej strony"
                raw_input("... ")
                print "jestes za glowa czujesz mrowienie na plecach"
                raw_input("... ")
                raw_input("... ")
                print "obszedles cala glowe i nic sie nie stalo"
                raw_input("dalej... ")
            elif wybor == "5":
                kieszen(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie)
            elif wybor == "4":
                print "Nagle oczy posagu rozswietlaja sie czerwonym blaskiem"
                raw_input("dalej... ")
                print "podloga zaczyna sie delikatnie trzasc"
                raw_input("dalej... ")
                print "slyszysz slowa:"
                raw_input("dalej... ")
                print "ODPOWIESZ NA MOJE PYTANIE, ALBO BEDZIESZ CIERPIEC!"
                raw_input("dalej... ")
                print "W KTORYM ROKU MIASTO W KTORYM SIE ZNAJDUJESZ"
                print "UZYSKALO PRAWA MIEJSKIE?!"
                wybor = raw_input("> ")
                if "1400" in wybor:
                    zagadkawybita = True
                    miecz = miecz + 2
                    pz = pz + 3
                    print "DOBRZE, ODPOWIEDZ JEST PRAWIDLOWA"
                    print "OTO TWOJA NAGRODA!!"
                    raw_input("dalej... ")
                    print "otrzymujesz nowe miecze oraz dodatkowy punkty zycia"
                    raw_input("dalej... ")
                    zagadka(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie)
                    
                else:
                    print "MILCZ SUKINSYNU"
                    print "ZLA ODPOWIEDZ! TERAZ PONIESIESZ KARE"
                    print "wielka blyskawica leci w twoim kierunku"
                    raw_input("dalej... ")
                    pz = pz - 5
                    if pz < 0:
                        smierc("blyskawica cie spopielila") 
            
    elif zagadkawybita is True:
            while True:
                print "znajdujesz sie w pomieszczeniu gdzie na srodku jest widoczna ogromna glowa"
                print "jest tez miejsce na polozenie dloni oraz drabina na dol"
                print "co robisz teraz?"
                print "1. ide do hallu"
                print "2. schodze na dol po drabinie"
                print "3. ta glowa jest podejrzana sprawdzam czy cos za nia sie nie znajduje"
                print "4. klade dlon w miejscu na polozenie dloni"
                print "5. postac"
                wybor = raw_input("> ")
                if wybor == "1":
                    hall(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie)
                elif wybor == "2":
                    sprochniala(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie)
                elif wybor == "3":
                    print "postanowiles obejsc glowe, kierujesz sie od lewej strony"
                    raw_input("... ")
                    print "jestes za glowa czujesz mrowienie na plecach"
                    raw_input("... ")
                    raw_input("... ")
                    print "obszedles cala glowe i nic sie nie stalo"
                    raw_input("dalej... ")
                elif wybor == "5":
                    kieszen(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie)
                elif wybor == "4":
                    print "czujesz tylko zimny chlod kamienia nic wiecej"
                    raw_input("dalej... ")
                    

def pajak(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie):
    lokalizacja = pajak
    for i in range(0,20):
        print "\n"
        i = i+1
    print "znajdujesz sie w miejscu gdzie widzisz drabine prowadzaca do gory oraz na dol"
    print "z lewej strony widoczne sa rowniez kamienne drzwi - a koszmarny leb pseudosmoka wyrzezbiony na drzwiach" 
    if pajakwybita is False:
        print "jakby tego bylo malo ogromny pajak zmierza w Twoim kierunku"
        print "syczy jest bardzo agresywny"
        while True:
            print "co robisz?"
            print "1. atakuje bestie"
            print "2. uciekam na gore"
            wybor = raw_input("> ")
            if wybor == "1":
                if miecz < 1:
                    print "rzucasz sie z piesciami na gigantycznego pajaka"
                    raw_input(" ... ENTER") 
                    print "blyskawicznie zeby jadowe wkluwaja sie w twoja piesc"
                    print "bol jest nie dotwytrzymania"
                    raw_input(" ... ENTER") 
                    pz = pz - 3
                    if pz < 0:
                        smierc("pajak zaczyna wyzerac ci twarz po godzinnej mece odchodzisz w pokoju z ziemskiego padolu")
                    else:
                        print "wymierzasz solidnego kopniaka"
                        print "pajak odbil sie od sciany - masz szanse na ucieczke drabina do gory lub w dol"
                        print "1. uciekam drabina w gore"
                        print "2. uciekam drabina w dol"
                        print "3. jestem dzielny walcze dalej"
                        wybor = raw_input("> ")
                        if wybor == "1":
                            zmijosala(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie)
                        elif wybor == "2":
                            swiniosala(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie)
                        elif wybor == "3":
                            print "pajak juz niemalze stracil jad"
                            print "wiec rozrywasz go na strzepy, a nastepnie zadeptujesz"
                            pz = pz + 2
                            pajakwybita = True
                            print "obok Ciebie martwy pajak"
                            raw_input("...ENTER")
                            pajak(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie)
                        else:
                            print "masz opcje to wyboru postaraj sie skupic"    
                elif miecz > 0:
                    print "wymierzasz potezny cios swoim ostrzem w bestie"
                    print "ktora momentalnie pada martwa"
                    pz = pz + 2
                    pajakwybita = True
                    print "obok Ciebie martwy pajak"
                    raw_input("...ENTER")
                    pajak(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie)
            elif wybor == "2":
                zmijosala(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie)
            else:
                print "skup sie wybierz prawidlowa opcje"
                
            
            
            
        
    else:
        while True:
            print "co robisz?"
            print "1. wspinam sie po drabinie do gory"
            print "2. schodze drabina na dol"
            print "3. przechodze przez kamienne drzwi"
            print "4. postac"
            wybor = raw_input("> ")
            if wybor == "1":
                zmijosala(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie)
            elif wybor == "2":
                swiniosala(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie)
            elif wybor == "3":
                przedbosem(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie)
            elif wybor == "4":
                kieszen(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie)
            else:
                print "wybierz 1 2 3 lub 4"
                raw_input(" ... ENTER")    
                
                
      



def przedbosem(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie):
    lokalizacja = przedbosem
    for i in range(0,20):
        print "\n"
        i = i+1
    
    print "znajdujesz sie w mrocznej jak mysli kreta sali"
    print "jest tutaj bardzo goraco w oddali widac buchajace kleby ognia"
    print "na scianach widac obrazy przestawiajace walke"
    print "szewczyka dratewki ze smokiem wawelskim"
    print "obok obrazu widac rowniez blyszczaca tarcze ze"
    print "swiecacym na niebisko mieczem"
    print "korytarz prowadzi do kolejnego przejscia"
    print "nad ktorym widac napis zapisany krasnoludzkimi runami:"
    print "PIECZARA SMOKA"
    print "co robisz?"
    while True:
        print "1. wracam do pomieszczenia z pajakiem"    
        print "2. chce zbadac te tarcze i miecza"
        print "3. ruszam w kierunku smoka"
        print "4. postac"
        wybor = raw_input("> ")
        if wybor == "1":
            print "ruszasz do komnaty,w ktorej byl pajak"
            raw_input("...[enter]")
            pajak(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie)
                    
        elif wybor == "2":
            print "podchodzisz do artefaktow"
            print "blyszcza sie majestatycznie jak wypucowane porsche"
            print "poczuwasz deliaktne wyladowania elektrycznie przy mieczu"
            print "co robisz"
            while True:
                print "1. zabieram mieczyk"
                print "2. odchodze - pierdole to boje sie tych piorunow"
                wybor = raw_input("> ")
                if wybor == "1":
                    przedbosemwyzbierana = przedbosemwyzbierana + 1
                    miecz = miecz + 1
                    for i in range(0,20):
                        print "\n"
                        i = i+1
                    print "niepewnie wyciagasz reke po bron i zabierasz do ekwipunku"
                    print "co chcesz dalej zrobic?"
                    if przedbosemwyzbierana > 3:
                        print "jestes bardzo chciwy !"
                        raw_input("... slyszysz trzask ... [enter]")
                        print "wielka blyskawica leci w twoim kierunku"
                        pz = pz - 5
                        if pz < 0:
                            smierc("spopiela Cie blyskawica, koniec tej glupiej zabawy")
                
                elif wybor == "2":
                    przedbosem(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie)
                else: 
                    print "postaraj sie wybrac dobrze"
        
        elif wybor == "3":
            print "niepewnym krokiem zmierzasz na spotkanie z przeznaczeniem"
            raw_input("...")
            
        elif wybor == "4":
            kieszen(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie)
        else:
            print "sprobuj jeszcze raz"
    
    
def boss(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie):
    lokalizacja = boss
    for i in range(0,20):
        print "\n"
        i = i+1
    
def sprochniala(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie):
    lokalizacja = sprochniala
    for i in range(0,20):
        print "\n"
        i = i+1

def gargulec(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie):
    lokaliazacja = gargulec
    for i in range(0,20):
        print "\n"
        i = i+1
    
def swiniosala(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie): 
    lokalizacja = swiniosala
    for i in range(0,20):
        print "\n"
        i = i+1

def smierc(powod):
    for i in range(0,20):
        print "\n"
        i = i+1
    print powod, "KONIEC ZABAWY !!!!!"
    exit()   

def kieszen(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie):
    
    for i in range(0,20):
        print "\n"
        i = i+1    
    print "Imie              : ", imie    
    print "twoje punkty zycia: ", pz
    print "liczba mieczy     : ", miecz
    raw_input("Enter - powrot")
    
    if lokalizacja == hall:
        hall(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie)
    elif lokalizacja == zmijosala:
        zmijosala(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie)
    elif lokalizacja == zagadka:
        zagadka(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie)
    elif lokalizacja == pajak:
        pajak(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie)
    elif lokalizacja == przedbosem:
        przedbosem(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie)
    elif lokalizacja == boss:
        boss(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie)
    elif lokalizacja == sprochniala:
        sprochniala(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie)
    elif lokalziacja == gargulec:
        gargulec(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie)
    elif lokalizacja == swiniosala:
        swiniosala(zmijosalawybita, zagadkawybita, pajakwybita, przedbosemwybita, sprochnialawybita, gargulecwybita, swiniosalawybita, przedbosemwyzbierana, gargulecwyzbierany, lokalizacja, miecz, pz, imie) 

start()  


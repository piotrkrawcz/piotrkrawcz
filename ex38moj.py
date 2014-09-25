print "podaj zdanie a podziele je na slowa"
zdanie = raw_input("> ")

podzielonezdanie = zdanie.split(' ')
print "oto podzielone zdanie:"
print podzielonezdanie

dodatkowe = ['ala', 'ma', 'kota', 'kot', 'ma', 'aids']

print "ilosc wyrazow podzielonego zdania: %d " % len(podzielonezdanie)

while len(podzielonezdanie) != 10:
    przekaznik = dodatkowe.pop()
    print "dodajemy: " , przekaznik
    podzielonezdanie.append(przekaznik)

print podzielonezdanie[1]
print podzielonezdanie[-1]


class Sklep(object):
    def __init__(self):
		self.przedmioty = [
			dict(
				towar = 'Miecz',
				cena = 50,
			),
			dict(
				towar = 'MlotBojowy',
				cena = 50,
			),
			dict(
				towar = 'Topor',
				cena = 60,
			),
			dict(
				towar = 'DobryMiecz',
				cena = 200,
			),
			dict(
				towar = 'DobryMlotBojowy',
				cena = 200,
			),
			dict(
				towar = 'DobryTopor',
				cena = 220,
			),
			dict(
				towar = 'mikstura',
				cena = 75,
			),
		
		]
		self.lista_przedmiotow = []
		for index, pozycja in enumerate(self.przedmioty):
			self.lista_przedmiotow.append(index)
		
abc = Sklep()
print abc.lista_przedmiotow
for x in range(abc.lista_przedmiotow[0],abc.lista_przedmiotow[-1]):
	print 'index: %d, towar: %s, cena: %s' %(x, abc.przedmioty[x]['towar'], abc.przedmioty[x]['cena'])

print'wybierz lb od o do', abc.lista_przedmiotow[-1]	
wybor = input('> ')
print abc.przedmioty[wybor]['towar']

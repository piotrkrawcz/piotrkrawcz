class Lokacja(object):
	def __init__(self):
		self.przypadek = dict(
				mianownik = self.przypadki[0],
				dopelniacz = self.przypadki[1],
				narzednik = self.przypadki[2],
			
			)
		self.licznik_wizyt = 1
		
		self.opis1 = '%s, wizyta nr: %d' % (self.nazwa('mianownik'), self.licznik_wizyt)
		self.opis2 = '...'
		self.opis = self.opis1 + self.opis2
		
	def nazwa(self, odmiana):
		return self.przypadek[odmiana]
		
	def wejscie(self, wizytator):
		self.licznik_wizyt += 1
		print '%s, wizyta nr: %d' % (self.nazwa('mianownik'), self.licznik_wizyt)
		
class Wioska(Lokacja):
	przypadki = ['wioska','wioski','wioska']
	nr_lokacji = 0

class Silnik(object):
	# ladna nazwa lokacji powinna wynikac z metody klasy do ktorej sie odwolujemy
	lokacje = [
		Wioska(),
		Sklep(),
		Trening(),
		Las(),
		Rzeka(),
		Wieza(),
		Legowisko(),
	]	
		
	przejscia = {
		0: [1,2,3],
		1: [0,],
		2: [0,],
		3: [0,4],
		4: [0,3,5],
		5: [4,6],
	
	}	
	
	def __init__(self):
		self.wygrane_walki = 0
		
	def prezentacja_lokacji(self, nr_lokacji):
		for opcja in self.przejscia[nr_lokacji]:
			print self.lokacje[opcja].nr_lokacji, self.lokacje[opcja].nazwa('mianownik')
			
	def pobierz_lokacje(self, nr_lokacji):
		return self.lokacje[nr_lokacji]
			
	def gra(self):
		nr_lokacji = 0
		obecnalokacja = self.pobierz_lokacje(nr_lokacji)
		while obecnalokacja != self.lokacje[-1]:
			obecnalokacja.wejscie(gracz)
			while True:
				self.prezentacja_lokacji(nr_lokacji)
				wybor = int(raw_input('> '))
				if wybor in self.przejscia[nr_lokacji]:
					nr_lokacji = wybor
					break
				else:
					print 'wybierz jedna z dostepnych opcji'
			obecnalokacja = self.pobierz_lokacje(nr_lokacji)
			print obecnalokacja.opis	

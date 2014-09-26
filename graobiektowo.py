from random import randint
import os
class Postac(object):
	def statystyki(self):
		imie = "Janek"
		pz_postac = 25 + randint(1,5)
		rusznica = 0 
		dobry_miecz = 0
		if rusznica == 1:
			punkty_ataku = 40
		elif dobry_miecz == 1 and rusznica == 0:
			punkty_ataku_postac = 20
		else:
			punkty_ataku_postac = 10
		zloto = 100 + randint(0,50)
		return imie, pz_postac, punkty_ataku_postac, zloto
class Potwor(object):

	def statystyki(self):
		pz = 10
		punkty_ataku = 10
		zloto = 0
		return pz, punkty_ataku, zloto
		
class Ork(Potwor):
	
	def statystyki(self):
		pz, punkty_ataku, zloto = super(Ork,self).statystyki()
		pz = pz + randint(1,10)
		punkty_ataku = punkty_ataku + randint(1,5)
		zloto = zloto + randint(1,5)
		return pz, punkty_ataku, zloto

class Goblin(Potwor):
	
	def statystyki(self):
		pz, punkty_ataku, zloto = super(Goblin,self).statystyki()
		pz = pz + randint(1,5)
		punkty_ataku = punkty_ataku + randint(1,2)
		zloto = zloto + randint(1,2)
		return pz, punkty_ataku, zloto		

class Wilk(Potwor):
	
	def statystyki(self):
		pz, punkty_ataku, zloto = super(Wilk,self).statystyki()
		pz = pz + randint(1,10)
		punkty_ataku = punkty_ataku + randint(1,5)
		zloto = zloto + randint(1,5)
		return pz, punkty_ataku, zloto
		
class Smok(Potwor):
	
	def statystyki(self):
		pz, punkty_ataku, zloto = super(Smok,self).statystyki()
		pz = pz + randint(20,40)
		punkty_ataku = punkty_ataku + randint(10,25)
		zloto = zloto + randint(1,5)
		return pz, punkty_ataku, zloto
		
class Silnik(object):
	
	def __init__(self, mapa):
		self.mapa = mapa
	
	def gra(self):
		obecnalokacja = self.mapa.pierwsza_scena()
		
		while True:
			kolejnalokacja = obecnalokacja.wejscie()
			obecnalokacja = self.mapa.pobierz_scene(kolejnalokacja)

class Wioska(object):
	os.system('clear')
	
	def wejscie(self):
		print "Jestes w wiosce, masz przed soba sklep, oraz mape swiata"
		print "podchodzisz do mapy i mozesz wybrac podroz tylko do:"
		print "1. Las"
		print "2. Rzeka"
		wybor = raw_input("> ")
		if wybor == "1":
			return 'las'
		elif wybor == "2":
			return 'rzeka'
		else:
			return 'wioska'

			
			
			
class Las(object):
	def wejscie(self):
		print "jestes w lesie, mozesz sie na niego popatrzec i powdychac swierze powietrze"
		print "Gdzie idziesz"
		print "1. Wioska"
		print "2. Rzeka"
		wybor = raw_input("> ")
		if wybor == "1":
			return 'wioska'
		elif wybor == "2":
			return 'rzeka'	
		else:	
			return 'las'

class Rzeka(object):
	def wejscie(self):
		print "woda w rzece jest bardzo mokra"
		print "1. Wioska"
		print "2. Las"
		wybor = raw_input("> ")
		if wybor == "1":
			return 'wioska'
		elif wybor == "2":
			return 'las'
		else:
			return 'rzeka'	



			
class MapaGry(object):
	mapa = {
		'wioska' : Wioska(),
		'las': Las(),
		'rzeka': Rzeka(),
		'wieza': 'Wieza()',
		'legowisko smoka': 'Legowisko()',
		}
	def __init__(self, scena1):
		self.scena1 = scena1
		
	def pobierz_scene(self, nazwa_sceny):
		return MapaGry.mapa.get(nazwa_sceny)
			
	def pierwsza_scena(self):
		return self.pobierz_scene(self.scena1)


class Walka(object):
	lista_potworow = {
		1 : 'Ork',
		2 : 'Goblin',
		3 : 'Wilk',
		}
		
	def losowanie_potwora(self):
		przeciwnik = Walka.lista_potworow.get(randint(1,3))
		return przeciwnik
	
	
	def akcja(self):
		print " zaatakowal cie %s" % self.losowanie_potwora()
	
	los = Ork()
	pz, punkty_ataku, zloto = los.statystyki()
	
	print pz, punkty_ataku, zloto
	
a = Walka()
print a.akcja()

#a = MapaGry('wioska')
#b = Silnik(a)
#b.gra()

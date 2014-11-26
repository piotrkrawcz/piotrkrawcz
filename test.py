wersja1
class Lokacja(object):
	def __init__(self):
		self.przypadek = dict(
			mianownik = self.mianownik,
			dopelniacz = self.dopelniacz,
			narzednik = self.narzednik,
		
		)
	def nazwa(self, odmiana):
		return self.przypadek[odmiana]
		
class Wioska(Lokacja):
	mianownik = 'wioska'
	dopelniacz = 'wioski'
	narzednik = 'wioska'
	
	def wejscie(self, gracz):
		pass
wersja 2		
class Lokacja(object):
	przypadek = dict(
			mianownik = self.przypadki[0],
			dopelniacz = self.przypadki[1],
			narzednik = self.przypadki[2],
		
		)
	def nazwa(self, odmiana):
		return self.przypadek[odmiana]
		
class Wioska(Lokacja):
	przypadki = ['wioska','wioski','wioska']
	
		
	def wejscie(self, gracz):
		pass

from random import randint
import os
class Postac(object):
	def __init__(self,imie):
		self.modyfikator = 0
		self.imie = imie
		self.pz = 20 +randint(5,10)
		self.atak = 10 + self.modyfikator
		self.zloto = 10
		self.modyfikator = 0
		self.bron = 'drewniana palka'
		self.mikstura_pz = 1
		self.zaliczeniesekretnejmisji = 'niezaliczone'
	def atakmodyf(self, bron, modyfikacja):
		if bron == 'rusznica':
			self.atak = self.atak + 50
			self.bron = 'rusznica'
		elif bron == 'dobry_miecz':
			self.atak = self.atak + 25
			self.bron = 'dobry_miecz'
		elif bron == 'miecz':
			self.atak = self.atak + 10
			self.bron = 'miecz'
		self.atak = self.atak + modyfikacja
		if modyfikacja > 0:
			print 'cwiczyles rozne techniki walki i twoj poziom'
			print 'ataku zwiekszyl sie o %s i teraz wynosi %s' % (modyfikacja, self.atak) 
			raw_input('[enter]')
		return self.atak, self.bron	
	
	def zarobki(self, zyskstrata):
		self.zloto = self.zloto + zyskstrata
		print 'masz teraz w sakiewce', self.zloto, ' zlotych monet'
		raw_input('[enter]')
		return self.zloto 
	
	def leczenie(self, uzycie, lbmikstur):
		if uzycie == 1 and self.mikstura_pz > 0:
			self.pz = self.pz + 10
			self.mikstura_pz = self.mikstura_pz - 1
			print 'wypiles miksture leczenia, Twoje pz zwiekszyly sie o 10'
			print 'zostalo ci %s mikstur' % self.mikstura_pz
			raw_input('[enter]')
		elif uzycie == 1 and self.mikstura_pz == 0:
			print 'nie masz mikstury pz'
			raw_input('[enter]')
		elif lbmikstur == 1:
			self.mikstura_pz = self.mikstura_pz + 1
			print 'masz teraz %s mikstur leczenia' % self.mikstura_pz
			raw_input('[enter]')
		return self.pz, self.mikstura_pz
		
	def obrazenia(self, obrazenia):
		print '%s obrywa za %s' % (self.imie, obrazenia) 
		self.pz = self.pz - obrazenia
		if self.pz < 0:
			self.smierc()
		print 'pozostalo ci %s punktow zycia' % self.pz
		raw_input('[enter]')	
		return self.pz
	
	def opis(self):
		return self.imie, self.bron, self.atak, self.pz, self.zloto, self.zaliczeniesekretnejmisji
	def wydruk_opisu(self):
		os.system('clear')
		print 'Imie postaci: ', self.imie
		print 'Posiadana bron: ', self.bron
		print 'Punkty ataku z modyfikatorem za bron: ', self.atak
		print 'Punkty zycia: ', self.pz
		print 'Posiadane zloto: ', self.zloto
		print 'Mikstury leczenia, ilosc: ', self.mikstura_pz
		raw_input('[ENTER]')
	def sekretnamisja(self, wykonanie):
		self.zaliczeniesekretnejmisji = wykonanie
		return self.zaliczeniesekretnejmisji
			
	def smierc(self):
		print 'umarles, potwor je twoja glowe a potem zabiera sie za reszte ciala'
		exit(1)
		
imie = raw_input('podaj imie> ')
gracz = Postac(imie)		
	
class Potwor(object):

	def __init__(self):
		self.pz = 10
		self.punkty_ataku = 10
		self.zloto = 10
		
class Legowisko():
	def wejscie(self):
		os.system('clear')
		print 'przed toba wielka zielonoluska bestia'
		print 'paszcze ma wielkosci konia'
		print 'a zeby wielkie i ostre, chca cie pozrec'
		print 'nie ma stad gdzie uciec, wiec jedyne co pozostaje to walka'
		raw_input('[enter]')
		while True:
			final = Walka('smok')
			wynik = final.akcja()
			if wynik == 'wygrana':
				print 'pokonales bestie stanowiaca zagrozenie dla'
				print 'wioski - zostales jej bohaterem'
				exit(1)
			else:
				print 'ucieczka nie jest realna'
				print 'musisz ponownie przystapic do walki'
				raw_input('[enter]')
			
class Ork(Potwor):
	def __init__(self):
		self.rodzaj = 'Ork'
		
	def statystyki(self):
		super(Ork,self).__init__()
		self.pz = self.pz + randint(10,15)
		self.punkty_ataku = self.punkty_ataku + randint(10,15)
		self.zloto = self.zloto + randint(10,50)
		return self.rodzaj, self.pz, self.punkty_ataku, self.zloto

class Goblin(Potwor):
	def __init__(self):
		self.rodzaj = 'Goblin'
		
	def statystyki(self):
		super(Goblin,self).__init__()
		self.pz = self.pz + randint(1,5)
		self.punkty_ataku = self.punkty_ataku + randint(1,5)
		self.zloto = self.zloto + randint(1,5)
		return self.rodzaj, self.pz, self.punkty_ataku, self.zloto	

class Wilk(Potwor):
	
	def __init__(self):
		self.rodzaj = 'Wilk'
		
	def statystyki(self):
		super(Wilk,self).__init__()
		self.pz = self.pz + randint(5,15)
		self.punkty_ataku = self.punkty_ataku + randint(5,15)
		self.zloto = self.zloto + randint(10,15)
		return self.rodzaj, self.pz, self.punkty_ataku, self.zloto
		
class Smok(Potwor):
	
	def __init__(self):
		self.rodzaj = 'Smok'
		
	def statystyki(self):
		super(Smok,self).__init__()
		self.pz = self.pz + randint(100,155)
		self.punkty_ataku = self.punkty_ataku + randint(110,120)
		self.zloto = self.zloto + randint(1,5)
		return self.rodzaj, self.pz, self.punkty_ataku, self.zloto

class Sekretnamisja(object):
	
	def wejscie(self):
		gracz.sekretnamisja('zaliczenie')
		print 'wchodzac do wioski podchodzi do Ciebie stary dziad i mowi:'
		print 'dobry Panie slyszalem zescie bohatery potezne sa'
		print 'moze pomoglibyscie staremu dziadowi odgonic wstretnego pajaka'
		print 'ktory zagniezdzil sie pod moim domem, obiecuje nagrode godna bohatera'
		print '1. dobrze zaprowadz mnie tam'
		print '2. spieprzaj dziadu'
		wybor = raw_input('> ')
		if wybor == '1':
			print 'zgodziles sie pomoc dziadowi w oczyszczeniu domu z robactwa'
			print 'dziad prowadzil cie przez krete sciezki lesne'
			print 'co chwile skrecajac w prawo i lewo'
			print 'nie masz pojecia gdzie sie teraz znajdujesz'
			raw_input('[enter]')
			print 'z oddali poslyszales przerazliwy syk'
			print 'nie trzeba bylo dlugo czekac a zlokalziowales zrodlo tego syku'
			print 'gigantyczny pajak rzucil sie na Ciebie a dziad uciekl'
			print 'do lasu'
			print 'musisz walczyc'
			raw_input('[enter]')
			atak = Walka('spiderman')
			wynik = atak.akcja()
			if wynik == 'wygrana':
				os.system('clear')
				print 'po ciezkiej walce udaje ci sie powalic pajaka'
				print 'dziada nigdzie nie ma, ale odnajdujesz skrzynie'
				print 'i ciekawie zagladasz do srodka'
				print 'okazuje sie ze znajduje sie tam piekna rusznica i sakwa wypelniona zlotem'
				print 'co robisz?'
				print '1. zabieram wszystko'
				print '2. zabieram rusznice'
				print '3. zabieram zloto'
				print '4. nie jestem zlodziejem zostawiam to wszystko na miejscu'
				wybor = raw_input('> ')
				if wybor == '1':
					print 'zabierasz bron i zloto'
					print 'nie majac wiecej do roboty wracasz przez las do wioski'
					gracz.zarobki(500)
					gracz.atakmodyf('rusznica',0)
			
					return 'las'
				elif wybor == '2':
					print 'zabierasz bron '
					print 'nie majac wiecej do roboty wracasz przez las do wioski'
					gracz.atakmodyf('rusznica',0)
									
					return 'las'	
				elif wybor == '3':
					print 'zabierasz zloto'
					print 'nie majac wiecej do roboty wracasz przez las do wioski'
					gracz.zarobki(500)
					return 'las'
				else:
					print 'nie majac wiecej do roboty wracasz przez las do wioski'
					return 'las'
			else:
				print 'uciekales jak szalony od pajaka, ktory gonil Cie po calym lesie'
				print 'az w koncu dal sobie spokoj'
				print 'wokol ciebie pelno drzew'
				raw_input('[enter]')
				return 'las'
		
		
		
		else:
			print 'czujesz ze straciles szanse swego zycia w tej wiosce'
			print 'dziad byl przekonujacy i na pewno mial dobra nagrode'
			raw_input('[enter]')
			return 'wioska'
			
	def wykonanie(self):
		return self.misja









	
class Wioska(object):
	
	
	def wejscie(self):
		imie, bron, postac_atak, pz, zloto, misja = gracz.opis()
		os.system("clear")
		if postac_atak > 70 and misja == 'niezaliczone':
			return 'sekretnamisja'
		else:
			print "Jestes w wiosce, nie pamietasz jak tu dotares, nie znasz nazwy tej wioski"
			print "Wokol widac kilka charakterystycznych miejsc: sklep platnerza, tablica z rysunkami potworow"
			print "wyglada na informacyjna"
			print "obok tablicy stoi osilek, pewnie potrafilby nauczyc cie walczyc"
			print "widac rowniez slepego zebraka, oraz krupiera"
			print "jest tez mapa z zaznaczonymi miejscami obok wioski:"
			print "co robisz?"
			print "1. Ide do sklepu"
			print "2. Podchodze do tablicy"
			print "3. Podchodze do osilka"
			print "4. Chce opuscic wioske, wiec podchodze do mapy"
			print "5. Podchodze do krupiera"
			print "6. Sprawdzam postac"
			print "7. Pije miksture leczenia"
			wybor = raw_input("> ")
			if wybor == "1":
				return 'sklep'
			elif wybor == "2":
				os.system('clear')
				print "drodzy mieszkancy wsi nowosiolki"
				print "uprzejmie donosi sie ze we wiosku naszej zlo straszliwe sie dzieje"
				print "wszedy pelno plugastwa wszelakiego i niebezpiecznie sie wloczyc"
				print "orki wilki i gobliny napastuje one nas bardzo"
				print "tedy uwaza sie jakby komu zechcialo po lesie sie wloczyc niech nie walczy z orkami i wilkami"
				print "majac tylko prowizorycznom bron"
				print "soltys wsi Jan Konieczny"
				raw_input('[enter]')
				return 'wioska'
			elif wybor == "3":
				return 'trening'
			elif wybor == "4":
				print "Mapa jasno i precyzyjnie opisuje droge do lasu"
				raw_input('[enter]')
				return 'las'
			elif wybor == "5":
				print "krupier widzac ciebie patrzy sie chytrym wzrokiem"
				print "zagrajmy w kosci - mowi - ile stawiasz"
				print "nie mozesz wiecej niz", zloto
				ile = input('> ')
				if ile == 0:
					print 'po co mi dupe zawracasz, wynocha, go away'
					raw_input('[enter]')
					return 'wioska'
				elif ile > zloto:
					print 'nie masz tyle zlota debilu wynocha'
					raw_input('[enter]')
					return 'wioska'
				else:
					print "krupier pobiera od Ciebie sume", ile
					gracz.zarobki(-ile)
					krupier, graczk = 0,0
					while krupier == graczk:
						os.system('clear')
						krupier1, krupier2,gracz1,gracz2 = randint(2,6),randint(2,6),randint(1,6),randint(1,6),
						print "wygrywa ten kto wiecej rzuci na kosciach"
						print "krupier wyrzuca na pierwszej kosci %s a na drugiej %s" % (krupier1, krupier2)
						krupier = krupier1 + krupier2
						graczk = gracz1 + gracz2
						print "rzucasz na pierwszej", gracz1
						print "na drugiej", gracz2
						raw_input('[enter]')
						if krupier > graczk:
							print "baaaaardzo mi przykro ale przegrales, zabieram pieniazki, a ty uciekaj do wioski"
							raw_input('[enter]')
							return 'wioska'
						elif krupier < graczk:
							print 'udalo ci sie obwiesiu, bierz kase i spadaj'
							ile = 2*ile
							gracz.zarobki(ile)
							return 'wioska'    
						else:
							print "cholera wyrzucilismy po tyle samo, sprobujmy jeszcze raz"
							raw_input('[enter]')                	
			elif wybor == "6":
				gracz.wydruk_opisu()
				return 'wioska' 
			elif wybor == "7":
				gracz.leczenie(1,0)
				return 'wioska'
			
			else:
				return 'wioska'

class Sklep(object):
    
    def wejscie(self):
        imie, bron, postac_atak, pz, zloto, misja = gracz.opis()
        os.system('clear')
        print "wszedles do sklepu, sprzedawca sie pyta co chcialbys kupic"
        print "widzisz liste przedmiotow wraz z cenami"
        print "1. zwykly miecz - cena 20"
        print "2. dobry miecz - cena 250"
        print "3. rusznica - cena 1500"
        print "4. mikstura leczenia - cena 75"
        print "5. wracam do wioski"
        wybor = raw_input('> ')
        if wybor == '1':
            if zloto < 20:
                print 'Panie nie stac cie na taki miecz'
                raw_input('[enter]')
                return 'sklep'
            else:
                print 'dziekuje za udany zakup'
                gracz.zarobki(-20)
                gracz.atakmodyf('miecz',0)
                
                return 'sklep'        
        elif wybor == '2':
            if zloto < 250:
                print 'Panie nie stac cie na taki miecz'
                raw_input('[enter]')
                return 'sklep'
            else:
                print 'dziekuje za udany zakup'
                gracz.zarobki(-250)
                gracz.atakmodyf('dobry_miecz',0)
              
                return 'sklep'     
        elif wybor == '3':
            if zloto < 1500:
                print 'nie stac cie wynocha z mojego sklepu'
                raw_input('[enter]')
                return 'wioska'
            else:
                print 'dziekuje za udany zakup'
                gracz.zarobki(-1500)
                gracz.atakmodyf('rusznica',0)
             
                return 'sklep' 
        elif wybor == '4':
            if zloto < 75:
                print 'nie stac cie na miksture'
                raw_input('[enter]')
                return 'sklep'
            else:
                print 'dziekuje za udany zakup'
                gracz.zarobki(-75)
                gracz.leczenie(0,1)
                return 'sklep'
        elif wybor == '5':
            return 'wioska'
        else:
            return 'sklep'            
			
class Trening(object):
	def wejscie(self):
		imie, bron, postac_atak, pz, zloto, misja = gracz.opis()
		os.system('clear')
		print 'witaj mlodziencu widze ze masz ochote na trening'
		print 'mam nadzieje ze masz zloto'
		print 'ile chcesz trenowac?'
		print '1. chce trenowac do poznej nocy [koszt 400, atak +10]'
		print '2. chce trenowac do wieczora [koszt 200, atak +5]'
		print '3. chce trenowac do poludnia [koszt 40, atak +1]'
		print '4. nie chce trenowac'
		print '5. sprawdzam postac'
		wybor = raw_input('> ')
		if wybor == '1':
			if zloto < 400:
				print 'nie bede z toba trenowac nie masz pieniedzy'
				raw_input('[enter]')
				return 'trening'
			else:
				gracz.zarobki(-400)
				gracz.atakmodyf(0, 10)
				return 'trening'
		elif wybor == '2':
			if zloto < 200:
				print 'nie bede z toba trenowac nie masz pieniedzy'
				raw_input('[enter]')
				return 'trening'
			else:
				gracz.zarobki(-200)
				gracz.atakmodyf(0, 5)
				return 'trening'
		elif wybor == '3':
			if zloto < 40:
				print 'nie bede z toba trenowac nie masz pieniedzy'
				raw_input('[enter]')
				return 'trening'
			else:
				gracz.zarobki(-40)
				gracz.atakmodyf(0, 1)
				return 'trening'		
		elif wybor == '4':
			return 'wioska'
		elif wybor == '5':
			gracz.wydruk_opisu()
			return 'trening'
		else:
			return 'trening'
class Las(object):
	def wejscie(self):
		os.system('clear')
		print "jestes w lesie, mozesz sie na niego popatrzec i powdychac swierze powietrze"
		print "Gdzie idziesz"
		print "1. Wioska"
		print "2. Dalej zwiedzam las"
		print "3. Sprawdzam postac"
		print "4. Pije miksture leczenia"
		wybor = raw_input("> ")
		if wybor == "1":
			return 'wioska'
		elif wybor == "2":
			atak = Walka(0)
			wynik = atak.akcja()
			if wynik == 'wygrana':
				print 'po pokonaniu przeciwnika mozesz udac sie nad rzeke, idziesz tam?'
				rzeka = raw_input('[tak/nie]> ')
				if rzeka == 'tak':
					return 'rzeka'
				else:	
					return 'las'
			return 'las'		
		elif wybor == '3':
			gracz.wydruk_opisu()
			return 'las'
		elif wybor == '4':
			gracz.leczenie(1,0)
			return 'las'
		else:	
			return 'las'

class Wieza(object):
	def wejscie(self):
		os.system('clear')
		print 'zmeczony podroza zblizasz sie w koncu do ponurej wiezy'
		print 'wylaniajacej sie leniwie zza pagorka'
		print 'podchodzac blizej dostrzegasz ze jest jest ona po czesci zawalona'
		print 'jest widoczne zejscie ponizej skad slychac dzikie wrzaski'
		print 'co robisz?'
		print "1. wracam do wioski"
		print "2. schodze po schodach w glab wiezy"
		print "3. wracam nad rzeke"
		print "4. Sprawdzam postac"
		print "5. Pije miksture leczenia"
		wybor = raw_input('> ')
		if wybor == '1':
			return 'wioska'
		elif wybor == '2':
			print 'schodzac chwile po schodach dostrzegasz 3 istoty'
			print 'z ktorymi juz zdarzalo ci sie walczyc'
			print 'jednak ta wygladaja znacznie agresywniej niz poprzednie'
			raw_input('[enter]')
			x = 3
			while x <> 0:
				x = x - 1
				potwor1 = Walka(0)
				wynik = potwor1.akcja()
				if wynik == 'wygrana':
					if x <> 0:
						print 'zostaly jeszcze %s potwory' % x
					else:
						print 'pokanales wszystkie stojace na twojej drodze potwory'
					raw_input('[enter]')
				else:
					print 'uciekasz schodami spowrotem w okolice wiezy'
					print 'wychodzac juz na powierzchnie widzisz ze potwory cie nie gonia'
					print 'lecz potykasz sie uderzasz glowa w konar drzewa'
					print 'tracisz przytmnosc, budzisz sie nastepnego ranka'
					print 'zmokniety i zmarzniety'
					raw_input('[enter]')
					return 'wieza'
			os.system('clear')		
			print 'po pokonaniu plugawych istot widzisz przed soba duzy portal'
			print 'za ktorym to w oddali widac ogromnego ziejacego ogniem smoka'
			print 'na predce oceniasz swoje szanse w starciu z bestia i wynika ze'
			imie, bron, postac_atak, pz, zloto, misja = gracz.opis()
			if postac_atak < 90:
				print 'nie masz zadnych szans w walce z bestia'
			elif postac_atak in range(90, 120):
				print 'potrzebujesz duzo szczescia aby zwyciezyc'
			elif postac_atak in range(120,150):
				print 'szanse sa wyrownane'
			elif postac_atak > 150:
				print 'smok nie ma z toba zadnych szans'
				print 'od czasu kiedy wyladowales w wiosce'
				print 'stales sie jednym z najpotezniejszych'
				print 'smiertelnikow na Ziemi'
			print 'co zamierzasz teraz zrobic?'
			print 'jesli wrocisz do wioski, mozesz byc pewien'
			print 'ze potwory pojawia sie na nowo'
			print '1. ide na spotkanie ze smokiem'
			print '2. wracam do wioski'
			wybor = raw_input('> ')
			if wybor == '1':
				return 'legowisko smoka'
			else:
				return 'wioska'
				
		elif wybor == '3':
			return 'rzeka'
		elif wybor == '4':
			gracz.wydruk_opisu()
			return 'wieza'
		elif wybor == '5':
			gracz.leczenie(1,0)
			return 'wieza'
		else:
			return 'wieza'
			
class Rzeka(object):
	def wejscie(self):
		os.system('clear')
		print "jestes nad rzeka, woda jest bardzo gleboka"
		print "w oddali widac las, mozesz rowniez isc dalej wzdluz rzeki w kierunku oslawionej wiezy"
		print "Gdzie idziesz?"
		print "1. wracam do wioski"
		print "2. Ide wzdluz rzeki"
		print "3. Ide do lasu"
		print "4. Sprawdzam postac"
		print "5. Pije miksture leczenia"
		wybor = raw_input("> ")
		if wybor == "1":
			return 'wioska'
		elif wybor == "2":
			atak = Walka(0)
			wynik = atak.akcja()
			if wynik == 'wygrana':
				print 'po pokonaniu przeciwnika mozesz udac sie w strone wiezy, idziesz tam?'
				rzeka = raw_input('[tak/nie]> ')
				if rzeka == 'tak':
					return 'wieza'
				else:	
					return 'rzeka'
			return 'rzeka'
		elif wybor == '3':
			return 'las'
		elif wybor == '4':
			gracz.wydruk_opisu()
			return 'rzeka'
		elif wybor == '5':
			gracz.leczenie(1,0)
			return 'rzeka'
		else:	
			return 'rzeka'
		
class Silnik(object):
	mapa = {
		'wioska' : Wioska(),
		'las': Las(),
		'rzeka': Rzeka(),
		'sklep': Sklep(),
		'trening' : Trening(),
		'wieza': Wieza(),
		'legowisko smoka': Legowisko(),
		'sekretnamisja' : Sekretnamisja(),
		}
	def __init__(self):
		self.pierwszamapa = Silnik.mapa.get('wioska')
	
	
	def pobierz_scene(self, mapa):
		return Silnik.mapa.get(mapa)
		
	def gra(self):
		obecnalokacja = self.pierwszamapa
		
		while True:
			kolejnalokacja = obecnalokacja.wejscie()
			obecnalokacja = self.pobierz_scene(kolejnalokacja)

class Spiderman(Potwor):
	def __init__(self):
		self.rodzaj = 'Gigantyczny Pajak'
		
	def statystyki(self):
		super(Spiderman,self).__init__()
		self.pz = self.pz + randint(40,80)
		self.punkty_ataku = self.punkty_ataku + randint(55,75)
		self.zloto = self.zloto + randint(1,2)
		return self.rodzaj, self.pz, self.punkty_ataku, self.zloto			
		
			
class Walka(object):
	lista_potworow = {
		1 : Ork(),
		2 : Goblin(),
		3 : Wilk(),
		4 : Smok(),
		5 : Spiderman(),
		}
	def __init__(self, specjalny):
		if specjalny == 'smok':
			self.potwor = Walka.lista_potworow.get(4)
			self.elit = 1
		elif specjalny == 'spiderman':
			self.potwor = Walka.lista_potworow.get(5)
			self.elit = 1
		else:	
			self.potwor = Walka.lista_potworow.get(randint(1,3))
			self.elit = 0
		
	def akcja(self):
		rodzaj, potwor_pz, potwor_atak, potwor_zloto = self.potwor.statystyki()
		imie, bron, postac_atak, pz, zloto, misja = gracz.opis()
		if pz > 10 and postac_atak > 50 and self.elit == 0:
			potwor_pz = potwor_pz * 3
			potwor_atak = potwor_atak * 3
			potwor_zloto = potwor_zloto * 4
			rodzaj = 'elitarny ' + rodzaj
		elif pz > 5 and postac_atak > 25 and self.elit == 0:	
			potwor_pz = potwor_pz * 2
			potwor_atak = potwor_atak * 2
			potwor_zloto = potwor_zloto * 3
			rodzaj = 'potezny ' + rodzaj
		else:
			pass
			
		print 'zaatakowal cie ', rodzaj
		
		runda = 1
		ucieczka = 2
		while potwor_pz > 0 and ucieczka <> '1':
			os.system('clear')
			print 'rozpoczyna sie runda', runda
			runda = runda + 1
			print '%s atakuje cie, co robisz?' % rodzaj
			print '1.boje sie uciekam'
			print '2.atakuje!!'
			print '3.pije miksture leczenia'
			ucieczka = raw_input('> ')
			if ucieczka == '3':
				gracz.leczenie(1,0)
			elif ucieczka == '2':
				obrazenia = (potwor_atak + randint(1,15))-(postac_atak + randint(1,15))
				if obrazenia > 0:
					gracz.obrazenia(obrazenia)
				else:
					potwor_pz = potwor_pz + obrazenia
					print '%s oberwal za %s i zostalo mu %s' % (rodzaj, obrazenia, potwor_pz)
					raw_input('[enter]')	
		if ucieczka <> '1':
			print '%s zostawil w zwlokach %s zlotych monet, ktore chciwie chowasz do kieszeni' % (rodzaj, potwor_zloto)
			gracz.zarobki(potwor_zloto)
			return 'wygrana'
		print 'tchorzliwie uciekasz z pola walki ', imie
		print ' najwidoczniej %s to zbyt potezny przeciwnik dla ciebie' % rodzaj
		raw_input('[enter]')
		return 'porazka'

	

granie = Silnik()
granie.gra()		

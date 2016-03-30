import threading
import random
import numpy as np

globina = 3
CRNI = 1
BELI = 2

def smiselne_pozicije(neki_seznam):
	sez = set()
	for (i, j) in neki_seznam:
		if i+1 <= 18:
			sez.add((i + 1, j))
			sez.add((i + 1, j - 1))			
		if j+1 <= 18:
			sez.add((i, j + 1))
			sez.add((i - 1, j + 1))
		if j+1 <= 18 and i+1 <=18:
			sez.add((i + 1, j + 1))
		sez.add((i - 1, j - 1))
		sez.add((i - 1, j))
		sez.add((i, j - 1))
	return list(sez)
	

class Racunalnik():
	def __init__(self, gui, algoritem, barva):
		self.gui = gui
		self.barva = self.gui.igra.na_potezi
		self.algoritem = algoritem
		self.mislec = None

	def igraj(self):
		self.mislec = threading.Thread(target=lambda: self.algoritem.izracunaj_potezo(self.gui.igra.kopija()))
		self.mislec.start()
		self.gui.plosca.after(100, self.preveri_potezo)

	def preveri_potezo(self):
		if self.algoritem.poteza is not None:
			(i, j) = self.algoritem.poteza
			self.gui.povleci_potezo(i, j)
			self.mislec = None
		else:
			self.gui.plosca.after(100, self.preveri_potezo)

	def prekini(self):
		if self.mislec:
			print("Prekinjamo {0}".format(self.mislec))
			self.algoritem.prekini()
			self.mislec.join()
			self.mislec = None

	# potrebno je prepovedati klikanje uporabnika na plošči medtem, ko računalnik razmišlja!!!
	# lahko da vlakna to že sama po sebi to rešijo
	def klik(self, i, j):
		pass

class Minimax():
	def __init__(self, globina):
		self.igra = None
		self.prekinitev = False
		self.globina = globina
		self.poteza = None

	def prekini(self):
		self.prekinitev = True

	def izracunaj_potezo(self, igra):
		self.igra = igra
		self.prekinitev = False
		self.jaz = self.igra.na_potezi
		self.poteza = None
		(poteza, vrednost) = self.minimax(self.globina, -10000000000, 10000000000,True, self.jaz)
		self.jaz = None
		self.igra = None
		if not self.prekinitev:
			print("minimax: poteza {0}, vrednost {1}".format(poteza, vrednost))
			self.poteza = poteza

	def vrednost_skupaj_1(self, tabela):
		ZMAGA = 1000000
		def seznamdolzine5(sez):
			rezultat = []
			rezultat += [sez[0:5]]
			rezultat += [sez[4:9]]
			rezultat += [sez[8:13]]
			rezultat += [sez[12:17]]
			rezultat += [sez[16:19]]
			return rezultat

		def sezseznamov5(tabela):
			sez = []
			for element in tabela:
				sez += seznamdolzine5(element)
			return sez

		def vse_diagonale(tabela):
			matrika1 = np.array(tabela)
			diagonale = []
			dolzina = len(tabela)
			#le diagonale, ki so dolzine vsaj 5
			for i in range(5-dolzina, dolzina-4):
				diagonale.append(list(matrika1.diagonal(i)))
				diagonale.append(list(np.fliplr(matrika1).diagonal(i)))
			return diagonale

		def stolpci(tabela):
			stolp = [list(x) for x in zip(*tabela)]
			return stolp

		vrstice = tabela
		vsistolpci = stolpci(tabela)
		diagonale = vse_diagonale(tabela)
		skupaj = sezseznamov5(vrstice + vsistolpci + diagonale)
		vrednost = 0
		if self.igra.na_potezi == BELI:
			for elem in skupaj:
				if len(elem)<5:
					pass
				elif (1 in elem) and (2 in elem):
					pass
				if elem.count(1) == 5:
					vrednost = -ZMAGA
				elif elem.count(2) == 5:
					vrednost = ZMAGA
				elif 2 in elem:
					vrednost += elem.count(2)*50
				elif 1 in elem:
					vrednost -= elem.count(1)*1000
			return vrednost
		elif self.igra.na_potezi == CRNI:
			for elem in skupaj:
				if len(elem)<5:
					pass
				elif (1 in elem) and (2 in elem):
					pass
				if elem.count(1) == 5:
					vrednost = -ZMAGA
				elif elem.count(2) == 5:
					vrednost = ZMAGA
				elif 1 in elem:
					vrednost -= elem.count(1)*1000
				elif 2 in elem:
					vrednost += elem.count(2)*50
			return vrednost
			
	def vrednost_skupaj(self, tabela, barva=None):
		ZMAGA = 1000000
		crni_boljsi = ["01110", "0110", "010", "211101", "011010", "010110"]
		crni_slabsi = ["211110", "011112", "101112", "211011", "110112", "21110", "01112", "2110", "0112", "210", "012"]
		def crni(niz, barva):
			#prvi in zanji element, da se ujema z elementi iz seznama
			niz = "2" + niz + "2"
			vrednost = 0
			if niz.count("11111") > 0:
				vrednost += ZMAGA
				return vrednost
			elif niz.count("011110") > 0:
				vrednost += ZMAGA//2
			#elif niz.count("01110") > 0:
			#	vrednost += ZMAGA//3
			elif niz.count("10111") > 0:		
				vrednost += ZMAGA//5
			elif niz.count("11011") > 0:		
				vrednost += ZMAGA//5
			elif niz.count("11101") > 0:		
				vrednost += ZMAGA//5
			elif niz.count("11110") > 0:		
				vrednost += ZMAGA//5
			elif niz.count("01111") > 0:		
				vrednost += ZMAGA//5
			elif niz.count("01110") > 0:		
				vrednost += ZMAGA//12
			
			for el in crni_boljsi:
				dolzina = len(el)
				ponavljanja = niz.count(el)
				ugodne = el.count("1")
				vrednost += ponavljanja * 4**ugodne
			for el in crni_slabsi:
				dolzina = len(el)
				ponavljanja = niz.count(el)
				ugodne = el.count("1")
				vrednost += ponavljanja * 3**ugodne

			return vrednost


		beli_boljsi = ["02220", "0220", "020", "122202", "022020", "020220"]
		beli_slabsi = ["122220", "022221", "202221", "122022", "220221" "12220", "02221", "1220", "0221", "120", "021"]

		def beli(niz, barva):
			niz = "1" + niz + "1"
			vrednost = 0
			if niz.count("22222") > 0:
				vrednost += ZMAGA
				return vrednost	
			elif niz.count("022220") > 0:
				vrednost += ZMAGA//5
			#elif niz.count("02220") > 0: #and barva == BELI:
			#	vrednost += ZMAGA//3
			elif niz.count("20222") > 0:		
				vrednost += ZMAGA//10
			elif niz.count("22022") > 0:		
				vrednost += ZMAGA//10
			elif niz.count("22202") > 0:		
				vrednost += ZMAGA//10
			elif niz.count("22220") > 0:		
				vrednost += ZMAGA//10
			elif niz.count("02222") > 0:		
				vrednost += ZMAGA//10

			for el in beli_slabsi:
				dolzina = len(el)
				ponavljanja = niz.count(el)
				ugodne = el.count("2")
				vrednost += ponavljanja * 4**ugodne
			for el in beli_boljsi:
				dolzina = len(el)
				ponavljanja = niz.count(el)
				ugodne = el.count("2")
				vrednost += ponavljanja * 3**ugodne

			return vrednost

		def vrednost_vrstic(tabela, barva):
			rezultat = 0
			for vrstica in tabela:
				nizek = ""
				for znak in vrstica:
					nizek += str(znak)
				rezultat += crni(nizek, barva) - beli(nizek, barva)
			return rezultat

		def vrednost_stolpcev(tabela, barva):
			#trans = numpy.array(tabela).transpose()
			stolpci = [list(x) for x in zip(*tabela)]
			return vrednost_vrstic(stolpci, barva)

		def vse_diagonale(tabela):
			matrika1 = np.array(tabela)
			diagonale = []
			dolzina = len(tabela)
			#le diagonale, ki so dolzine vsaj 5
			for i in range(5-dolzina, dolzina-4):
				diagonale.append(list(matrika1.diagonal(i)))
				diagonale.append(list(np.fliplr(matrika1).diagonal(i)))
			

			return diagonale

		def vrednost_diagonal(tabela, barva):
				return vrednost_vrstic(vse_diagonale(tabela), barva)

		if self.igra.na_potezi == CRNI:
			return vrednost_vrstic(tabela, barva) + vrednost_stolpcev(tabela, barva) + vrednost_diagonal(tabela, barva)
		elif self.igra.na_potezi == BELI:
			return -(vrednost_vrstic(tabela, barva) + vrednost_stolpcev(tabela, barva) + vrednost_diagonal(tabela, barva))
		else:
			assert False, "Napacna barva v vrednost_skupaj"

	
	def minimax(self, globina, alfa, beta, maksimiziramo, trenutni):		
		if self.prekinitev:
			print("Minimax prekinja")
			return (None, 0)
		
		if self.igra.konec:
			if trenutni == CRNI:
				return (None, 10000000000)
			elif trenutni == BELI:
				return (None, -10000000000)
			else:
				return (None, 0)
		if len(self.igra.poteze) == 0:
			return ((9,9), 10000000000)
		if globina == 0:
			#print("globina 0")
			return (None, self.vrednost_skupaj(self.igra.tabela))
		if maksimiziramo:
			najpoteza = None
			vrednostnajpoteze = -10000000000
			for (iv, ist) in smiselne_pozicije(self.igra.poteze):
				if self.igra.tabela[ist][iv] == 0:
					self.igra.povleci_racunalnik(iv, ist)
					vr1 = self.minimax(globina-1, alfa, beta, not maksimiziramo, self.igra.nasprotnik())[1]
					self.igra.razveljavi()
					if vr1 > vrednostnajpoteze:
						vrednostnajpoteze = vr1
						najpoteza = (iv, ist)
					if vr1 > alfa:
						alfa = vr1
					if beta <= alfa:
						break
		else:
			najpoteza = None
			vrednostnajpoteze = 10000000000
			for (iv, ist) in smiselne_pozicije(self.igra.poteze):
				if self.igra.tabela[ist][iv] == 0:
					self.igra.povleci_racunalnik(iv, ist)
					vr1 = self.minimax(globina-1, alfa, beta, not maksimiziramo, self.igra.nasprotnik())[1]
					self.igra.razveljavi()
					if vr1 < vrednostnajpoteze:
						vrednostnajpoteze = vr1
						najpoteza = (iv, ist)
					if vr1 < beta:
						beta = vr1
					if beta <= alfa:
						break
		assert (najpoteza is not None), "minimax: izračunana poteza je None"
		return (najpoteza, vrednostnajpoteze)





import threading
import random
from vrednost_boljsa import*
globina = 2
CRNI = 1
BELI = 2


def prebarvaj(barva):
	if barva == CRNI:
		return BELI
	else:
		return CRNI

def smiselne_pozicije(neki_seznam):
	sez = set()
	for (i, j) in neki_seznam:
		sez.add((i + 1, j))
		sez.add((i, j + 1))
		sez.add((i + 1, j + 1))
		sez.add((i - 1, j))
		sez.add((i, j - 1))
		sez.add((i - 1, j - 1))
		sez.add((i - 1, j + 1))
		sez.add((i + 1, j - 1))
	return list(sez)

class Racunalnik():
	def __init__(self, igra, algoritem, barva):
		self.igra = igra
		self.barva = barva
		self.algoritem = algoritem
		self.mislec = None

	def igraj(self):
		self.mislec = threading.Thread(target=lambda: self.algoritem.izracunaj_potezo(self.igra.kopija()))
		self.mislec.start()
		self.igra.gui.plosca.after(100, self.preveri_potezo)
#		(i, j) = self.algoritem.izracunaj_potezo(self.igra.kopija())
#		if self.algoritem.poteza is not None:
#			self.igra.gui.povleci_potezo(i, j)

	def preveri_potezo(self):
		if (self.algoritem.poteza is not None) and (not self.igra.konec):
			(i, j) = self.algoritem.poteza
			self.igra.gui.povleci_potezo(i, j)
			#self.igra.zamenjaj()
			self.mislec = None
		else:
			self.igra.gui.plosca.after(100, self.preveri_potezo)

	def prekini(self):
		if self.mislec:
			print("Prekinjamo {0}".format(self.mislec))
			self.algoritem.prekini()
			self.mislec.join()
			self.mislec = None

	# potrebno je prepovedati klikanje uporabnika na plošči medtem, ko računalnik razmišlja!!!
	# lahko da vlakna to že sama po sebi to rešijo
	def klik(self, event):
		pass

class Minimax():
	def __init__(self, globina):
		self.igra = None
		self.prekinitev = False
		self.globina = globina
		self.poteza = None
		self.smiselne_moznosti = []

	def prekini(self):
		self.prekinitev = True

	def izracunaj_potezo(self, igra):
		self.igra = igra
		self.smiselne_moznosti = smiselne_pozicije(self.igra.poteze)
		self.prekinitev = False
		self.jaz = self.igra.na_potezi
		self.poteza = None
		(poteza, vrednost) = self.minimax(self.globina, True, self.jaz.barva)
		self.jaz = None
		self.igra = None
		if not self.prekinitev:
			print("minimax: poteza {0}, vrednost {1}".format(poteza, vrednost))
			self.poteza = poteza

	def minimax(self, globina, maksimiziramo, barva):		
		if self.prekinitev:
			print("Minimax prekinja")
			return (None, 0)

		if self.igra.konec:
			if self.igra.na_potezi.barva == CRNI:
				return (None, 10000000000)
			elif self.igra.na_potezi.barva == BELI:
				return (None, -10000000000)
			# izenačenje !?!
			else:
				return (None, 0)
		if len(self.igra.poteze) == 0:
			return ((10,10), 10000000000)
		if globina == 0:
			#print("globina 0")
			return (None, vrednost_skupaj(self.igra.tabela, barva))
		if maksimiziramo:
			najpoteza = None
			vrednostnajpoteze = -10000000000
#			for iv, vrstica in enumerate(self.igra.tabela):
#				for ist, stolpec in enumerate(vrstica):
			for (iv, ist) in self.smiselne_moznosti:
				if self.igra.tabela[ist][iv] == 0:
					self.igra.povleci(iv, ist)
					vr1 = self.minimax(globina-1, not maksimiziramo, prebarvaj(barva))[1]
					self.igra.razveljavi()
					if vr1 > vrednostnajpoteze:
						vrednostnajpoteze = vr1
						najpoteza = (iv, ist)
		else:
			najpoteza = None
			vrednostnajpoteze = 10000000000
#			for iv, vrstica in enumerate(self.igra.tabela):
#				for ist, stolpec in enumerate(vrstica):
			for (iv, ist) in self.smiselne_moznosti:
				if self.igra.tabela[ist][iv] == 0:
					self.igra.povleci(iv, ist)
					vr1 = self.minimax(globina-1, not maksimiziramo, prebarvaj(barva))[1]
					self.igra.razveljavi()
					if vr1 < vrednostnajpoteze:
						vrednostnajpoteze = vr1
						najpoteza = (iv, ist)

		assert (najpoteza is not None), "minimax: izračunana poteza je None"
		return (najpoteza, vrednostnajpoteze)




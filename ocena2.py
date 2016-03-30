import numpy as np

BELI = 2
CRNI = 1
def vrednost_skupaj(tabela):
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
				vrednost = ZMAGA
			elif elem.count(2) == 5:
				vrednost = -ZMAGA
			elif 1 in elem:
				vrednost += elem.count(1)*50
			elif 2 in elem:
				vrednost -= elem.count(2)*100
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
				vrednost -= elem.count(1)*100
			elif 2 in elem:
				vrednost += elem.count(2)*50
		return vrednost
import numpy as np
ZMAGA = 1000000

CRNI = 1
BELI = 2

seznam_1 = ["01110", "0110", "010", "211101", "011010", "010110"]
seznam_2 = ["211110", "011112", "101112", "211011", "110112", "21110", "01112", "2110", "0112", "210", "012"]
def crni(niz, barva):
	#prvi in zanji element, da se ujema z elementi iz seznama
	niz = "2" + niz + "2"
	vrednost = 0
	if niz.count("11111") > 0:
		vrednost = ZMAGA
		return vrednost
	elif niz.count("011110") > 0:
		vrednost += ZMAGA//2
	elif niz.count("01110") > 0 and barva == BELI:
		vrednost += ZMAGA//2
	elif niz.count("11110") > 0 and barva == BELI:
		vrednost += ZMAGA//2
	elif niz.count("01111") > 0 and barva == BELI:
		vrednost += ZMAGA//2
	for el in seznam_1:
		dolzina = len(el)
		ponavljanja = niz.count(el)
		ugodne = el.count("1")
		vrednost += ponavljanja * 4**ugodne
	for el in seznam_2:
		dolzina = len(el)
		ponavljanja = niz.count(el)
		ugodne = el.count("1")
		vrednost += ponavljanja * 3**ugodne

	return vrednost


seznam_3 = ["02220", "0220", "020", "122202", "022020", "020220"]
seznam_4 = ["122220", "022221", "202221", "122022", "220221" "12220", "02221", "1220", "0221", "120", "021"]

def beli(niz, barva):
	niz = "1" + niz + "1"
	vrednost = 0
	if niz.count("22222") > 0:
		vrednost = ZMAGA
		return vrednost
	elif niz.count("022220") > 0:
		vrednost += ZMAGA//2
	elif niz.count("02220") > 0 and barva == CRNI:
		vrednost += ZMAGA//2
	elif niz.count("22220") > 0 and barva == CRNI:
		vrednost += ZMAGA//2
	elif niz.count("02222") > 0 and barva == CRNI:
		vrednost += ZMAGA//2
	for el in seznam_4:
		dolzina = len(el)
		ponavljanja = niz.count(el)
		ugodne = el.count("2")
		vrednost += ponavljanja * 4**ugodne
	for el in seznam_3:
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

	transponrana = [list(x) for x in zip(*tabela)]
	matrika2 = np.array(transponrana)
	for i in range(5-dolzina, dolzina-4):
		diagonale.append(list(matrika2.diagonal(i)))

	return diagonale

def vrednost_diagonal(tabela, barva):
		return vrednost_vrstic(vse_diagonale(tabela), barva)

def vrednost_skupaj(tabela, barva):
	if barva == CRNI:
		return vrednost_vrstic(tabela, barva) + vrednost_stolpcev(tabela, barva) + vrednost_diagonal(tabela, barva)
	elif barva == BELI:
		return -(vrednost_vrstic(tabela, barva) + vrednost_stolpcev(tabela, barva) + vrednost_diagonal(tabela, barva))
	else:
		assert False, "Napacna barva v vrednost_skupaj"
# tabela1 = [[0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 2, 1, 1, 0, 0, 0], [0, 0, 1, 0, 2, 2, 2, 2, 2, 1, 2, 2, 0, 1, 0, 0, 2, 0, 2], [2, 0, 1, 0, 2, 0, 2, 2, 0, 1, 0, 2, 0, 0, 0, 2, 0, 0, 2], [0, 1, 0, 2, 0, 0, 0, 2, 0, 2, 1, 0, 0, 2, 0, 0, 1, 2, 1], [2, 1, 0, 2, 0, 0, 0, 0, 0, 2, 2, 0, 1, 0, 0, 1, 1, 0, 2], [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 2, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 2, 2, 0, 0, 0, 0], [0, 0, 0, 1, 1, 2, 0, 0, 0, 0, 0, 1, 0, 2, 0, 1, 1, 2, 1], [1, 0, 0, 0, 1, 0, 2, 0, 1, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0], [2, 2, 0, 0, 0, 2, 2, 1, 2, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1], [0, 2, 1, 0, 2, 0, 0, 1, 0, 0, 1, 1, 0, 2, 2, 0, 1, 2, 0], [2, 1, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 2, 0, 1, 1, 0, 0, 1, 1, 0, 2, 0, 2, 1, 0], [0, 0, 1, 1, 2, 2, 0, 2, 1, 0, 2, 1, 0, 2, 0, 0, 0, 1, 0], [1, 0, 0, 2, 2, 2, 0, 0, 0, 1, 2, 1, 0, 2, 1, 0, 2, 0, 0], [1, 0, 2, 1, 1, 2, 2, 0, 2, 1, 0, 0, 1, 0, 1, 1, 2, 0, 0], [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 2, 0, 0, 1, 0, 0, 1], [2, 0, 1, 0, 0, 0, 2, 0, 0, 1, 0, 1, 0, 2, 0, 0, 0, 1, 0], [2, 1, 2, 0, 0, 1, 0, 0, 0, 1, 0, 2, 0, 0, 1, 0, 2, 0, 0]]
# tabela2 = [[0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 2, 1, 1, 0, 0, 0], [0, 0, 1, 0, 0, 2, 2, 2, 2, 1, 2, 2, 0, 1, 0, 0, 2, 0, 2], [2, 0, 1, 0, 2, 0, 2, 2, 0, 1, 0, 2, 0, 0, 0, 2, 0, 0, 2], [0, 1, 0, 2, 0, 0, 0, 2, 0, 2, 1, 0, 0, 2, 0, 0, 1, 2, 1], [2, 1, 0, 2, 0, 0, 0, 0, 0, 2, 2, 0, 1, 0, 0, 1, 1, 0, 2], [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 2, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 2, 2, 0, 0, 0, 0], [0, 0, 0, 1, 1, 2, 0, 0, 0, 0, 0, 1, 0, 2, 0, 1, 1, 2, 1], [1, 0, 0, 0, 1, 0, 2, 0, 1, 0, 0, 0, 0, 0, 2, 2, 0, 2, 0], [2, 2, 0, 0, 0, 2, 2, 1, 2, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1], [0, 2, 1, 0, 2, 0, 0, 1, 0, 0, 1, 1, 0, 2, 2, 0, 1, 2, 0], [2, 1, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 2, 0, 1, 1, 0, 0, 1, 1, 0, 2, 0, 2, 1, 0], [0, 0, 1, 1, 2, 2, 0, 2, 1, 0, 2, 1, 0, 2, 0, 0, 0, 1, 0], [1, 0, 0, 2, 2, 2, 0, 0, 0, 1, 2, 1, 0, 2, 1, 0, 2, 0, 0], [1, 0, 2, 1, 1, 2, 2, 0, 2, 1, 0, 1, 1, 0, 1, 1, 2, 0, 0], [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 2, 0, 0, 1, 0, 0, 1], [2, 0, 1, 0, 0, 0, 2, 0, 0, 1, 0, 1, 0, 2, 0, 0, 0, 1, 0], [2, 1, 2, 0, 0, 1, 0, 0, 0, 1, 0, 2, 0, 0, 1, 0, 2, 0, 0]]
# tabela3 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
# print(vrednost_skupaj(tabela2))
# print(vrednost_skupaj(tabela1))
# print(vrednost_skupaj(tabela3))
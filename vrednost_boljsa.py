import numpy as np
ZMAGA = 1000000

CRNI = 1
BELI = 2

crni_boljsi = ["01110", "0110", "010", "211101", "011010", "010110"]
crni_slabsi = ["211110", "011112", "101112", "211011", "110112", "21110", "01112", "2110", "0112", "210", "012"]
def crni(niz, barva):
	#prvi in zanji element, da se ujema z elementi iz seznama
	niz = "2" + niz + "2"
	vrednost = 0
	if niz.count("11111") > 0:
		vrednost += ZMAGA
		return vrednost
	ponovitve = niz.count("011110")
	if ponovitve > 0:
		vrednost += ponovitve * ZMAGA//2
	ponovitve = niz.count("01110") 
	if ponovitve  > 0:
		vrednost += ponovitve * ZMAGA//3
	ponovitve = niz.count("10111") 
	if ponovitve > 0:		
		vrednost += ponovitve * ZMAGA//5
	ponovitve = niz.count("11011") 
	if ponovitve > 0:		
		vrednost += ponovitve * ZMAGA//5
	ponovitve = niz.count("11101") 
	if ponovitve > 0:		
		vrednost += ponovitve * ZMAGA//5
	ponovitve = niz.count("11110") 
	if ponovitve > 0:		
		vrednost += ponovitve * ZMAGA//5
	ponovitve = niz.count("01111") 
	if ponovitve > 0:		
		vrednost += ponovitve * ZMAGA//5
	ponovitve = niz.count("01110") 
	if ponovitve > 0:		
		vrednost += ponovitve * ZMAGA//12
	
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
	ponovitve = niz.count("022220")
	if ponovitve  > 0:
		vrednost += ponovitve * ZMAGA//5
	ponovitve = niz.count("02220") #
	if ponovitve > 0: #and barva == Bponovitve * ELI:
		vrednost += ZMAGA//12
	ponovitve = niz.count("20222") 
	if ponovitve > 0:		
		vrednost +=ponovitve *  ZMAGA//10
	ponovitve = niz.count("22022") 
	if ponovitve > 0:		
		vrednost +=ponovitve *  ZMAGA//10
	ponovitve = niz.count("22202") 
	if ponovitve > 0:		
		vrednost +=ponovitve *  ZMAGA//10
	ponovitve = niz.count("22220") 
	if ponovitve > 0:		
		vrednost +=ponovitve *  ZMAGA//10
	ponovitve = niz.count("02222") 
	if ponovitve > 0:		
		vrednost +=ponovitve *  ZMAGA//10

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
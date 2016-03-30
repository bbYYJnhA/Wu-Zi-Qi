CRNI = 1
BELI = 2


def matrika_nicel(n, m):
	"""
	Funkcija naredi matriko n x m ni
	"""
	sez = []
	for i in range(m):
		sez += [[0]*n]
	return sez

class Igra():
	def __init__(self, gui):
		self.tabela = matrika_nicel(19,19)

		self.na_potezi = CRNI
		self.gui = gui


		
		#Mogoče, bova rabla
		self.konec = False
		self.poteze = []

	def zamenjaj(self):
		self.nasportnik()
		self.na_potezi.igraj()
	
	def razveljavi(self):
		if len(self.poteze)>0:
			(i,j) = self.poteze.pop()
			self.tabela[j][i] = 0
			self.konec = False
		else:
			assert "Seznam je prazen"
		# manjka self.igraj ....
		# izbris krozca

	def kopija(self):
		"""Vrni kopijo te igre, brez zgodovine."""
		k = Igra(self.gui)
		k.tabela = [self.tabela[i][:] for i in range(19)]
		k.na_potezi = self.na_potezi
		k.konec = self.konec
		k.igralec1 = self.igralec1
		k.igralec2 = self.igralec2
		k.poteze = self.poteze[:]
		return k

        #Ali je poteza pravilna (to metodo bo poklical Gui - self.igra.pravilna(i,j))
	def pravilna(self, i, j):
		"""Funkcija preveri ali je poteza pravilna"""
		return ((self.tabela[j][i] == 0) and not (self.konec))

	def preveri_konec(self):
		"""Funkcija ugotovi, če je tabela polna"""
		for i in self.tabela:
			if 0 in i:
				break
		else:
			self.konec = True
		
	def nasportnik(self):
		if self.na_potezi == CRNI:
			self.na_potezi = BELI
		elif self.na_potezi == BELI:
			self.na_potezi = CRNI
		else:
		#	self.na_potezi = self.igralec1
			assert False, "Neveljaven nasprotnik"
	
	def povleci_racunalnik(self, i, j):
		if self.pravilna(i,j):
			self.tabela[j][i] = self.na_potezi.barva
			self.poteze += [(i, j)]
			#self.nasportnik()
			#self.na_potezi.igraj()	
	
	def povleci(self, i, j):
		if self.pravilna(i,j):
			self.tabela[j][i] = self.na_potezi.barva
			self.poteze += [(i, j)]
			#print(self.tabela)	
			(kaj, kdo, kje) = self.preveri_zmago(i,j)
			if kaj:
				print(str(kdo.barva),str(kje))
			else:
				self.nasportnik()
				self.gui.na_potezi.igraj()

		#Ali je konec (to metodo bo poklical Gui - self.igra.preveri_konec(i,j))
	def preveri_zmago(self, j, i):
		###Pri vrstici in stolpcu lahko poljubno igraš naprej in bo računalo vedno nove zmagovalne petorke. Pri diagonali pa vrne
		###vedno prvo zmagovalno diagonalo ter barva krogca se ne spreminja.!!! (Če ustavimo igro ob zmagi, to ne bo problem!)
		"""Preveri, če je konec in vrne trojko (Bool, zmagovalec, zmagovalna petorka)"""
		dolzina = len(self.tabela)
		#Preveri vodoravno
		#Izracuna prvi in zadnji clen zmagovalne petorke
		#prvi = max(0, j-4)
		#zadnji = min(j+4, 18)
		vrstica = i
		for stolpec in range(dolzina-4):
			if self.tabela[vrstica][stolpec] != 0:
				ena = self.tabela[vrstica][stolpec]
				dva = self.tabela[vrstica][stolpec+1]
				tri = self.tabela[vrstica][stolpec+2]
				stiri = self.tabela[vrstica][stolpec+3]
				pet = self.tabela[vrstica][stolpec+4]
				#print("{0}{1}{2}{3}{4}".format(ena,dva,tri,stiri,pet))
				if ena == dva == tri == stiri == pet:
					self.konec = True
					return (True, self.na_potezi, \
							[(vrstica,stolpec),(vrstica,stolpec+1),(vrstica,stolpec+2),(vrstica,stolpec+3),(vrstica,stolpec+4)])

		# #Preveri navpično
		# #prvi = max(0, i-4)
		# #zadnji = min(i+4, 18)
		stolpec = j
		for vrstica in range(dolzina-4):
			if self.tabela[vrstica][stolpec] != 0:
					ena = self.tabela[vrstica][stolpec]
					dva = self.tabela[vrstica+1][stolpec]
					tri = self.tabela[vrstica+2][stolpec]
					stiri = self.tabela[vrstica+3][stolpec]
					pet = self.tabela[vrstica+4][stolpec]
					if ena == dva == tri == stiri == pet:
						self.konec = True
						return (True, self.na_potezi,\
							[(vrstica,stolpec),(vrstica+1,stolpec),(vrstica+2,stolpec),(vrstica+3,stolpec),(vrstica+4,stolpec)])


		for vrstica in range(4, dolzina):
			for stolpec in range(0, dolzina-4):
				if self.tabela[vrstica][stolpec] != 0:
					ena = self.tabela[vrstica][stolpec]
					dva = self.tabela[vrstica-1][stolpec+1]
					tri = self.tabela[vrstica-2][stolpec+2]
					stiri = self.tabela[vrstica-3][stolpec+3]
					pet = self.tabela[vrstica-4][stolpec+4]
					if ena == dva == tri == stiri == pet:
						self.konec = True	
						return (True, self.na_potezi,\
							[(vrstica,stolpec),(vrstica-1,stolpec+1),(vrstica-2,stolpec+2),(vrstica-3,stolpec+3),(vrstica-4,stolpec+4)])   

		for vrstica in range(0, dolzina-4):
			for stolpec in range(0, dolzina-4):
				if self.tabela[vrstica][stolpec] != 0:
					ena = self.tabela[vrstica][stolpec] 
					dva = self.tabela[vrstica+1][stolpec+1]
					tri = self.tabela[vrstica+2][stolpec+2]
					stiri = self.tabela[vrstica+3][stolpec+3]
					pet = self.tabela[vrstica+4][stolpec+4]
					if ena == dva == tri == stiri == pet:
						self.konec = True
						return (True, self.na_potezi,\
							[(vrstica,stolpec),(vrstica+1,stolpec+1),(vrstica+2,stolpec+2),(vrstica+3,stolpec+3),(vrstica+4,stolpec+4)]) 
		return (False, None, None)

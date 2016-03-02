from clovek import*

CRNI = 1
BELI = -1




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
		self.igralec1 = Clovek(self)
		self.igralec2 = Clovek(self)
		self.na_potezi = self.igralec1
		self.gui = gui
		#Mogoče, bova rabla
		self.konec = False
		self.na_potezi.igraj()
		
	# def nasportnik(self):
		# if igralec == self.igralec1:
			# return self.igralec2
		# else:
			# return self.igralec1

		#Ali je poteza pravilna (to metodo bo poklical Gui - self.igra.pravilna(i,j))
	def pravilna(self, i, j):
		return self.tabela[i][j] == 0
	
		#Ugotovi, če je tabela polna
	def preveri_konec(self):
		pass
		
	def nasportnik(self):
		if self.na_potezi == self.igralec1:
			self.na_potezi = self.igralec2
		else:
			self.na_potezi = self.igralec1
			
	def povleci(self, i, j):
		if self.pravilna(i,j):
			if self.na_potezi == self.igralec1:
				self.tabela[i][j] = CRNI
			else:
				self.tabela[i][j] = BELI
			#self.na_potezi = self.na_potezi.nasprotnik()
			if self.preveri_zmago()[0]:
				print("KONEC")
			else:
				self.nasportnik()
			
	
		#Ali je konec (to metodo bo poklical Gui - self.igra.preveri_konec(i,j))
	def preveri_zmago(self):
		#Preveri, če je konec in vrne par (Bool, zmagovalna petorka)
		##Kaj je lepše? self.tabela[vrstica][stolpec] == self.tabela[vrstica...ali ena==dva==... ?
		dolzina = len(self.tabela)
		for vrstica in range(dolzina):
			for stolpec in range(dolzina-4):
				if self.tabela[vrstica][stolpec] != 0:
					ena = self.tabela[vrstica][stolpec] 
					dva = self.tabela[vrstica][stolpec+1] 
					tri = self.tabela[vrstica][stolpec+2] 
					stiri = self.tabela[vrstica][stolpec+3] 
					pet = self.tabela[vrstica][stolpec+4]
					if ena == dva == tri == stiri == pet:
						self.konec = True	
						return (True, self.na_potezi, \
							[(vrstica,stolpec),(vrstica,stolpec+1),(vrstica,stolpec+2),(vrstica,stolpec+3),(vrstica,stolpec+4)])

		for stolpec in range(dolzina):
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

		return (False,None, None)

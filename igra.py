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

        #Ali je poteza pravilna (to metodo bo poklical Gui - self.igra.pravilna(i,j))
	def pravilna(self, i, j):
		"""Funkcija preveri ali je poteza pravilna"""
		return self.tabela[j][i] == 0
	
	def preveri_konec(self):
		"""Funkcija ugotovi, če je tabela polna"""
		pass
		
	def nasportnik(self):
		if self.na_potezi == self.igralec1:
			self.na_potezi = self.igralec2
		elif self.na_potezi == self.igralec2:
			self.na_potezi = self.igralec1
		else:
			assert False, "Neveljaven nasprotnik"
			
	def povleci(self, i, j):
		if self.pravilna(i,j):
			if self.na_potezi == self.igralec1:
				self.tabela[j][i] = CRNI
				print(self.tabela)
			else:
				self.tabela[j][i] = BELI
			#self.na_potezi = self.na_potezi.nasprotnik()
			(kaj, kdo, kje) = self.preveri_zmago(i,j)
			if kaj:
				if kdo == self.igralec1:
					print("KONEC  " + "Zmagal je CRNI" + "  " + str(kje))
				else: 
					print("KONEC  " + "Zmagal je BELI" + "  " + str(kje))
				#self.ustavi
				#self.stanje = "Zmagal je" + self.preveri_zmago()[1]
				#self.stanje ko bo igra izenačena
			else:
				self.nasportnik()

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

		# #Preveri navpčno
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

		#Preveri prvo diagonalo
		# diag = j-i
		# for vrstica in range(15):
		# 	if (vrstica - diag < 15) and (vrstica - diag >= 0) and (self.tabela[vrstica][vrstica - diag] != 0):
		# 		ena = self.tabela[vrstica][vrstica - diag]
		# 		dva = self.tabela[vrstica+1][vrstica - diag +1]
		# 		tri = self.tabela[vrstica+2][vrstica - diag + 2]
		# 		stiri = self.tabela[vrstica+3][vrstica - diag + 3]
		# 		pet = self.tabela[vrstica+4][vrstica - diag + 4]
		# 		if ena == dva == tri == stiri == pet:
		# 			self.konec = True
		# 			return (True, self.na_potezi,\
		# 				[(vrstica,vrstica - diag),(vrstica+1,vrstica - diag +1),(vrstica+2,vrstica - diag +2),(vrstica+3,vrstica - diag +3),(vrstica+4,vrstica - diag +4)])

		# #Preveri drugo diagonalo
		# diag = i+j
		# for vrstica in range(15):
		# 	if (diag - vrstica < 15) and (diag - vrstica >= 0) and (self.tabela[vrstica][diag - vrstica] != 0):
		# 		ena = self.tabela[vrstica][diag - vrstica]
		# 		dva = self.tabela[vrstica+1][diag - vrstica +1]
		# 		tri = self.tabela[vrstica+2][diag - vrstica + 2]
		# 		stiri = self.tabela[vrstica+3][diag - vrstica + 3]
		# 		pet = self.tabela[vrstica+4][diag - vrstica + 4]
		# 		if ena == dva == tri == stiri == pet:
		# 			self.konec = True
		# 			return (True, self.na_potezi,\
		# 				[(vrstica,diag - vrstica),(vrstica+1,diag - vrstica +1),(vrstica+2,diag - vrstica +2),(vrstica+3,diag - vrstica +3),(vrstica+4,diag - vrstica +4)])


		# return (False, None, None)

		# for vrstica in range(dolzina):
		# 	for stolpec in range(dolzina-4):
		# 		if self.tabela[vrstica][stolpec] != 0:
		# 			ena = self.tabela[vrstica][stolpec] 
		# 			dva = self.tabela[vrstica][stolpec+1] 
		# 			tri = self.tabela[vrstica][stolpec+2] 
		# 			stiri = self.tabela[vrstica][stolpec+3] 
		# 			pet = self.tabela[vrstica][stolpec+4]
		# 			if ena == dva == tri == stiri == pet:
		# 				self.konec = True
		# 				# Kaj če je 6 ali več v vrsto??? V sezamu je le 5 elementov.
		# 				# Dovolj je vrniti le začetno in končno potezo ujemanja
		# 				return (True, self.na_potezi, \
		# 					[(vrstica,stolpec),(vrstica,stolpec+1),(vrstica,stolpec+2),(vrstica,stolpec+3),(vrstica,stolpec+4)])

		# for stolpec in range(dolzina):
		# 	for vrstica in range(dolzina-4):
		# 		if self.tabela[vrstica][stolpec] != 0:
		# 			ena = self.tabela[vrstica][stolpec]
		# 			dva = self.tabela[vrstica+1][stolpec]
		# 			tri = self.tabela[vrstica+2][stolpec]
		# 			stiri = self.tabela[vrstica+3][stolpec]
		# 			pet = self.tabela[vrstica+4][stolpec]
		# 			if ena == dva == tri == stiri == pet:
		# 				self.konec = True	
		# 				return (True, self.na_potezi,\
		# 					[(vrstica,stolpec),(vrstica+1,stolpec),(vrstica+2,stolpec),(vrstica+3,stolpec),(vrstica+4,stolpec)])     

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
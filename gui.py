import tkinter
from igra import*
from clovek import*

class Gui():

	def __init__(self, master):
		#Potrebno je popraviti rob plošče in dodati dodatne gumbe
		#gumbe je potrebno spraviti tudi v delovanje
		self.napis1 = tkinter.StringVar(master, value="Dobrodošli v 五子棋")
		tkinter.Label(master, textvariable=self.napis1).grid(row=0, column=0)

		#tukaj bi raje dodal napis self.napis
		self.napis2 = tkinter.StringVar(master, value="Na potezi je črni")
		tkinter.Label(master, textvariable=self.napis2).grid(row=42, column=0)

		self.plosca = tkinter.Canvas(master, width=648, height=648, bg = "green", borderwidth=0)
		self.plosca.grid(row=1, column=0, columnspan=1, rowspan=41)
		
		self.gumb1 = tkinter.Button(master, text="Nova igra", command=self.koncaj_igro)
		self.gumb1.grid(row=1, column=1)
		# gumn, ki razveljavi potezo ...

		self.gumb2 = tkinter.Button(master, text="Razveljavi", command=self.razveljavi_gumb)
		self.gumb2.grid(row=2, column=1)

		self.gumb3 = tkinter.Button(master, text="Računalnik črni", command=self.rac_crni)
		self.gumb3.grid(row=3, column=1)

		self.gumb4 = tkinter.Button(master, text="Računalnik beli", command=self.rac_beli)
		self.gumb4.grid(row=4, column=1)

		#!!! manjkata dve črti !!!
		for i in range(18):
			self.plosca.create_line(i*36, 0, i*36, 648)
			self.plosca.create_line(0, i*36, 648, i*36)
			#self.izbira_igralcev()

		self.igra = Igra(self)
		self.igra.na_potezi.igraj()

	def rac_crni(self):
		self.igra.igralec1 = Racunalnik(self)
		self.igra.na_potezi.igraj()
	def rac_beli(self):
		self.igra.igralec2 = Racunalnik(self)
		self.igra.na_potezi.igraj()
	def razveljavi_gumb(self):
		self.igra.razveljavi
		self.napis2.set("Razveljavitev gotovo ni grafično podprta")

	def narisi1(self, i, j):
		x = i * 36
		y = j * 36
		self.plosca.create_oval(x - 18, y - 18, x + 18, y + 18, fill="black")
	def narisi2(self, i, j):
		x = i * 36
		y = j * 36
		self.plosca.create_oval(x - 18, y - 18, x + 18, y + 18, fill="white")     

	def narisi_crto(self, kje):
		(y0, x0) = kje[0]
		(y1, x1) = kje[4]
		self.plosca.create_line(x0 * 36, y0 * 36, x1 * 36, y1 * 36, fill="red", width="3")


	def koncaj_igro(self):
		aplikacija = Gui(root)
		self.igra = Igra(self)
		self.igra.na_potezi.igraj()

	def povleci_potezo(self, i, j):
		if self.igra.pravilna(i, j):
			if self.igra.na_potezi == self.igra.igralec1:
				self.narisi1(i, j)
				self.napis2.set("Na potezi je beli")
			else:
				self.narisi2(i, j)
				self.napis2.set("Na potezi je črni")
			self.igra.povleci(i, j)
		#else:
		#	self.napis2.set("Igra je končana")

if __name__ == "__main__":
	# Naredimo glavno okno in nastavimo ime
	root = tkinter.Tk()
	root.title("五子棋")
	
	# Naredimo objekt razreda Gui in ga spravimo v spremenljivko,
	# sicer bo Python mislil, da je objekt neuporabljen in ga bo pobrisal
	# iz pomnilnika.
	aplikacija = Gui(root)
	# Kontrolo prepustimo glavnemu oknu. Funkcija mainloop neha
	# delovati, ko okno zapremo.
	root.mainloop()        

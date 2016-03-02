import tkinter
from igra import*
from clovek import*

#igralec1 = 1
#igralec2 = -1

neodloceno = None

class Gui():
	
	def __init__(self, master):
		self.napis1 = tkinter.StringVar(master, value="Dobrodošli v 五子棋")
		tkinter.Label(master, textvariable=self.napis1).grid(row=0, column=0)

		self.napis2 = tkinter.StringVar(master, value="igrate 5 v vrsto")
		tkinter.Label(master, textvariable=self.napis2).grid(row=2, column=0)


		self.plosca = tkinter.Canvas(master, width=648, height=648, bg = "green")
		self.plosca.grid(row=1, column=0)
		
		self.gumb1 = tkinter.Button(master, text="Nova igra")
		self.gumb1.grid(row=1, column=1)

		for i in range(18):
			self.plosca.create_line(i*36, 0, i*36, 684)
			self.plosca.create_line(0, i*36, 684, i*36)
			#self.izbira_igralcev()

		self.igra = Igra(self)

	def narisi1(self, i, j):
		x = i * 36
		y = j * 36
		self.plosca.create_oval(x - 18, y - 18, x + 18, y + 18, fill="black")
	def narisi2(self, i, j):
		x = i * 36
		y = j * 36
		self.plosca.create_oval(x - 18, y - 18, x + 18, y + 18, fill="white")     
	def koncaj_igro(self):
		print("Konec")
	def povleci_potezo(self, i, j):
		if self.igra.pravilna(i, j):
			if self.igra.na_potezi == self.igra.igralec1:
				self.narisi1(i, j)
			else:
				self.narisi2(i, j)
			self.igra.povleci(i, j)


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

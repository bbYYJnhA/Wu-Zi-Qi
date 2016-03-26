class Clovek():
	def __init__(self, igra, barva, tezavnost=None):
		self.igra = igra
		self.barva = barva
        
	def igraj(self):
		self.igra.gui.plosca.bind('<Button-1>', self.klik)

	def prekini(self):
		pass

	def klik(self, event):
		i = (event.x+18) // 36
		j = (event.y+18) // 36
		self.igra.gui.povleci_potezo(i, j)
		#self.igra.zamenjaj()
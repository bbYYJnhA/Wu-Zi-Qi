import random
globina = 1

class Racunalnik():
	def __init__(self, igra, tezavnost=None):
		self.igra = igra


	def prekini(self):
		pass
    
	
	def igraj(self):
		a = 10
		b = 10
		while not (self.igra.pravilna(a,b)):
			a = random.randrange(0,19)
			b = random.randrange(0,19)
		self.igra.gui.povleci_potezo(a,b)
    
	def klik(self, event):
		pass

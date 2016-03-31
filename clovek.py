class Clovek():
    def __init__(self, gui, barva, tezavnost=None):
        self.gui = gui
        self.barva = barva
        
    def igraj(self):
        pass
        #self.igra.gui.plosca.bind('<Button-1>', self.klik)

    def prekini(self):
        pass

    def klik(self, i, j):
        if not self.gui.konec:
            self.gui.povleci_potezo(i, j)
class Clovek():
    def __init__(self, gui, racunalnik, tezavnost=None):
        self.gui = gui
        
    def igraj(self):
        pass


    def prekini(self):
        pass

    def klik(self, x, y):
        """Metoda posreduje koordinate, ki jih je dobila s klikom na platno, gui-ju, da povlece potezo."""
        if not self.gui.konec:
            self.gui.povleci_potezo(x, y)
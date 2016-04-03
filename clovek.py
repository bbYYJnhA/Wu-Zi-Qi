class Clovek():
    def __init__(self, gui, racunalnik, tezavnost=None):
        self.gui = gui
        
    def igraj(self):
        """Funkcija ne dela nič in je tu zgolj zaradi formalnosti."""
        pass

    def prekini(self):
        """Človek bo že sam vedel, kdaj mora nehati igrati."""
        pass

    def klik(self, x, y):
        """Metoda posreduje koordinate, ki jih je dobila s klikom na platno, GUI-ju, da povleče potezo."""
        if not self.gui.konec:
            self.gui.povleci_potezo(x, y)

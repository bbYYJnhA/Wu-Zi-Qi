class Clovek():
    def __init__(self, gui, racunalnik, barva, tezavnost=None):
        self.gui = gui
        self.barva = barva
        
    def igraj(self):
        """Funkcija ne dela nil in je tu zgolj zaradi formalnosti"""
        pass

    def prekini(self):
        """Človek bo že sam vedel kdaj mora nehati igrati"""
        pass

    def klik(self, x, y):
        """Funkcija požene funkcijo, ki nariše potezo na željo 
        uporabnika, če je seveda poteza veljavna."""
        if not self.gui.konec:
            self.gui.povleci_potezo(x, y)
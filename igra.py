CRNI = 1
BELI = 2


def matrika_nicel(n, m):
    """
    Funkcija naredi matriko n x m ni
    """
    sez = []
    for i in range(m):
        sez += [[0]*n]
    return sez

class Igra():
    """Razred vsebuje atribute self.tabela - matrika, kjer se shranjuje stanje igre; self.na_potezi - igralca, ki je na potezi (privzet
        je prvi igralec - črni); self.konec - ali je konec igre (privzeto na False); self.poteze - seznam odigranih potez vsebuje pare
        (i,j), ki sta koordinati v matriki self.tabela; self.gui - dostop do grafičnega umesnika, ki ga dobi kot parameter."""
    def __init__(self, gui):
        self.tabela = matrika_nicel(19,19)
        self.na_potezi = CRNI
        self.gui = gui
        self.konec = False
        self.poteze = []

    def razveljavi(self):
        """Metoda izbriše zadnjo potezo iz seznama self.poteze in nastavi odigrano polje na prazno."""
        if len(self.poteze)>0:
            (i,j) = self.poteze.pop()
            self.tabela[j][i] = 0
            self.konec = False
        else:
            assert "Seznam je prazen"


    def kopija(self):
        """Vrne kopijo te igre, brez zgodovine."""
        k = Igra(self.gui)
        k.tabela = [self.tabela[i][:] for i in range(19)]
        k.na_potezi = self.na_potezi
        k.konec = self.konec
        k.poteze = self.poteze[:]
        return k

    def pravilna(self, i, j):
        """Funkcija preveri ali je poteza pravilna."""
        return ((self.tabela[j][i] == 0) and not (self.konec))

    def preveri_konec(self):
        """Funkcija ugotovi, če je tabela polna."""
        for i in self.tabela:
            if 0 in i:
                break
        else:
            self.konec = True
        
    def nasprotnik(self):
        """Metoda nastavi self.na_potezi na nasprotnika."""
        if self.na_potezi == CRNI:
            self.na_potezi = BELI
        elif self.na_potezi == BELI:
            self.na_potezi = CRNI
        else:
            assert False, "Neveljaven nasprotnik"
    
    def povleci_racunalnik(self, i, j):
        """V tabelo vstavi figuro trenutnega igralca in potezo shrani v self.poteze."""
        if self.pravilna(i,j):
            self.tabela[j][i] = self.na_potezi
            self.poteze += [(i, j)]

    
    def povleci(self, i, j):
        if self.pravilna(i,j):
            self.tabela[j][i] = self.na_potezi
            self.poteze += [(i, j)]
            #print(self.tabela) 
            self.nasprotnik()
            #   self.gui.na_potezi.igraj()

        #Ali je konec (to metodo bo poklical Gui - self.igra.preveri_konec(i,j))
    

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
    def __init__(self, gui):
        self.tabela = matrika_nicel(19,19)

        self.na_potezi = CRNI
        self.gui = gui


        
        #Mogoče, bova rabla
        self.konec = False
        self.poteze = []

    def razveljavi(self):
        if len(self.poteze)>0:
            (i,j) = self.poteze.pop()
            self.tabela[j][i] = 0
            self.konec = False
        else:
            assert "Seznam je prazen"
        # manjka self.igraj ....
        # izbris krozca

    def kopija(self):
        """Vrni kopijo te igre, brez zgodovine."""
        k = Igra(self.gui)
        k.tabela = [self.tabela[i][:] for i in range(19)]
        k.na_potezi = self.na_potezi
        k.konec = self.konec
        k.poteze = self.poteze[:]
        return k

        #Ali je poteza pravilna (to metodo bo poklical Gui - self.igra.pravilna(i,j))
    def pravilna(self, i, j):
        """Funkcija preveri ali je poteza pravilna"""
        return ((self.tabela[j][i] == 0) and not (self.konec))

    def preveri_konec(self):
        """Funkcija ugotovi, če je tabela polna"""
        for i in self.tabela:
            if 0 in i:
                break
        else:
            self.konec = True
        
    def nasprotnik(self):
        if self.na_potezi == CRNI:
            self.na_potezi = BELI
        elif self.na_potezi == BELI:
            self.na_potezi = CRNI
        else:
        #   self.na_potezi = self.igralec1
            assert False, "Neveljaven nasprotnik"
    
    def povleci_racunalnik(self, i, j):
        if self.pravilna(i,j):
            self.tabela[j][i] = self.na_potezi
            print(self.tabela)
            self.poteze += [(i, j)]
            #self.nasportnik()
            #self.na_potezi.igraj() 
    
    def povleci(self, i, j):
        if self.pravilna(i,j):
            self.tabela[j][i] = self.na_potezi
            self.poteze += [(i, j)]
            #print(self.tabela) 
            self.nasprotnik()
            #   self.gui.na_potezi.igraj()

        #Ali je konec (to metodo bo poklical Gui - self.igra.preveri_konec(i,j))
    

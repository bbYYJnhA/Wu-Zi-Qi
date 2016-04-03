import threading
import random
import numpy as np


CRNI = 1
BELI = 2

def smiselne_pozicije(neki_seznam):
    """Funkcija izračuna smiselne poteze in sicer +-1 za vsako že postavljeno figuro. Računalnik pri razmišlajanju
    preveri le te možnosti."""
    sez = set()
    for (i, j) in neki_seznam:
        if i+1 <= 18:
            sez.add((i + 1, j))
        if i+1 <= 18 and j-1>0:
            sez.add((i + 1, j - 1))         
        if j+1 <= 18:
            sez.add((i, j + 1))
        if j+1 <= 18 and i-1>0:
            sez.add((i - 1, j + 1))
        if j+1 <= 18 and i+1 <=18:
            sez.add((i + 1, j + 1))
        if i-1>0 and j-1>0:
            sez.add((i - 1, j - 1))
        if i-1>0:
            sez.add((i - 1, j))
        if j-1>0:
            sez.add((i, j - 1))
    return list(sez)

def drug_igralec(igralec):
    """Zamenja igralca, ki je na potezi. To funkcijo uporablja alfabeta."""
    if igralec == CRNI:
        return BELI
    elif igralec == BELI:
        return CRNI
    else:
        assert False, "Napačen igralec v drug_igralec"
    
##################################################################################################################################
class Racunalnik():
    def __init__(self, gui, algoritem):
        self.gui = gui
        self.algoritem = algoritem
        self.mislec = None


    def igraj(self):
        """Požene vlakno in vsakih 100 ms preveri, če je poteza že izračunana."""
        self.mislec = threading.Thread(target=lambda: self.algoritem.izracunaj_potezo(self.gui.igra.kopija()))
        self.mislec.start()
        self.gui.plosca.after(100, self.preveri_potezo)

    def preveri_potezo(self):
        """Če je bila poteza izračunana, jo vrne, sicer čaka."""
        if self.algoritem.poteza is not None:
            (i, j) = self.algoritem.poteza
            self.gui.povleci_potezo(i+1, j+1)
            self.mislec = None
        else:
            self.gui.plosca.after(100, self.preveri_potezo)

    def prekini(self):
        """Prekine igro. Računalniku sporoči, naj ustavi thread."""
        if self.mislec:
            self.algoritem.prekini()
            self.mislec.join()
            self.mislec = None

    def klik(self, i, j):
        """Računalnik ne klika, zato je ta funkcija tu zgolj zaradi formalnosti."""
        pass
#################################################################################################################################
class Alfabeta():
    def __init__(self, globina):
        self.igra = None
        self.prekinitev = False
        self.globina = globina
        self.poteza = None

    def prekini(self):
        """Če uporabnik zahteva prekinitev, se atribut self.prekinitev nastavi na True."""
        self.prekinitev = True

    def izracunaj_potezo(self, igra):
        """Algoritem s to metodo izračuna optimalno potezo za dano globino."""
        self.igra = igra
        self.prekinitev = False
        self.jaz = self.igra.na_potezi
        self.poteza = None
        (poteza, vrednost) = self.alfabeta(self.globina, -10000000000, 10000000000,True, self.jaz)
        self.jaz = None
        self.igra = None
        if not self.prekinitev:
            self.poteza = poteza

################################################################################################################################            
# HEVRISTIKA

    def vrednost_skupaj(self, tabela):
        """Metoda oceni vrednost pozicije."""
        ZMAGA = 1000000
        
        def crni(niz):
            """Vrne vrednost črnih figur na igralnem polju."""
            crni_boljsi = ["01110", "0110", "010", "211101", "011010", "010110"]
            crni_slabsi = ["211110", "011112", "101112", "211011", "110112", "21110", "01112", "2110", "0112", "210", "012"]
            
            #Prvi in zadnji element nastavi za nasprotnikove figure, da lahko primerja z elementi iz seznama
            niz = "2" + niz + "2"
            vrednost = 0
            if self.jaz == BELI:
                if niz.count("11111") > 0:
                    vrednost += ZMAGA
                    return vrednost
                elif niz.count("011110") > 0:
                    vrednost += ZMAGA//2
                elif niz.count("10111") > 0:        
                    vrednost += ZMAGA//5
                elif niz.count("11011") > 0:        
                    vrednost += ZMAGA//5
                elif niz.count("11101") > 0:        
                    vrednost += ZMAGA//5
                elif niz.count("11110") > 0:        
                    vrednost += ZMAGA//5
                elif niz.count("01111") > 0:        
                    vrednost += ZMAGA//5
                elif niz.count("01110") > 0:        
                    vrednost += ZMAGA//12
                
                for el in crni_boljsi:
                    dolzina = len(el)
                    ponavljanja = niz.count(el)
                    ugodne = el.count("1")
                    vrednost += ponavljanja * 4**ugodne
                for el in crni_slabsi:
                    dolzina = len(el)
                    ponavljanja = niz.count(el)
                    ugodne = el.count("1")
                    vrednost += ponavljanja * 3**ugodne
            else:
                if niz.count("11111") > 0:
                    vrednost += ZMAGA//2
                    return vrednost
                elif niz.count("011110") > 0:
                    vrednost += ZMAGA//5
                elif niz.count("10111") > 0:        
                    vrednost += ZMAGA//10
                elif niz.count("11011") > 0:        
                    vrednost += ZMAGA//10
                elif niz.count("11101") > 0:        
                    vrednost += ZMAGA//10
                elif niz.count("11110") > 0:        
                    vrednost += ZMAGA//10
                elif niz.count("01111") > 0:        
                    vrednost += ZMAGA//10
                
                for el in crni_boljsi:
                    dolzina = len(el)
                    ponavljanja = niz.count(el)
                    ugodne = el.count("1")
                    vrednost += ponavljanja * 3**ugodne
                for el in crni_slabsi:
                    dolzina = len(el)
                    ponavljanja = niz.count(el)
                    ugodne = el.count("1")
                    vrednost += ponavljanja * 4**ugodne
                

            return vrednost




        def beli(niz):
            """Vrne vrednost belih figur na igralnem polju."""
            beli_boljsi = ["02220", "0220", "020", "122202", "022020", "020220"]
            beli_slabsi = ["122220", "022221", "202221", "122022", "220221" "12220", "02221", "1220", "0221", "120", "021"]
            
            #Prvi in zadnji element nastavi za nasprotnikove figure, da lahko primerja z elementi iz seznama
            niz = "1" + niz + "1"
            vrednost = 0
            if self.jaz == BELI:
                if niz.count("22222") > 0:
                    vrednost += ZMAGA//2
                    return vrednost     
                elif niz.count("022220") > 0:
                    vrednost += ZMAGA//5
                elif niz.count("20222") > 0:        
                    vrednost += ZMAGA//10
                elif niz.count("22022") > 0:        
                    vrednost += ZMAGA//10
                elif niz.count("22202") > 0:        
                    vrednost += ZMAGA//10
                elif niz.count("22220") > 0:        
                    vrednost += ZMAGA//10
                elif niz.count("02222") > 0:        
                    vrednost += ZMAGA//10
                
                for el in beli_slabsi:
                    dolzina = len(el)
                    ponavljanja = niz.count(el)
                    ugodne = el.count("2")
                    vrednost += ponavljanja * 4**ugodne
                for el in beli_boljsi:
                    dolzina = len(el)
                    ponavljanja = niz.count(el)
                    ugodne = el.count("2")
                    vrednost += ponavljanja * 3**ugodne
            else:
                if niz.count("22222") > 0:
                    vrednost += ZMAGA
                    return vrednost     
                elif niz.count("022220") > 0:
                    vrednost += ZMAGA//5
                elif niz.count("20222") > 0:        
                    vrednost += ZMAGA//5
                elif niz.count("22022") > 0:        
                    vrednost += ZMAGA//5
                elif niz.count("22202") > 0:        
                    vrednost += ZMAGA//5
                elif niz.count("22220") > 0:        
                    vrednost += ZMAGA//5
                elif niz.count("02222") > 0:        
                    vrednost += ZMAGA//5
                elif niz.count("02220") >0:
                    vrednost += ZMAGA//12
                
                for el in beli_slabsi:
                    dolzina = len(el)
                    ponavljanja = niz.count(el)
                    ugodne = el.count("2")
                    vrednost += ponavljanja * 3**ugodne
                for el in beli_boljsi:
                    dolzina = len(el)
                    ponavljanja = niz.count(el)
                    ugodne = el.count("2")
                    vrednost += ponavljanja * 4**ugodne

            return vrednost

        def vrednost_vrstic(tabela):
            """Vrne vrednost vrstic v tabeli."""
            rezultat = 0
            for vrstica in tabela:
                nizek = ""
                for znak in vrstica:
                    nizek += str(znak)
                rezultat += crni(nizek) - beli(nizek)
            return rezultat

        def vrednost_stolpcev(tabela):
            """Vrne vrednost stolpcev v tabeli."""
            stolpci = [list(x) for x in zip(*tabela)]
            return vrednost_vrstic(stolpci)

        def vse_diagonale(tabela):
            """Naredi seznam vseh diagonal."""
            matrika1 = np.array(tabela)
            diagonale = []
            dolzina = len(tabela)
            #Le diagonale, ki so dolžine vsaj 5
            for i in range(5-dolzina, dolzina-4):
                diagonale.append(list(matrika1.diagonal(i)))
                diagonale.append(list(np.fliplr(matrika1).diagonal(i)))
            

            return diagonale

        def vrednost_diagonal(tabela):
            """Vrne vrednost diagonal v tabeli."""
            return vrednost_vrstic(vse_diagonale(tabela))

        if self.jaz == CRNI:
            return vrednost_vrstic(tabela) + vrednost_stolpcev(tabela) + vrednost_diagonal(tabela)
        elif self.igra.na_potezi == BELI:
            return -(vrednost_vrstic(tabela) + vrednost_stolpcev(tabela) + vrednost_diagonal(tabela))
        else:
            assert False, "Napačna v vrednost_skupaj"
##################################################################################################################################
    
    def alfabeta(self, globina, alfa, beta, maksimiziramo, trenutni):
        """Algoritem izračuna optimalno potezo za dano globino."""
        if self.prekinitev:
            return (None, 0)

        if self.igra.konec:
            if trenutni == CRNI:
                return (None, 10000000000)
            elif trenutni == BELI:
                return (None, -10000000000)
            else:
                return (None, 0)
        if len(self.igra.poteze) == 0:
            return ((9,9), 10000000000)
        if globina == 0:
            return (None, self.vrednost_skupaj(self.igra.tabela))
        if maksimiziramo:
            najpoteza = None
            vrednostnajpoteze = -10000000000
            for (iv, ist) in smiselne_pozicije(self.igra.poteze):
                if self.igra.tabela[ist][iv] == 0:
                    self.igra.povleci_racunalnik(iv, ist)
                    vr1 = self.alfabeta(globina-1, alfa, beta, not maksimiziramo, drug_igralec(trenutni))[1]
                    self.igra.razveljavi()
                    if vr1 > vrednostnajpoteze:
                        vrednostnajpoteze = vr1
                        najpoteza = (iv, ist)
                    if vr1 > alfa:
                        alfa = vr1
                    if beta <= alfa:
                        break
        else:
            najpoteza = None
            vrednostnajpoteze = 10000000000
            for (iv, ist) in smiselne_pozicije(self.igra.poteze):
                if self.igra.tabela[ist][iv] == 0:
                    self.igra.povleci_racunalnik(iv, ist)
                    vr1 = self.alfabeta(globina-1, alfa, beta, not maksimiziramo, drug_igralec(trenutni))[1]
                    self.igra.razveljavi()
                    if vr1 < vrednostnajpoteze:
                        vrednostnajpoteze = vr1
                        najpoteza = (iv, ist)
                    if vr1 < beta:
                        beta = vr1
                    if beta <= alfa:
                        break
        assert (najpoteza is not None), "alfabeta: izračunana poteza je None"
        return (najpoteza, vrednostnajpoteze)





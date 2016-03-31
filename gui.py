import tkinter
from tkinter import ttk
from igra import*
from clovek import*
from racunalnik import*

def sporocilo(msg, naslov):
    popup = tkinter.Tk()
    popup.wm_title(naslov)
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=20)
    popup.mainloop()

class Gui():

    def __init__(self, master):
        self.igra = Igra(self)
        
        self.igralec1 = Clovek(self, CRNI)
        self.igralec2 = Racunalnik(self, Alfabeta(2), BELI)#Clovek(self,BELI)
        self.klik = None
        self.konec = False
        self.igralec1.igraj()
        #Potrebno je popraviti rob plošče in dodati dodatne gumbe
        #gumbe je potrebno spraviti tudi v delovanje
        self.napis1 = tkinter.StringVar(master, value="Dobrodošli v 五子棋")
        tkinter.Label(master, textvariable=self.napis1).grid(row=0, column=0)

        #tukaj bi raje dodal napis self.napis
        self.napis2 = tkinter.StringVar(master, value="Na potezi je črni")
        tkinter.Label(master, textvariable=self.napis2).grid(row=42, column=0)

        self.plosca = tkinter.Canvas(master, width=648+36, height=648+36, bg = "green", borderwidth=0)
        self.plosca.grid(row=1, column=0, columnspan=1, rowspan=41)
        
        self.gumb1 = tkinter.Button(master, text="Nova igra", command=self.koncaj_igro)
        self.gumb1.grid(row=1, column=1)
        
        self.plosca.bind('<Button-1>', self.klik_plosca)



        #!!! manjkata dve črti !!!
        for i in range(18):
            self.plosca.create_line(i*36+36, 0+36, i*36+36, 648)
            self.plosca.create_line(0+36, i*36+36, 648, i*36+36)


    def klik_plosca(self, event):
        i = (event.x+18) // 36
        j = (event.y+18) // 36
        if i > 0 and j > 0 and i < 19 and j < 19:
            if self.igra.na_potezi == CRNI:
                self.igralec1.klik(i, j)
            elif self.igra.na_potezi == BELI:
                self.igralec2.klik(i, j)
            else:
                assert False, "Neveljaven igralec klik"
            
    def narisi1(self, i, j):
        x = i * 36
        y = j * 36
        self.plosca.create_oval(x - 18, y - 18, x + 18, y + 18, fill="black")
        
    def narisi2(self, i, j):
        x = i * 36
        y = j * 36
        self.plosca.create_oval(x - 18, y - 18, x + 18, y + 18, fill="white")     

    def narisi_crto(self, kje):
        (y0, x0) = kje[0]
        (y1, x1) = kje[4]
        self.plosca.create_line(x0 * 36, y0 * 36, x1 * 36, y1 * 36, fill="red", width="3")

    def konec_igre_okno(self):
        tkinter.messagebox("Say Hello", "Hello World")  

    def koncaj_igro(self):
        aplikacija = Gui(root)
        self.igra = Igra(self)
        self.igralec1 = Clovek(self, CRNI)
        self.igralec2 = Racunalnik(self, Alfabeta(2), BELI)

    def preveri_zmago(self, j, i):
        ###Pri vrstici in stolpcu lahko poljubno igraš naprej in bo računalo vedno nove zmagovalne petorke. Pri diagonali pa vrne
        ###vedno prvo zmagovalno diagonalo ter barva krogca se ne spreminja.!!! (Če ustavimo igro ob zmagi, to ne bo problem!)
        """Preveri, če je konec in vrne trojko (Bool, zmagovalec, zmagovalna petorka)"""
        dolzina = len(self.igra.tabela)
        #Preveri vodoravno
        #Izracuna prvi in zadnji clen zmagovalne petorke
        #prvi = max(0, j-4)
        #zadnji = min(j+4, 18)
        vrstica = i
        for stolpec in range(dolzina-4):
            if self.igra.tabela[vrstica][stolpec] != 0:
                ena = self.igra.tabela[vrstica][stolpec]
                dva = self.igra.tabela[vrstica][stolpec+1]
                tri = self.igra.tabela[vrstica][stolpec+2]
                stiri = self.igra.tabela[vrstica][stolpec+3]
                pet = self.igra.tabela[vrstica][stolpec+4]
                #print("{0}{1}{2}{3}{4}".format(ena,dva,tri,stiri,pet))
                if ena == dva == tri == stiri == pet:
                    self.konec = True
                    return (True, self.igra.na_potezi, \
                            [(vrstica,stolpec),(vrstica,stolpec+1),(vrstica,stolpec+2),(vrstica,stolpec+3),(vrstica,stolpec+4)])

        # #Preveri navpično
        # #prvi = max(0, i-4)
        # #zadnji = min(i+4, 18)
        stolpec = j
        for vrstica in range(dolzina-4):
            if self.igra.tabela[vrstica][stolpec] != 0:
                    ena = self.igra.tabela[vrstica][stolpec]
                    dva = self.igra.tabela[vrstica+1][stolpec]
                    tri = self.igra.tabela[vrstica+2][stolpec]
                    stiri = self.igra.tabela[vrstica+3][stolpec]
                    pet = self.igra.tabela[vrstica+4][stolpec]
                    if ena == dva == tri == stiri == pet:
                        self.konec = True
                        return (True, self.igra.na_potezi,\
                            [(vrstica,stolpec),(vrstica+1,stolpec),(vrstica+2,stolpec),(vrstica+3,stolpec),(vrstica+4,stolpec)])


        for vrstica in range(4, dolzina):
            for stolpec in range(0, dolzina-4):
                if self.igra.tabela[vrstica][stolpec] != 0:
                    ena = self.igra.tabela[vrstica][stolpec]
                    dva = self.igra.tabela[vrstica-1][stolpec+1]
                    tri = self.igra.tabela[vrstica-2][stolpec+2]
                    stiri = self.igra.tabela[vrstica-3][stolpec+3]
                    pet = self.igra.tabela[vrstica-4][stolpec+4]
                    if ena == dva == tri == stiri == pet:
                        self.konec = True   
                        return (True, self.igra.na_potezi,\
                            [(vrstica,stolpec),(vrstica-1,stolpec+1),(vrstica-2,stolpec+2),(vrstica-3,stolpec+3),(vrstica-4,stolpec+4)])   

        for vrstica in range(0, dolzina-4):
            for stolpec in range(0, dolzina-4):
                if self.igra.tabela[vrstica][stolpec] != 0:
                    ena = self.igra.tabela[vrstica][stolpec] 
                    dva = self.igra.tabela[vrstica+1][stolpec+1]
                    tri = self.igra.tabela[vrstica+2][stolpec+2]
                    stiri = self.igra.tabela[vrstica+3][stolpec+3]
                    pet = self.igra.tabela[vrstica+4][stolpec+4]
                    if ena == dva == tri == stiri == pet:
                        self.konec = True
                        return (True, self.igra.na_potezi,\
                            [(vrstica,stolpec),(vrstica+1,stolpec+1),(vrstica+2,stolpec+2),(vrstica+3,stolpec+3),(vrstica+4,stolpec+4)]) 
        return (False, None, None)
        
    def povleci_potezo(self, i, j):
        if self.igra.pravilna(i, j):
            trenutni = self.igra.na_potezi
            if self.igra.na_potezi == CRNI:
                self.narisi1(i, j)              
                self.igra.povleci(i, j)
                (kaj, kdo, kje) = self.preveri_zmago(i,j)
                if kaj:
                    self.narisi_crto(kje)
                    self.konec = True
                    self.napis2.set("Zmagal je ČRNI")
                    sporocilo("     Zmagal je ČRNI     ", "Igre je konec")
                    print(str(kdo))
                else:
                    self.napis2.set("Na potezi je beli")
                    self.igralec2.igraj()
            elif self.igra.na_potezi == BELI:
                self.narisi2(i, j)              
                self.igra.povleci(i, j)
                (kaj, kdo, kje) = self.preveri_zmago(i,j)
                if kaj:
                    self.narisi_crto(kje)
                    self.konec = True
                    self.napis2.set("Zmagal je BELI")
                    sporocilo("     Zmagal je BELI     ", "Igre je konec")
                    print(str(kdo))
                else:
                    self.napis2.set("Na potezi je črni")
                    self.igralec1.igraj()
            else:
                assert False, "Neveljaven igralec poskuša povlect potezo."
            
        #else:
        #   self.napis2.set("Igra je končana")

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

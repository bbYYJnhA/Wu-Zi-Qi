import tkinter as tk
from igra import*
from clovek import*
from racunalnik import*

class Gui():

    def __init__(self, master):
        self.igra = Igra(self)
        
        self.napis1 = tk.StringVar(master, value="Dobrodošli v 5 v vrsto")
        tk.Label(master, textvariable=self.napis1).grid(row=0, column=0)

        self.napis2 = tk.StringVar(master, value="Na potezi je črni")
        tk.Label(master, textvariable=self.napis2).grid(row=42, column=0)

        self.plosca = tk.Canvas(master, width=648+36+36, height=648+36+36, bg = "lightblue", borderwidth=0)
        self.plosca.grid(row=1, column=0, columnspan=1, rowspan=41)

        self.gumb1 = tk.Button(master, text="Nova igra", command=self.nova_igra_gumb)
        self.gumb1.grid(row=1, column=1)

        self.plosca.bind('<Button-1>', self.klik_plosca)
        
        # Glavni meni
        menu = tk.Menu(master)
        master.config(menu=menu)

        # Podmeni Igra
        menu_igra = tk.Menu(menu)
        menu.add_cascade(label="Igra", menu=menu_igra)
        menu_igra.add_command(label="Nova igra", command=self.nova_igra_gumb)
        menu_igra.add_command(label="Izhod", command=master.destroy)

        # Podmeni pomoč
        menu_pomoc = tk.Menu(menu)
        menu.add_cascade(label="Pomoč", menu=menu_pomoc)
        menu_pomoc.add_command(label="Pomoč", command=self.pomoc)
        menu_pomoc.add_command(label="O igri", command=self.oigri)

        for i in range(19):
            self.plosca.create_line(i*36+36, 0+36, i*36+36, 648+36)
            self.plosca.create_line(0+36, i*36+36, 648+36, i*36+36)
        
        self.igralec1 = Clovek(self, Alfabeta(2))
        self.igralec2 = Racunalnik(self, Alfabeta(2))
        self.klik = None
        self.konec = False
        self.igralec1.igraj()
    
    def pomoc(self):
        """Funkcija ustvari okno pomoč v GUI"""
        help = tk.Toplevel()
        help.grab_set()                                  
        help.title("Pomoč")                           
        help.resizable(width=False, height=False)  
        tk.Label(help, text="Navodila za igranje igre 5 v vrsto", font=("Helvetica", 20)).grid(row=0, column=0)       

        tk.Label(help, text=" \n"
                                 "Igra se igra na igralni plošči velikosti 19x19. \n"
                                 "Igrata jo dva igralca. Figurice (črne in bele)  \n"
                                 "igralca izmenično postavljata na vozlišča mreže in \n"
                                 "poskušata narediti vrsto, stolpec ali diagonalo \n"
                                 "petih figuric svoje barve. \n"
                                 " \n"
                                 "Zmaga igralec, ki prvi doseže 5 v vrsto. \n"
                                 " \n"
                                 "V kolikor želite igrati novo igro, izberite \n"
                                 "v meniju igra -> nova igra ali desno zgoraj \n"
                                 "kliknite na nova igra. Odprlo se vam bo novo \n"
                                 "okno, v katerem lahko nastavite parametre igralcev. \n"
                                 , justify="left").grid(row=1, column=0)

    def oigri(self):
        """Funkcija ustvari okno o igri v GUI."""        
        about = tk.Toplevel()
        about.grab_set()                                  
        about.title("O igri")                           
        about.resizable(width=False, height=False) 
       

        tk.Label(about, text=" \n"
                                 "Verzija igre: 1.0 \n"
                                 "  \n"
                                 "Avtorja: Mark Baltič in Jure Bernot \n"
                                 "Leto izida: 2016 \n"
                                 " \n"
                                 " \n"
"""Igra je objavljena pod licenco MIT. Več o licenci si lahko 
preberete na https://opensource.org/licenses/MIT. Celotna 
licenca je objavljena tudi v datoteki LICENCE.md v igri.

Avtorja vljudno naprošava, da morebitne napake, 
težave in hrošče v programu sporočite na:
https://github.com/bbYYJnhA/Wu-Zi-Qi/issues

Celotna koda programa je objavljena na:
https://github.com/bbYYJnhA/Wu-Zi-Qi
""" , justify="left").grid(row=1, column=0)




    def sporocilo(self, msg, naslov):
        """
        Funkcija odpre novo okno z vsebino sporočila in naslovom podanim v funkciji.
        """
        popup = tk.Toplevel()                               
        popup.title(naslov)                           
        popup.resizable(width=False, height=False)  
        tk.Label(popup, text=msg, font=("Helvetica", 20)).grid(row=0, column=0) 


    def nova_igra(self, igralec1, igralec2, tezavnost_crni=2, tezavnost_beli=2):
        """
        Funkcija prekine že obstoječo igro in nastavi novo glede na parametre,
        ki jih naklika uporabnik v gui.
        """
        if self.igralec1 is not None:
            self.igralec1.prekini()
        if self.igralec2 is not None:
            self.igralec2.prekini()

        # Nastavljamo vse potrebno za pričetek igre       
        self.igralec1 = igralec1(self, Alfabeta(tezavnost_crni))
        self.igralec2 = igralec2(self, Alfabeta(tezavnost_beli))     
        self.klik = None
        self.konec = False
        self.igra = Igra(self)        
        
        # Brišemo figure in črte s polja
        self.plosca.delete("figure")
        self.plosca.delete("crta")
        self.plosca.delete("pika")
        self.napis2.set("Na potezi je ČRNI")
        self.igralec1.igraj()

    def nova_igra_gumb(self):
        """Ustvari okno za izbiro nastavitev nove igre (če ne obstaja) ter začne novo igro z izbranimi nastavitvami."""

        def ustvari_igro():
            """Pomožna funkcija, ki ustvari novo igro, nastavi ime igralcev ter zapre okno za izbiro nastavitev."""
            if igralec_1_clovek.get():
                igralec_1 = Clovek
            else:
                igralec_1 = Racunalnik
            if igralec_2_clovek.get():
                igralec_2 = Clovek
            else:
                igralec_2 = Racunalnik
            self.nova_igra(igralec_1, igralec_2, tezavnost_crni.get(), tezavnost_beli.get())
            new_game.destroy()

        # Novo okno nova igra
        new_game = tk.Toplevel()
        new_game.grab_set()                                  
        new_game.title("Nova igra")                           
        new_game.resizable(width=False, height=False)         


        # Nastavitve višine, širine posameznih stolpcev/vrstic
        new_game.grid_columnconfigure(0, minsize=120)       
        new_game.grid_columnconfigure(2, minsize=150)
        new_game.grid_rowconfigure(0, minsize=80)
        new_game.grid_rowconfigure(5, minsize=70)
        new_game.grid_rowconfigure(9, minsize=80)

        tk.Label(new_game, text="Nastavitve nove igre", font=("Helvetica", 20)).grid(row=0, column=0, columnspan=4)

      
        # Nastavitve igralcev
        tk.Label(new_game, text="ČRNI", font=("Helvetica", 13)).grid(row=2, column=0, sticky="E")
        tk.Label(new_game, text="BELI", font=("Helvetica", 13)).grid(row=2, column=2, sticky="E")
        tk.Label(new_game, text="Vrsta igralca:").grid(row=3, column=0, rowspan=2, sticky="E")
        tk.Label(new_game, text="Vrsta igralca:").grid(row=3, column=2, rowspan=2, sticky="E")

        igralec_1_clovek = tk.BooleanVar()                         
        igralec_1_clovek.set(True)                                 
        igralec_2_clovek = tk.BooleanVar()                         
        igralec_2_clovek.set(True)                                 
        igralci = [("Človek", True, igralec_1_clovek, 4, 1), ("Računalnik", False, igralec_1_clovek, 5, 1),
                   ("Človek", True, igralec_2_clovek, 4, 3), ("Računalnik", False, igralec_2_clovek, 5, 3)]

        # Ustvari radijske gumbe za izbiro vrste igralcev
        for besedilo, vrednost, spremenljivka, vrstica, stolpec in igralci:
            tk.Radiobutton(new_game, text=besedilo, variable=spremenljivka, value=vrednost, width=10, anchor="w")\
                .grid(row=vrstica, column=stolpec)

        # Drsnik za izbiro težavnosti belega in črnega igralca
        tezavnost_crni = tk.IntVar()
        tezavnost_crni.set(2)        
        tk.Label(new_game, text="Težavnost:").grid(row=6, column=0, rowspan=2, sticky="E")
        skala_crni = tk.Scale(new_game, from_=1, to=3, variable = tezavnost_crni, orient="horizontal")
        skala_crni.grid(row=6, column=1)
        
        tezavnost_beli = tk.IntVar()
        tezavnost_beli.set(2)          
        tk.Label(new_game, text="Težavnost:").grid(row=6, column=2, rowspan=2, sticky="E")
        skala_crni = tk.Scale(new_game, from_=1, to=3, variable = tezavnost_beli, orient="horizontal")
        skala_crni.grid(row=6, column=3)
        

        # Gumba za začetek nove igre in preklic
        tk.Button(new_game, text="Prekliči", width=20, height=2,
                  command=lambda: new_game.destroy()).grid(row=9, column=0, columnspan=3, sticky="E")
        tk.Button(new_game, text="Začni igro", width=20, height=2,
                  command=lambda: ustvari_igro()).grid(row=9, column=3, columnspan=3, sticky="E")
    


    def klik_plosca(self, event):
        """
        Nariše črne oz. bele krogce na polje v odvisnosti igralca na potezi.
        """
        x = ((event.x + 18) // 36)
        y = ((event.y + 18) // 36)
        if x > 0 and y > 0 and x < 20 and y < 20:
            if self.igra.na_potezi == CRNI:
                self.igralec1.klik(x, y)
            elif self.igra.na_potezi == BELI:
                self.igralec2.klik(x, y)
            else:
                assert False, "Neveljaven igralec klik"
            
    def narisi1(self, i, j):
        """
        Funkcija riše črne krogce. i,j so koodrinate v tabeli; x,y pa koordinate na risalnem platnu.
        """
        x = i * 36
        y = j * 36
        self.plosca.create_oval(x - 18, y - 18, x + 18, y + 18, fill="black", tags="figure")
        self.plosca.create_oval(x - 5, y - 5, x + 5, y + 5, fill="red", tags="pika")

    def narisi2(self, i, j):
        """
        Funkcija riše bele krogce. i,j so koodrinate v tabeli; x,y pa koordinate na risalnem platnu.
        """
        x = i * 36
        y = j * 36
        self.plosca.create_oval(x - 18, y - 18, x + 18, y + 18, fill="white", tags="figure")
        self.plosca.create_oval(x - 5, y - 5, x + 5, y + 5, fill="red", tags="pika")     

    def narisi_crto(self, kje):
        """
        Funkcija nariše daljico. Krajišči sta podani z začetnima in končnima koordinatama zmagovalne petorke.
        Uporablja se za povezovanje figur zmagovalne kombinacije.
        """
        (y0, x0) = kje[0]
        (y1, x1) = kje[4]
        self.plosca.create_line((x0+1) * 36, (y0+1) * 36, (x1+1) * 36, (y1+1) * 36, fill="red", width="3", tag="crta") 

    def preveri_zmago(self, j, i):
        """Preveri, če je konec, in vrne trojico (Bool, zmagovalec, zmagovalna petorka)."""
        dolzina = len(self.igra.tabela)

        # Preverjamo po vrsticah
        vrstica = i
        for stolpec in range(dolzina-4):
            if self.igra.tabela[vrstica][stolpec] != 0:
                ena = self.igra.tabela[vrstica][stolpec]
                dva = self.igra.tabela[vrstica][stolpec+1]
                tri = self.igra.tabela[vrstica][stolpec+2]
                stiri = self.igra.tabela[vrstica][stolpec+3]
                pet = self.igra.tabela[vrstica][stolpec+4]
                if ena == dva == tri == stiri == pet:
                    self.konec = True
                    return (True, self.igra.na_potezi, \
                            [(vrstica,stolpec),(vrstica,stolpec+1),(vrstica,stolpec+2),(vrstica,stolpec+3),(vrstica,stolpec+4)])

        # Preverjamo po stolpcih
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

        # Preverjamo po levih diagonalah
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
        
        # Preverjamo po desnih diagonalah
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
        
    def povleci_potezo(self, x, y):
        """
        Funkcija naredi in nariše potezo.
        """
        i = x - 1
        j = y - 1
        if self.igra.pravilna(i, j):
            trenutni = self.igra.na_potezi
            if self.igra.na_potezi == CRNI:
                self.plosca.delete("pika")
                self.narisi1(x, y)              
                self.igra.povleci(i, j)
                (kaj, kdo, kje) = self.preveri_zmago(i,j)
                if kaj:
                    self.narisi_crto(kje)
                    self.konec = True
                    self.napis2.set("Zmagal je ČRNI")
                    self.sporocilo("     Zmagal je ČRNI     ", "Igre je konec")
                else:
                    self.napis2.set("Na potezi je beli")
                    self.igralec2.igraj()
            elif self.igra.na_potezi == BELI:
                self.narisi2(x, y)              
                self.igra.povleci(i, j)
                (kaj, kdo, kje) = self.preveri_zmago(i,j)
                if kaj:
                    self.narisi_crto(kje)
                    self.konec = True
                    self.napis2.set("Zmagal je BELI")
                    self.sporocilo("     Zmagal je BELI     ", "Igre je konec")
                else:
                    self.napis2.set("Na potezi je črni")
                    self.igralec1.igraj()
            else:
                assert False, "Neveljaven igralec poskuša povleči potezo."
            

if __name__ == "__main__":
    # Naredimo glavno okno in nastavimo ime
    root = tk.Tk()
    root.resizable(width=False, height=False) 
    root.title("五子棋")
    
    # Naredimo objekt razreda Gui in ga spravimo v spremenljivko,
    # sicer bo Python mislil, da je objekt neuporabljen in ga bo pobrisal
    # iz pomnilnika.
    aplikacija = Gui(root)
    # Kontrolo prepustimo glavnemu oknu. Funkcija mainloop neha
    # delovati, ko okno zapremo.
    root.mainloop()        

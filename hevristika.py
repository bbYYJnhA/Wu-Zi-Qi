import numpy as np

ZMAGA = 10000000
CRNI = 1
BELI = 2

def vrednost_crni(vrstica):
    vrednost = 0
    vrstica.append(BELI)
    prvi_konec = BELI
    trenutni = BELI
    trenutna_vrednost = 0
    for el in vrstica:
        if el == CRNI:
            trenutni = CRNI
            trenutna_vrednost += 1
        elif el == 0:
            if trenutni == CRNI:
                if prvi_konec == 0:
                    if trenutna_vrednost >= 5:
                        vrednost += ZMAGA
                    if trenutna_vrednost == 4:
                        vrednost += ZMAGA // 10
                    if trenutna_vrednost == 3:
                        vrednost += ZMAGA // 100
                    vrednost += 4**trenutna_vrednost
                    trenutna_vrednost = 0
                    trenutni = 0
                    prvi_konec = 0
                else:
                    if trenutna_vrednost >= 5:
                        vrednost += ZMAGA
                    vrednost += 2**trenutna_vrednost
                    trenutna_vrednost = 0
                    trenutni = 0
                    prvi_konec = 0

            trenutni = 0
            prvi_konec = 0
            trenutna_vrednost = 0
        
        elif el == BELI:
            if trenutni == CRNI:
                if prvi_konec == 0:
                    if trenutna_vrednost >= 5:
                        vrednost += ZMAGA
                    vrednost += 2**trenutna_vrednost
                    trenutna_vrednost = 0
                    trenutni = BELI
                    prvi_konec = BELI
                    if trenutna_vrednost >= 5:
                        vrednost += ZMAGA
                    if trenutna_vrednost == 4:
                        vrednost += ZMAGA // 10
                    if trenutna_vrednost == 3:
                        vrednost += ZMAGA // 100
            trenutni = BELI
            prvi_konec = BELI
            trenutna_vrednost = 0

        else:
            assert False, "Neveljaven element v tabeli"

    return vrednost

def vrednost_beli(vrstica):
    vrednost = 0
    vrstica.append(CRNI)
    prvi_konec = CRNI
    trenutni = CRNI
    trenutna_vrednost = 0
    for el in vrstica:
        if el == BELI:
            trenutni = BELI
            trenutna_vrednost += 1
        elif el == 0:
            if trenutni == BELI:
                if prvi_konec == 0:
                    if trenutna_vrednost >= 5:
                        vrednost += ZMAGA
                    if trenutna_vrednost == 4:
                        vrednost += ZMAGA // 2
                    if trenutna_vrednost == 3:
                        vrednost += ZMAGA // 3
                    vrednost += 4**trenutna_vrednost
                    trenutna_vrednost = 0
                    trenutni = 0
                    prvi_konec = 0
                else:
                    if trenutna_vrednost >= 5:
                        vrednost += ZMAGA
                    vrednost += 2**trenutna_vrednost
                    trenutna_vrednost = 0
                    trenutni = 0
                    prvi_konec = 0

            trenutni = 0
            prvi_konec = 0
            trenutna_vrednost = 0
        
        elif el == CRNI:
            if trenutni == BELI:
                if prvi_konec == 0:
                    if trenutna_vrednost >= 5:
                        vrednost += ZMAGA
                    vrednost += 2**trenutna_vrednost
                    trenutna_vrednost = 0
                    trenutni = CRNI
                    prvi_konec = CRNI
                else:
                    if trenutna_vrednost >= 5:
                        vrednost += ZMAGA

            trenutni = CRNI
            prvi_konec = CRNI
            trenutna_vrednost = 0

        else:
            assert False, "Neveljaven element v tabeli"

    return vrednost

def vrednost_seznama(sez,barva):
    #if barva == BELI:
     #   return 2*vrednost_beli(sez[:]) - vrednost_crni(sez[:])
    #elif barva == CRNI:
    return -vrednost_crni(sez[:]) + vrednost_beli(sez[:])
    #else:
     #  assert False, "Neveljavna barva v skupaj"

def vrednost_vrstic(tabela,barva):
    vrednost = 0
    for vrstica in tabela:
        vrednost += vrednost_seznama(vrstica, barva)
    return vrednost

def vrednost_stolpcev(tabela,barva):
    trans = [list(x) for x in zip(*tabela)]
    return vrednost_vrstic(trans, barva)

def vrednost_diagonal(tabela, barva):
    def vse_diagonale(tabela):
        matrika1 = np.array(tabela)
        diagonale = []
        dolzina = len(tabela)
        #le diagonale, ki so dolzine vsaj 5
        for i in range(5-dolzina, dolzina-4):
            diagonale.append(list(matrika1.diagonal(i)))
            diagonale.append(list(np.fliplr(matrika1).diagonal(i)))

        #transponrana = [list(x) for x in zip(*tabela)]
        # matrika2 = np.array(tabela)
        # for i in range(5-dolzina, dolzina-4):
        #     diagonale.append(list(matrika2.diagonal(i)))
        return diagonale

    return vrednost_vrstic(vse_diagonale(tabela), barva)


def vrednost_skupaj(tabela,barva):
    return vrednost_vrstic(tabela,barva) + vrednost_stolpcev(tabela,barva) + vrednost_diagonal(tabela,barva)

# testna_tabela = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                 [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                 [0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                 [0, 0, 0, 0, 0, 0, 1, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                 [0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0], 
#                 [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
#test1 = [1,0,1,2,2,2,2,1,0,2,0,1,1,0]
#test2 = [1,2,2,2,2,1]
#test1 = [0,1,2]
#test2 = [2,1,1,1,2]

#print(skupaj(test1))
#print(skupaj(test2))
#print(skupaj(test2,1))
#print(vrednost_skupaj(testna_tabela,BELI))

#v0 = [[0,2,1,0],[0,2,1,0],[0,2,0,0]]
#s0 = [[0,2,2,2,0],[0,0,1,1,0]]
#d0 = [0,2,0]
#print("{0} vrstice".format(vrednost_vrstic(v0, BELI)))
#print("{0} stolpci".format(vrednost_stolpcev(s0,BELI)))
t = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 1, 2,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
#print("{0} vrstice".format(vrednost_vrstic(t, BELI)))
#print("{0} stolpci".format(vrednost_stolpcev(t,BELI)))
#print("{0} diagonale".format(vrednost_diagonal(t,BELI)))

#d = [[0,2,0],[0,2,1,0],[0,2,1,0],[0,1,1,0],[0,2,0]]
#print("{0} vrstice".format(vrednost_vrstic(d, BELI)))
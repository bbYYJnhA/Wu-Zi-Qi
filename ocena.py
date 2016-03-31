CRNI = 1
BELI = 2
PRAZNO = 0

def ocena_pozicije(zevvrsti, konci, na_potezi):
    if konci == 0 and zevvrsti < 5:
        return 0
    elif zevvrsti == 4:
        if konci == 1:
            if na_potezi:
                return 100000000
            else:
                return 50
        if konci == 2:
            if na_potezi:
                return 100000000
            else:
                return 5000
    elif zevvrsti == 3:
        if konci == 1:
            if na_potezi:
                return 7
            else:
                return 5
        if konci == 2:
            if na_potezi:
                return 10000
            else:
                return 50
    elif zevvrsti == 2:
        if konci == 1:
            return 2
        if konci == 2:
            return 5
    elif zevvrsti == 1:
        if konci == 1:
            return 0.5
        if konci == 2:
            return 1
    return 200000000

def analiza_vrstic_crni(tabela, na_potezi):
    vrednost = 0
    stevilozaporedji = 0
    konci = 0

    for i in range(19):
        for j in range(19):
            if tabela[i][j] == CRNI:
                stevilozaporedji += 1
            elif tabela[i][j] == PRAZNO and stevilozaporedji > 0:
                konci += 1
                vrednost += ocena_pozicije(stevilozaporedji, konci, na_potezi == CRNI)
                stevilozaporedji = 0
                konci = 1
            elif tabela[i][j] == PRAZNO:
                konci = 1
            elif stevilozaporedji > 0:
                vrednost += ocena_pozicije(stevilozaporedji, konci, na_potezi == CRNI)
                stevilozaporedji = 0
                konci = 0
            else:
                konci == 0
            if stevilozaporedji > 0:
                vrednost += ocena_pozicije(stevilozaporedji, konci, na_potezi == CRNI)
                stevilozaporedji = 0
                konci = 0
    return vrednost

def analiza_vrstic_beli(tabela, na_potezi):
    vrednost = 0
    stevilozaporedji = 0
    konci = 0

    for i in range(19):
        for j in range(19):
            if tabela[i][j] == BELI:
                stevilozaporedji += 1
            elif tabela[i][j] == PRAZNO and stevilozaporedji > 0:
                konci += 1
                vrednost += ocena_pozicije(stevilozaporedji, konci, na_potezi == BELI)
                stevilozaporedji = 0
                konci = 1
            elif tabela[i][j] == PRAZNO:
                konci = 1
            elif stevilozaporedji > 0:
                vrednost += ocena_pozicije(stevilozaporedji, konci, na_potezi == BELI)
                stevilozaporedji = 0
                konci = 0
            else:
                konci == 0
            if stevilozaporedji > 0:
                vrednost += ocena_pozicije(stevilozaporedji, konci, na_potezi == BELI)
                stevilozaporedji = 0
                konci = 0
    return vrednost

def vrednost_skupaj(tabela, na_potezi):
    if na_potezi == BELI:       
        return (analiza_vrstic_beli(tabela, True) - analiza_vrstic_crni(tabela, False))
    else:
        return -(analiza_vrstic_beli(tabela, True) - analiza_vrstic_crni(tabela, False))

#tabela1 = [[0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 2, 1, 1, 0, 0, 0], [0, 0, 1, 0, 2, 2, 2, 2, 2, 1, 2, 2, 0, 1, 0, 0, 2, 0, 2], [2, 0, 1, 0, 2, 0, 2, 2, 0, 1, 0, 2, 0, 0, 0, 2, 0, 0, 2], [0, 1, 0, 2, 0, 0, 0, 2, 0, 2, 1, 0, 0, 2, 0, 0, 1, 2, 1], [2, 1, 0, 2, 0, 0, 0, 0, 0, 2, 2, 0, 1, 0, 0, 1, 1, 0, 2], [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 2, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 2, 2, 0, 0, 0, 0], [0, 0, 0, 1, 1, 2, 0, 0, 0, 0, 0, 1, 0, 2, 0, 1, 1, 2, 1], [1, 0, 0, 0, 1, 0, 2, 0, 1, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0], [2, 2, 0, 0, 0, 2, 2, 1, 2, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1], [0, 2, 1, 0, 2, 0, 0, 1, 0, 0, 1, 1, 0, 2, 2, 0, 1, 2, 0], [2, 1, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 2, 0, 1, 1, 0, 0, 1, 1, 0, 2, 0, 2, 1, 0], [0, 0, 1, 1, 2, 2, 0, 2, 1, 0, 2, 1, 0, 2, 0, 0, 0, 1, 0], [1, 0, 0, 2, 2, 2, 0, 0, 0, 1, 2, 1, 0, 2, 1, 0, 2, 0, 0], [1, 0, 2, 1, 1, 2, 2, 0, 2, 1, 0, 0, 1, 0, 1, 1, 2, 0, 0], [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 2, 0, 0, 1, 0, 0, 1], [2, 0, 1, 0, 0, 0, 2, 0, 0, 1, 0, 1, 0, 2, 0, 0, 0, 1, 0], [2, 1, 2, 0, 0, 1, 0, 0, 0, 1, 0, 2, 0, 0, 1, 0, 2, 0, 0]]
#tabela2 = [[0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 2, 1, 1, 0, 0, 0], [0, 0, 1, 0, 0, 2, 2, 2, 2, 1, 2, 2, 0, 1, 0, 0, 2, 0, 2], [2, 0, 1, 0, 2, 0, 2, 2, 0, 1, 0, 2, 0, 0, 0, 2, 0, 0, 2], [0, 1, 0, 2, 0, 0, 0, 2, 0, 2, 1, 0, 0, 2, 0, 0, 1, 2, 1], [2, 1, 0, 2, 0, 0, 0, 0, 0, 2, 2, 0, 1, 0, 0, 1, 1, 0, 2], [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 2, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 2, 2, 0, 0, 0, 0], [0, 0, 0, 1, 1, 2, 0, 0, 0, 0, 0, 1, 0, 2, 0, 1, 1, 2, 1], [1, 0, 0, 0, 1, 0, 2, 0, 1, 0, 0, 0, 0, 0, 2, 2, 0, 2, 0], [2, 2, 0, 0, 0, 2, 2, 1, 2, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1], [0, 2, 1, 0, 2, 0, 0, 1, 0, 0, 1, 1, 0, 2, 2, 0, 1, 2, 0], [2, 1, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 2, 0, 1, 1, 0, 0, 1, 1, 0, 2, 0, 2, 1, 0], [0, 0, 1, 1, 2, 2, 0, 2, 1, 0, 2, 1, 0, 2, 0, 0, 0, 1, 0], [1, 0, 0, 2, 2, 2, 0, 0, 0, 1, 2, 1, 0, 2, 1, 0, 2, 0, 0], [1, 0, 2, 1, 1, 2, 2, 0, 2, 1, 0, 1, 1, 0, 1, 1, 2, 0, 0], [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 2, 0, 0, 1, 0, 0, 1], [2, 0, 1, 0, 0, 0, 2, 0, 0, 1, 0, 1, 0, 2, 0, 0, 0, 1, 0], [2, 1, 2, 0, 0, 1, 0, 0, 0, 1, 0, 2, 0, 0, 1, 0, 2, 0, 0]]



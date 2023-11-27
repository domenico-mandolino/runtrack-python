L= [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

def arrondir_les_chiffres(liste):
    
    for element in liste:
        partie_decimale = element % 1
        if partie_decimale >= 0.5:
            element = element + (1 - partie_decimale)
        else:
            element = element - partie_decimale

arrondir_les_chiffres(L)
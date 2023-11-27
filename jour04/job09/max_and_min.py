L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

def valeur_min_max(liste):
        min = liste[0]  
        longueur=len(liste)
        for i in range(longueur):
            if liste[i] <= min:
                min = liste[i]

        maxi = liste[0]
        longueur=len(liste)
        for i in range(longueur):
            if liste[i] >= maxi:
                maxi = liste[i]
                
        print(min, maxi)

valeur_min_max(L)


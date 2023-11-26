L = [1, 2, 3, 4, 5]

def echange_valeur(liste):
    liste = L
    #verification que la liste n'est pas vive
    if len(liste) >= 2:
      #échange des valeurs de la première et de la dernière case
      liste[0], liste[4] = liste[4], liste[0]
   
echange_valeur(L)

print(L)


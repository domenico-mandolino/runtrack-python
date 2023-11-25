
L = [1, 2, 3, 4, 5]
print('voici me liste', L)
print("Deuxième valeur de la liste :", L[1])

def remplacer_element(liste, index):
         if 0 < index < len(liste) - 1:
            liste[index] = liste[index - 1] + liste[index + 1]
            print("Liste après modification :", L)
            
remplacer_element(L,3)

print("Dernière valeur de la liste :", L[-1])





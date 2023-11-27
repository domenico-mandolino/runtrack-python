L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]


# Filtrer les valeurs dans l'intervalle [25, 90]
valeurs_intervalle = [valeur for valeur in L if 25 <= valeur <= 90]

# Calculer le produit des valeurs dans l'intervalle
produit = 1
for valeur in valeurs_intervalle:
    produit *= valeur

print("Liste :", L)
print("Valeurs dans l'intervalle [25, 90] :", valeurs_intervalle)
print("Produit des valeurs dans l'intervalle [25, 90] :", produit)

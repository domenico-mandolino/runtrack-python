liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

# Liste résultante sans doublons
liste_sans_doublons = []

# Parcourir la liste originale
for element in liste:
    # Ajouter à la liste résultante si l'élément n'est pas déjà présent
    if element not in liste_sans_doublons:
        liste_sans_doublons.append(element)


print("Liste sans doublons :", liste_sans_doublons)
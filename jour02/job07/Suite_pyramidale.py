# Chaîne de caractères
chaine = "abcdefghijklmnopqrstuvwxyz"

# Nombre de lignes dans la pyramide
nombre_lignes = len(chaine)

# Affichage de la pyramide
for ligne in range(1, nombre_lignes + 1):
    espace = (ligne -nombre_lignes) * " " 
    caractere_pyramide =  chaine[:ligne - 1]
    print(espace + caractere_pyramide)
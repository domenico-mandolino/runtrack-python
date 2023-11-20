
# Boucle à travers les caractères ASCII correspondant aux lettres de l'alphabet
for lettre in range(ord('Z'), ord('A') -1 , -1):
    print(chr(lettre), end=' ')

# Nouvelle ligne pour améliorer la lisibilité
print()
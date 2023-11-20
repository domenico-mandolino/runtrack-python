# Programme Python pour afficher l'alphabet

# Boucle à travers les caractères ASCII correspondant aux lettres de l'alphabet
for lettre in range(ord('A'), ord('Z') + 1):
    print(chr(lettre), end=' ')

print()

# Ce programme utilise une boucle for pour itérer à travers les caractères ASCII 
# correspondant aux lettres majuscules de l'alphabet (de 'A' à 'Z'). 
# La fonction ord() renvoie le code ASCII d'un caractère, 
# et chr() renvoie le caractère correspondant à un code ASCII.
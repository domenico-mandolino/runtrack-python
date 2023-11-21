def est_triangle(a, b, c):
    #Vérifie si les longueurs peuvent former un triangle
    return a + b > c and b + c > a and c + a > b

def type_triangle(a, b, c):
   #Détermine le type de triangle
    if a == b == c:
        return "Équilatéral"
    elif a == b or b == c or c == a:
        if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
            return "Rectangle et Isocèle"
        else:
            return "Isocèle"
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
        return "Rectangle"
    else:
        return "Quelconque"

# Demander à l'utilisateur les longueurs a, b, c
a = float(input("Entrez la longueur a : "))
b = float(input("Entrez la longueur b : "))
c = float(input("Entrez la longueur c : "))

# Vérifier si les longueurs peuvent former un triangle
if est_triangle(a, b, c):
    # Déterminer le type de triangle
    type_tri = type_triangle(a, b, c)
    print(f"Les longueurs {a}, {b}, {c} peuvent former un triangle de type {type_tri}.")
else:
    print("Les longueurs données ne peuvent pas former un triangle.")
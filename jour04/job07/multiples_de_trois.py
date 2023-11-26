L = [8, 24, 48, 2, 16]

def compter_multiples_de_3(liste):
    # filtrer les multiples de 3
    multiples_de_3 = [nombre for nombre in liste if nombre % 3 == 0]

    # Afficher la liste des multiples de 3
    print("Multiples de 3 dans la liste :", multiples_de_3)

    # Retourner le nombre de multiples de 3
    return len(multiples_de_3)



# Afficher nombre de multiples de 3 dans la liste
nombre_multiples_de_3 = compter_multiples_de_3(L)
print("Nombre de multiples de 3 dans la liste :", nombre_multiples_de_3)
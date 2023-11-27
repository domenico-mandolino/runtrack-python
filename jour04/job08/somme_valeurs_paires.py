L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]

def nombres_paires(liste):

    nombre_paire = [nombre for nombre in liste if nombre % 2 == 0]

    print("Nombre paires dans la liste :", nombre_paire)

    print(sum(nombre_paire))

nombres_paires(L)
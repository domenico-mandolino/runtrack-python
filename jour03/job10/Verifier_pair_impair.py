def verifier_pair_impair(nombre):
    # Vérification si le nombre est un entier positif
    if nombre == int and nombre >= 0:
        if nombre % 2 == 0:
            print(f"{nombre} est un nombre pair.")
        else:
            print(f"{nombre} est un nombre impair.")
    else:
        print("Veuillez entrer un nombre entier positif.")
verifier_pair_impair(0)
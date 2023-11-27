def my_long_word(longueur_minimale, phrase):
    mots = phrase.split()  # Séparer la phrase en une liste de mots
    mots_long = [mot for mot in mots if len(mot) > longueur_minimale]  # Filtrer les mots plus longs que la longueur minimale
    resultat = " ".join(mots_long)  # Joindre les mots filtrés en une seule chaîne de caractères
    return resultat


resultat = my_long_word(3, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance")
print("Output :", resultat)
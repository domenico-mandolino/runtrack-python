def ajouter_mangue():
    fruits = ["pomme", "cerise", "orange","melon"]
    fruits.insert(2 , "mangue")
    return fruits

resultat = ajouter_mangue()
print(resultat)
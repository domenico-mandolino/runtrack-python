# Variables représentant un produit
nom_produit = "Ordinateur portable"
prix_unitaire = 1000.0
quantite_stock = 50

# Afficher les informations du produit de manière formatée
print("Informations du produit :")
print(f"Nom du produit : {nom_produit}")
print(f"Prix unitaire : ${prix_unitaire}")
print(f"Quantité en stock : {quantite_stock} unités\n")

# Ajouter des produits en stock
quantite_acheter = int(input("Combien d'unités souhaitez-vous acheter ? "))
quantite_stock += quantite_acheter

# Mettre à jour le prix du produit avec l'inflation de 10%
prix_unitaire *= 1.1

# Afficher à nouveau les informations sur le produit
print("\nInformations mises à jour du produit :")
print(f"Nom du produit : {nom_produit}")
print(f"Nouveau prix unitaire : ${prix_unitaire}")
print(f"Nouvelle quantité en stock : {quantite_stock} unités")
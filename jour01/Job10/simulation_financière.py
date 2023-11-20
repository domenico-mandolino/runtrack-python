
montant_initial = 10000.0
taux_rendement_annuel = 5.0  # En pourcentage

# Afficher le gain annuel en fonction du taux de rendement
gain_annuel = (taux_rendement_annuel / 100) * montant_initial
print(f"Gain annuel initial : {gain_annuel} euros\n")

# L'investisseur augmente son capital de 5 000 euros et le taux augmente de 2%
montant_initial += 5000
taux_rendement_annuel += 2

# Calculer à nouveau le gain de l'investisseur
nouveau_gain_annuel = (taux_rendement_annuel / 100) * montant_initial
print(f"Nouveau gain annuel après augmentation : {nouveau_gain_annuel} euros\n")

# L'investisseur retire 10% du montant total, le rendement diminue de 1%
retrait = 0.10 * montant_initial
montant_initial -= retrait
taux_rendement_annuel -= 1

# Calculer le montant final de l'investissement
montant_final = montant_initial + nouveau_gain_annuel

# Afficher le nouveau gain
print(f"Montant final de l'investissement après retrait : {montant_final} euros")
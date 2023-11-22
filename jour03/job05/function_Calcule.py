def calcule (n1 , operateur , n2):
   if operateur == "+":
    resultat = n1 + n2
   elif operateur == "-":
     resultat = n1 - n2
   elif operateur == "*":
     resultat = n1 * n2
   elif operateur == "x" or operateur == "X":
     resultat = n1 * n2
   elif operateur == "/":
        resultat = n1 / n2
   elif operateur == "%":
        resultat = n1 % n2
   else:
        return "Erreur: Division par zéro"

   return resultat  

print (calcule(30 , "%", 100))
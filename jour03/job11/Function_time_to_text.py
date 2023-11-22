def time_to_text(minutes):
    if type(minutes) == int and minutes >= 0:
        heures = minutes // 60
        minutes_restantes = minutes % 60

        if heures == 0:
            resultat = f"{minutes} minute"

        elif minutes_restantes == 0:
            resultat = f"{heures} heure"
            
        else:
            resultat = f"{heures} heure et {minutes_restantes} minute"

        print(resultat)
        
    else:
        print("Veuillez entrer un nombre entier de minutes positif.")

time_to_text(124)
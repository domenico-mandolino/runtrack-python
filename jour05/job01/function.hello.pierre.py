message = "Hello"

def message_bienvenu():
    prenom = input("Quel est votre prenom?")
    if prenom == "Pierre" or "pierre":
        print(message +" " f"{prenom}" "!")
    else:
        print("Votre nom n'est pas enregisté")

message_bienvenu()
def moyenne ():
    note1 = int(input("entrer la note n.1:"))
    note2 = int(input("entrer la note n.2:")) 
    note3 = int(input("entrer la note n.3:"))
    moyenne_etudiant = (note1 + note2 + note3) / 3
    print (int(moyenne_etudiant))
    if 15<= moyenne_etudiant <= 20:
        print ("Très bon élève")
    elif 11>= moyenne_etudiant <= 14:
        print ("Bon élève")
    elif 8>= moyenne_etudiant <= 10:
        print ("Élève moyen")
    elif 0>= moyenne_etudiant <= 7:
        print ("Élève devant faire des efforts")
moyenne()
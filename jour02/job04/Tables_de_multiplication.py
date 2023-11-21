while True:
    n = int(input("donnez un entier > 0 : "))
    print("Table de multiblication de", n)
    if n > 0:
        for x in range(1, 11):
         resultat = n*x
         print( n,"*",x,"=",resultat)


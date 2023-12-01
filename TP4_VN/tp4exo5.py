dates = str(input("entrer une date au format jjmmaaaa"))
print(dates)

while len(dates) != 8: 
        dates = str(input("mauvais format veuiller ecrire une date de format jjmmaaaa"))
        

annee = dates[4]+dates[5]+dates[6]+dates[7]
mois = dates[2]+dates[3]
jour = dates[0]+dates[1]


if int(annee) % 4 == 0:
    if int(mois) == 2 :
        if int(jour) > 29 :
            print("date invalide")
        else :
            print("Date valide")
            
    if int(mois) == 1 or  int(mois) == 3 or int(mois) == 5 or int(mois) == 7 or int(mois) == 8 or int(mois) == 10 or int(mois) == 12 :
        if int(jour) < 32 and int(jour) > 0 :
            print("Date correcte")
        else :
            print("Date incorrect")
    if int(mois) == 4 or  int(mois) == 6 or int(mois) == 9 or int(mois) == 11 :
        if int(jour) < 31 and int(jour) > 0 :
            print("Date correcte")
        else :
            print("Date incorrect")
else :
    if int(mois) == 2 :
        if int(jour) > 28 :
            print("date invalide")
        else :
            print("Date valide")
            
    if int(mois) == 1 or  int(mois) == 3 or int(mois) == 5 or int(mois) == 7 or int(mois) == 8 or int(mois) == 10 or int(mois) == 12 :
        if int(jour) < 32 and int(jour) > 0 :
            print("Date correcte")
        else :
            print("Date incorrect")
    if int(mois) == 4 or  int(mois) == 6 or int(mois) == 9 or int(mois) == 11 :
        if int(jour) < 31 and int(jour) > 0 :
            print("Date correcte")
        else :
            print("Date incorrect")

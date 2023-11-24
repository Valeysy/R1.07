heure_debut = int(input("Donnez l'heure de début de la location (un entier) : "))
heure_fin = int(input("Donnez l'heure de fin de la location (un entier) : "))


if heure_debut < 0 or heure_debut > 24 or heure_fin < 0 or heure_fin > 24:
    print("Les heures doivent être comprises entre 0 et 24 !\n")
elif heure_debut == heure_fin:
    print("Attention ! L'heure de fin est identique à l'heure de début.\n")
elif heure_debut > heure_fin:
    print("Attention ! Le début de la location est après la fin.\n")
else:

    duree_location = heure_fin - heure_debut

    cout_total = 0
    for heure in range(heure_debut, heure_fin):
        if heure < 7 or (heure >= 17 and heure < 24):
            cout_total += 1.0
        else:
            cout_total += 2.0


print(f"Vous avez loué votre vélo pendant")

duree_tarif_1 = 0
duree_tarif_2 = 0

for heure in range(heure_debut, heure_fin):
    tarif = 1.0 if heure < 7 or (heure >= 17 and heure < 24) else 2.0
    
    if tarif == 1.0:
        duree_tarif_1 += 1
    else:
        duree_tarif_2 += 1

if duree_tarif_1 > 0:
    print(f"{duree_tarif_1} heure(s) au tarif horaire de 1.0 euro(s)")

if duree_tarif_2 > 0:
    print(f"{duree_tarif_2} heure(s) au tarif horaire de 2.0 euro(s)")

print(f"Le montant total à payer est de {cout_total} euro(s).")

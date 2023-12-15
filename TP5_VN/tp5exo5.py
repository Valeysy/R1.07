def calculer_salaire(heures_travaillees, salaire_horaire):
    salaire = min(heures_travaillees, 160) * salaire_horaire

    if heures_travaillees > 160 and heures_travaillees <= 200:
        salaire += (heures_travaillees - 160) * salaire_horaire * 0.25

    if heures_travaillees > 200:
        salaire += (heures_travaillees - 200) * salaire_horaire * 0.50

    return salaire

heures_travaillees = float(input("Entrez le nombre d'heures travaillées : "))
salaire_horaire = float(input("Entrez le salaire horaire : "))

salaire_total = calculer_salaire(heures_travaillees, salaire_horaire)
print(f"Le salaire total est : {salaire_total} euros.")

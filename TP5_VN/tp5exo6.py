def taille_chaine(chaine):
    taille = 0
    for caractere in chaine:
        if caractere == '\0':  # Le caractère de fin de chaîne
            break
        taille += 1
    return taille

def pourcentage_voyelles(chaine):
    voyelles = "aeiouAEIOU"
    nombre_voyelles = sum(1 for caractere in chaine if caractere in voyelles)
    taille = taille_chaine(chaine)
    pourcentage = (nombre_voyelles / max(1, taille)) * 100  # Évite la division par zéro
    return pourcentage

def recherche_sous_chaine(chaine, sous_chaine):
    taille_chaine_totale = taille_chaine(chaine)
    taille_sous_chaine = taille_chaine(sous_chaine)

    for i in range(taille_chaine_totale - taille_sous_chaine + 1):
        if chaine[i:i + taille_sous_chaine] == sous_chaine:
            return i  # Retourne le début de la première occurrence

    return -1  # Retourne -1 si la sous-chaîne n'est pas trouvée

def nombre_occurrences(chaine, sous_chaine):
    occurrences = 0
    index = 0

    while index != -1:
        index = recherche_sous_chaine(chaine[index:], sous_chaine)
        if index != -1:
            occurrences += 1
            index += 1  # Passer au caractère suivant pour éviter de compter la même occurrence à plusieurs reprises

    return occurrences

chaine_utilisateur = input("Entrez la chaîne de caractères : ")

taille = taille_chaine(chaine_utilisateur)
print(f"1. Taille de la chaîne : {taille} caractères")

pourcentage_voy = pourcentage_voyelles(chaine_utilisateur)
print(f"2. Pourcentage de voyelles : {pourcentage_voy:.2f}%")

debut_occurrence = recherche_sous_chaine(chaine_utilisateur, 'wagon')
if debut_occurrence != -1:
    print(f"3. 'wagon' est une sous-chaîne, début de la première occurrence : {debut_occurrence}")
else:
    print("3. 'wagon' n'est pas une sous-chaîne dans la chaîne donnée.")

occurrences_wagon = nombre_occurrences(chaine_utilisateur, 'wagon')
print(f"4. Nombre d'occurrences de 'wagon' dans la chaîne : {occurrences_wagon}")

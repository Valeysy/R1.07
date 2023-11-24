#exo a
N = int(input("Entrez la valeur de N : "))

somme = 0

for i in range(N + 1):
    somme += i

print(f"La somme des N entiers naturels de 0 à {N} est : {somme}")


#exo b
valeur_utilisateur = None

while valeur_utilisateur != 100:
    valeur_utilisateur = int(input("Entrez une valeur : "))

print("Vous avez entré la valeur 100. La boucle d'attente est terminée.")


#exo c
inf_10_count = 0
sup_10_inf_15_count = 0
sup_15_count = 0

for _ in range(10):
    while True:
        try:
            valeur = float(input("Veuillez entrer une valeur réelle entre 0 et 20 : "))
            if 0 <= valeur <= 20:
                break
            else:
                print("La valeur doit être comprise entre 0 et 20. Réessayez.")
        except ValueError:
            print("Veuillez entrer une valeur réelle valide. Réessayez.")

    if valeur < 10:
        inf_10_count += 1
    elif 10 <= valeur < 15:
        sup_10_inf_15_count += 1
    else:
        sup_15_count += 1

print(f"Nombre de valeurs inférieures strictement à 10 : {inf_10_count}")
print(f"Nombre de valeurs supérieures ou égales à 10 et inférieures strictement à 15 : {sup_10_inf_15_count}")
print(f"Nombre de valeurs supérieures ou égales à 15 : {sup_15_count}")


#exo d
X = int(input("Entrez la valeur de X (supérieure à 1) : "))

somme = 0
N = 0

while somme <= X:
    N += 1
    somme += N

N -= 1

print(f"Le plus grand nombre N tel que la somme <= {X} est : {N}")

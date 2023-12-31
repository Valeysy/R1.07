def factorielle_for(n):
    resultat = 1
    print(f"Calcul de la factorielle de {n} avec la boucle 'for':")
    for i in range(1, n + 1):
        resultat *= i
        print(f"Itération {i}: {resultat}")
    return resultat

def factorielle_while(n):
    resultat = 1
    i = 1
    print(f"Calcul de la factorielle de {n} avec la boucle 'while':")
    while i <= n:
        resultat *= i
        print(f"Itération {i}: {resultat}")
        i += 1
    return resultat

n = int(input("Entrez un nombre entier pour calculer sa factorielle : "))

choix_boucle = input("Choisissez la boucle ('for' ou 'while') : ")

if choix_boucle == 'for':
    resultat_final = factorielle_for(n)
elif choix_boucle == 'while':
    resultat_final = factorielle_while(n)
else:
    print("Choix de boucle non valide. Veuillez choisir 'for' ou 'while'.")

print(f"La factorielle de {n} est : {resultat_final}")

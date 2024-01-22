# fonction max

def max_without_max():
    """Trouver le plus grand nombre dans une liste"""
    numbers = [1, 2, 3, 4, 5] # Exemple de liste à tester
    if len(numbers) > 0:
        maximum = numbers[0]
        for num in numbers[1:]:
            if num > maximum:
                maximum = num
    else:
        print("La liste est vide.") # Si la liste est vide, affiche un message d'erreur
    return maximum

# Moyenne

name="toto"
firstname="titi"
math=12
anglais=12
info=12
promotion=2023
moy = (math+anglais+info)/3

print (type(name))
print (type(firstname))
print (type(anglais))
print (type(info))
print (type(promotion))
print (type(moy))

print ("L’étudiant {}{} de la promotion {} a une moyenne de {}" .format(name, firstname, promotion, moy))

# Calcule minute 

jour=23 
heure=14
minute=50
calc=jour*24*60
calc= calc + 50

print(calc)

# Minute écoulé depuis le début du mois 

print("Combien de minutes se sont écoulés depuis le début du mois?")
minute=int(input())
heure = minute // 60
jour = heure // 24

print ("il s'est passé", jour, "jours depuis le début du mois")

# Généraltion aléatoire entre 0 et 100 

from random import *
a = randint(0,100)
print(a)

# Permutation x et y 

x = int(input("Entrez x: "))
y = int(input("Entrez y: "))

print("Avant permutation:")
print("x :", x)
print("y :", y)

temp = x
x = y
y = temp

print("Après permutation:")
print("x :", x)
print("y :", y)

# Année de naissance 

age_utilisateur = input("Donnez votre âge : ")

age = int(age_utilisateur)

annee_naissance = 2023 - age  

print("Votre année de naissance est :", annee_naissance)

# Permutation 

a= input("Entrez la première valeur : ")
b= input("Entrez la deuxième valeur : ")
c= input("Entrez la troisième valeur : ")

print("Les valeurs entrées sont : a = " + a + ", b = " + b + " et c = " + c)
print("Permutation: a ==> b, b ==> c, c ==> a")

temp = a
a = c
c = b
b = temp

print("Les valeurs permutées sont : a = " + a + ", b = " + b + " et c = " + c)

# exo fondu 

BASE = 4

fromage_base = 800.0
eau_base = 2
ail_base = 2
pain_base = 400

nbConvives = int(input("Entrez le nombre de personne(s) conviées à la fondue :"))

fromage = fromage_base * nbConvives / BASE
eau = eau_base * nbConvives / BASE
ail = ail_base * nbConvives / BASE
pain = pain_base * nbConvives / BASE

print(f"Pour faire une fondue fribourgeoise pour {nbConvives} personnes, il vous faut :")
print(f"- {fromage} gr de fromage")
print(f"- {eau} dl d'eau")
print(f"- {ail} gousse(s) d'ail")
print(f"- {pain} gr de pain")


# Verif si nombre postif, negatif, pair ou impair 

nombre = int(input("Entrez un nombre entier : "))

if nombre > 0:
    signe = "positif"
elif nombre < 0:
    signe = "négatif"
else:
    signe = "zéro"

if nombre % 2 == 0:
    pair = "pair"
else:
    pair = "impair"

print(f"Le nombre est {signe} et {pair}")

# Pile ou face

import random

nombre_aleatoire = random.randint(0, 100)

if nombre_aleatoire < 50:
    resultat = "Pile !"
else:
    resultat = "Face !"

print(resultat)

# Intervalle 

x = float(input("Entrez un nombre décimal : "))

appartient_a_I = ((2<x<3) or (x==2) or (0<x<1) or (x==1) or (-10<x<-2) (x==-10) (x==-2))

if appartient_a_I:
    print("x appartient à I")
else:
    print("x n'appartient pas à I")


# Calcul et affichage de la somme des N entiers naturels (de 0 à N inclus) avec N saisit par l’utilisateur

N = int(input("Entrez la valeur de N : "))

somme = 0

for i in range(N + 1):
    somme += i

print(f"La somme des N entiers naturels de 0 à {N} est : {somme}")


# Boucle d’attente qui se termine si l’utilisateur entre la valeur 100

valeur_utilisateur = None

while valeur_utilisateur != 100:
    valeur_utilisateur = int(input("Entrez une valeur : "))

print("Vous avez entré la valeur 100. La boucle d'attente est terminée.")


# Lecture de 10 valeurs réelles comprises entre 0 et 20
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


#Calcul et affichage du plus grand nombre N tel que ∑ 𝑖 𝑁𝑖=0 ≤ 𝑋 avec X un nombre supérieur à 1 saisit par l’utilisateur.

X = int(input("Entrez la valeur de X (supérieure à 1) : "))

somme = 0
N = 0

while somme <= X:
    N += 1
    somme += N

N -= 1

print(f"Le plus grand nombre N tel que la somme <= {X} est : {N}")

# Compte a rebour

import time

n = int(input("Entrez un nombre entier supérieur à 0 : "))

while n >= 0:
    print(n)
    n -= 1
    time.sleep(1)  

# Jeu nombre mystere

import random

nombre_mystere = random.randint(0, 100)

compteur_tentatives = 0

while True:
    guess = int(input("Devinez le nombre entre 0 et 100 : "))
    
    compteur_tentatives += 1
    
    if guess < nombre_mystere:
        print("Le nombre mystère est plus grand.")
    elif guess > nombre_mystere:
        print("Le nombre mystère est plus petit.")
    else:
        print(f"Félicitations ! Vous avez trouvé le nombre mystère en {compteur_tentatives} tentatives.")
        break  


# Factoriel itérative 

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


# exo vélo :

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


# table de Multiplication :

ask_nb = float(input("Vous cherchez la table de multiplication de quel nombre ? "))
table = []

for multiply in range(10):
    table.append(round(ask_nb * multiply, 1))  
    
for multiply in range(10):
    print(f"{ask_nb} * {multiply} = {table[multiply]}")

# Moyenne calcule ;

# Demande le nombre d'étudiants à l'utilisateur
nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
# déclaration d’une liste vide qui va contenir autant de notes que d'étudiants
notes = []

for i in range(nombreEtudiants):
    note = float(input(f"Note étudiant {i} : "))
    
    while note < 0 or note > 20:
        print("Note invalide. Veuillez saisir une note entre 0 et 20.")
        note = float(input(f"Note étudiant {i} : "))
        
    notes.append(note)
    moyenne += note
        
moyenne /= nombreEtudiants
        
print(f"Moyenne de classe : {moyenne}")

print("Numéro de l’Etudiant | note | ecart a la moyenne")
for i in range(nombreEtudiants):
    ecart = notes[i] - moyenne
    print(f"{i} | {notes[i]} | {ecart}")

# Produit scalaire 

# Demande le nombre d'étudiants à l'utilisateur
nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
# déclaration d’une liste vide qui va contenir autant de notes que d'étudiants
notes = []

for i in range(nombreEtudiants):
    note = float(input(f"Note étudiant {i} : "))
    
    while note < 0 or note > 20:
        print("Note invalide. Veuillez saisir une note entre 0 et 20.")
        note = float(input(f"Note étudiant {i} : "))
        
    notes.append(note)
    moyenne += note
        
moyenne /= nombreEtudiants
        
print(f"Moyenne de classe : {moyenne}")

print("Numéro de l’Etudiant | note | ecart a la moyenne")
for i in range(nombreEtudiants):
    ecart = notes[i] - moyenne
    print(f"{i} | {notes[i]} | {ecart}")


# nombre fréquent 

L1 = [2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7]

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""

def most_frequent(numbers):
    occurrences = {}
    
    for num in numbers:
        if num in occurrences:
            occurrences[num] += 1
        else:
            occurrences[num] = 1
    
    max_occurrences = 0
    most_frequent_number = None
    
    for key, value in occurrences.items():
        if value > max_occurrences:
            max_occurrences = value
            most_frequent_number = key
    
    return most_frequent_number, max_occurrences

resultat = most_frequent(L1)

print(f"Le nombre le plus frequent dans la liste est le : {resultat[0]} ({resultat[1]} x)")

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""

# Nombre fréquent avec count()

L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7]

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""

def most_frequent(numbers):
    most_frequent_number = None
    max_occurrences = 0
    
    for num in set(numbers):
        occurrences = numbers.count(num)
        if occurrences > max_occurrences or (occurrences == max_occurrences and num < most_frequent_number):
            most_frequent_number = num
            max_occurrences = occurrences
    
    return most_frequent_number, max_occurrences

resultat = most_frequent(L1)

print(f"Le nombre le plus frequent dans la liste est le : {resultat[0]} ({resultat[1]} x)")

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""

# Verification date 

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


# liste, ajoute 

L2 = []

taille = int(input("entrer la taille de la liste"))


for i in range(taille):
    tirage = (input("entrer un nombre !"))
    L2.append(tirage)
    print(L2)
    

for i in range(len(L2)-1, 0, -1):
    for j in range(i): 
        if L2[j] > L2[j+1]:
            L2[j], L2[j+1] = L2[j+1], L2[j] 
    print(L2)
    
# Ajout nom 

def nomprenom(nom1, prenom1, nom2, prenom2):

  nom1 = nom1.upper()
  prenom1 = prenom1.capitalize()
  nom2 = nom2.upper()
  prenom2 = prenom2.capitalize()

  if nom1 < nom2:
    print(prenom1, nom1)
    print(prenom2, nom2)
  else:
    print(prenom2, nom2)
    print(prenom1, nom1)

if __name__ == "__main__":
  nom1 = input("Entrez le nom de la première personne : ")
  prenom1 = input("Entrez le prénom de la première personne : ")
  nom2 = input("Entrez le nom de la deuxième personne : ")
  prenom2 = input("Entrez le prénom de la deuxième personne : ")

  nomprenom(nom1, prenom1, nom2, prenom2)


# moyenne v 3

notes = []
coefficients = []
for i in range(5):
    note, coefficient = map(float, input("Veuillez entrer la note du module {} et le coefficient correspondant : ".format(i + 1)).split(" "))
    notes.append(note)
    coefficients.append(int(coefficient))

moyenne_generale = sum(note * coefficient for note, coefficient in zip(notes, coefficients)) / sum(coefficients)

admis = moyenne_generale > 10 and all(note >= 8 for note in notes)

if admis:
    print("L'étudiant est admis.")
else:
    print("L'étudiant n'est pas admis.")


# phrase palindrome 

def est_palindrome(phrase):
    phrase_epuree = ''.join(caractere.lower() for caractere in phrase if caractere.isalpha())
    
    if phrase_epuree == phrase_epuree[::-1]:
        return True
    else:
        return False

mot_phrase = input("Entrez un mot ou une phrase : ")
if est_palindrome(mot_phrase):
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")


# décompose argent 

somme = int(input("Veuillez saisir une somme d'argent : "))

billets_100 = somme // 100
billets_50 = (somme % 100) // 50
billets_10 = ((somme % 100) % 50) // 10
pieces_2 = (((somme % 100) % 50) % 10) // 2
pieces_1 = (((somme % 100) % 50) % 10) % 2

print("La somme de", somme, "euros se décompose en :",
      billets_100, "billets de 100,",
      billets_50, "billets de 50,",
      billets_10, "billets de 10,",
      pieces_2, "pièces de 2,",
      pieces_1, "pièces de 1.")

# Salaire horaire 

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


# Voyelle et verification d'une chaine de caractere

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

# Verification ficheir 

import os
from datetime import datetime

def verifier_fichier(nom_fichier):
    if os.path.isfile(nom_fichier):
        taille = os.path.getsize(nom_fichier)
        date_modification_timestamp = os.path.getmtime(nom_fichier)
        date_modification = datetime.fromtimestamp(date_modification_timestamp)

        print(f"Le fichier {nom_fichier} existe.")
        print(f"Taille du fichier : {taille} octets.")
        print(f"Dernière modification : {date_modification}")
    else:
        print(f"Le fichier {nom_fichier} n'existe pas.")

fichier1 = input("Entrez le nom du premier fichier : ")
fichier2 = input("Entrez le nom du deuxième fichier : ")

verifier_fichier(fichier1)
verifier_fichier(fichier2)


# jeu du juste prix 

import random

def jeu_juste_prix():
    print("Bienvenue dans le jeu du Juste Prix!")
    nombre_a_deviner = random.randint(1, 100)
    essais = 0

    while True:
        essai_joueur = int(input("Devinez le nombre (entre 1 et 100) : "))
        essais += 1

        if essai_joueur < nombre_a_deviner:
            print("Trop petit! Essayez encore.")
        elif essai_joueur > nombre_a_deviner:
            print("Trop grand! Essayez encore.")
        else:
            print(f"Bravo! Vous avez deviné le juste prix en {essais} essais.")
            break

if __name__ == "__main__":
    jeu_juste_prix()


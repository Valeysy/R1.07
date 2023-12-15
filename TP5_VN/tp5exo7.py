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

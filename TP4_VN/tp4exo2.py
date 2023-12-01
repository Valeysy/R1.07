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


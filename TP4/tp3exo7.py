binome = ('login1', 'login2')
print(f"L'étudiant {binome[0]} est en binome avec l'étudiant {binome[1]}")

nouveau_login = input("Entrez le nouveau login pour changer de binôme : ")
binome = (binome[0], nouveau_login)
print(f"Nouveau binôme : L'étudiant {binome[0]} est en binome avec l'étudiant {binome[1]}")

del binome[1]

troinome = binome + ('login3',)  
print(f"Nouveau trinôme : {troinome}")

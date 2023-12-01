nMax = 4
v1 = []
v2 = []

n = int(input(f"Quelle est la taille de vos vecteurs [entre 1 et {nMax}] ? "))

while n < 1 or n > nMax:
    print(f"La taille des vecteurs doit être entre 1 et {nMax}.")
    n = int(input(f"Quelle est la taille de vos vecteur [entre 1 et {nMax}] ? "))
    
print("Saisie du premier vecteur :")
for i in range(n):
    v1.append(int(input(f"v1[{i}] =")))

print("Saisie du second vecteur :")
for i in range(n):
    v2.append(int(input(f"v2[{i}] =")))

produitScalaire = sum(x * y for x, y in zip (v1, v2))

print(f"Le produit scalaire de v1 et v2 vaut {produitScalaire}")




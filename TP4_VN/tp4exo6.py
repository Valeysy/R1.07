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
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

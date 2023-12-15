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

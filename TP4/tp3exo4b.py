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

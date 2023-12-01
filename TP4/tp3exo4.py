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


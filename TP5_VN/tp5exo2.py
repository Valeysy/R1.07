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

ask_nb = float(input("Vous cherchez la table de multiplication de quel nombre ? "))
table = []

for multiply in range(10):
    table.append(round(ask_nb * multiply, 1))  
    
for multiply in range(10):
    print(f"{ask_nb} * {multiply} = {table[multiply]}")

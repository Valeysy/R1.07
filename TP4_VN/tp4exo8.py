dic={"name":"Nechaev", "firstname":"Vladimir", "promo":2023, "groupe":111}
dic2={"name":"toto", "firstname":"titi", "promo":2021, "groupe":121}


print("\nLes clés du dictionnaire sont :")
for key in dic.keys():
    print(f"-{key}")
    
print("\nLes valeurs du dictionnaire sont :")
for value in dic.values():
    print(f"-{value}")

print("\nLes tuplets du dictionnaire sont :")
for item in dic.items():
    print(f"-{item}")
    

print("Les étudiants formant un binôme sont : ") 
print("- l'étudiant", dic["name"], dic["firstname"], "du groupe", dic["groupe"])
print("- l'étudiant", dic2["name"], dic2["firstname"], "du groupe", dic2["groupe"])
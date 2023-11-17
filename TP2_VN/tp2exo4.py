BASE = 4

fromage_base = 800.0
eau_base = 2
ail_base = 2
pain_base = 400

nbConvives = int(input("Entrez le nombre de personne(s) conviées à la fondue :"))

fromage = fromage_base * nbConvives / BASE
eau = eau_base * nbConvives / BASE
ail = ail_base * nbConvives / BASE
pain = pain_base * nbConvives / BASE

print(f"Pour faire une fondue fribourgeoise pour {nbConvives} personnes, il vous faut :")
print(f"- {fromage} gr de fromage")
print(f"- {eau} dl d'eau")
print(f"- {ail} gousse(s) d'ail")
print(f"- {pain} gr de pain")





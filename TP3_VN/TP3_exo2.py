import time

n = int(input("Entrez un nombre entier supérieur à 0 : "))

while n >= 0:
    print(n)
    n -= 1
    time.sleep(1)  

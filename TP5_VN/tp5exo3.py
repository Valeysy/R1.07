def est_palindrome(phrase):
    phrase_epuree = ''.join(caractere.lower() for caractere in phrase if caractere.isalpha())
    
    if phrase_epuree == phrase_epuree[::-1]:
        return True
    else:
        return False

mot_phrase = input("Entrez un mot ou une phrase : ")
if est_palindrome(mot_phrase):
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")


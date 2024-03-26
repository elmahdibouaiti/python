# Chaîne de caractères à modifier
chaine = "abcde"

# Si la chaîne est vide ou ne contient qu'un seul caractère, afficher la chaîne sans modification
if len(chaine) < 2:
    print(chaine)
else:
    # Échanger le premier et le dernier caractère de la chaîne
    chaine = chaine[-1] + chaine[1:-1] + chaine[0]
    
    # Afficher la chaîne modifiée
    print(chaine)
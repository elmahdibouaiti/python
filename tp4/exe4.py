def trinome(a, b, c):
    # Calcul du discriminant
    delta = b**2 - 4*a*c
    
    # Pas de racines réelles
    if delta < 0:
        return (0,)
    # Une racine réelle double
    elif delta == 0:
        x = -b / (2*a)
        return (1, x)
    # Deux racines réelles distinctes
    else:
        x1 = (-b - delta**0.5) / (2*a)
        x2 = (-b + delta**0.5) / (2*a)
        return (2, x1, x2)

# Saisie des coefficients par l'utilisateur
a = float(input("Entrez le coefficient a : "))
b = float(input("Entrez le coefficient b : "))
c = float(input("Entrez le coefficient c : "))

# Appel de la fonction trinome avec les coefficients saisis
resultat = trinome(a, b, c)

# Affichage des résultats
if resultat[0] == 0:
    print("Le trinôme n'a pas de racines réelles.")
elif resultat[0] == 1:
    print(f"Le trinôme a une racine réelle double : {resultat[1]}")
else:
    print(f"Le trinôme a deux racines réelles distinctes : {resultat[1]} et {resultat[2]}")

def somme(*args):
    """
    Fonction qui calcule la somme des nombres passés en arguments.
    
    Paramètres:
    *args (int): Liste de nombres à additionner.
    
    Retourne:
    int: Somme des nombres passés en arguments.
    """
    
    # Initialiser la variable s à 0
    s = 0
    
    # Parcourir chaque argument passé à la fonction
    for i in args:
        # Ajouter le nombre actuel à la variable s
        s += i
    
    # Retourner la somme des nombres
    return s

# Appeler la fonction avec les arguments 1 et 2
print(somme(1,2,3,4,5))

def exemple(**kargs):
    """
    Fonction qui affiche les arguments passés en paramètres nommés.
    
    Paramètres:
    **kargs (dict): Dictionnaire des arguments passés en paramètres nommés.
    """
    
    print(kargs)
    
# Appeler la fonction avec les arguments i=1, j=2, et text="coucou"
print(exemple(i=1,j=2,text="coucou"))

def Puissance(nb, pui = 2):
    """
    Fonction qui calcule la puissance d'un nombre.
    
    Paramètres:
    nb (int): Nombre à élever à la puissance.
    pui (int): Puissance à laquelle élever le nombre.
    
    Retourne:
    int: Résultat de l'opération.
    """
    
    # Calculer de la puissance , retourner le résultat de l'opération
    return nb ** pui
    
# Appeler la fonction avec les arguments 2 et 3
print(Puissance(2,3))

# Appeler la fonction avec l'argument 2
print(Puissance(2))

def factoriel(nb):
    
    """
    Fonction qui calcule le factoriel d'un nombre.
    
    Paramètres:
    nb (int): Nombre dont on veut calculer le factoriel.
    
    Retourne:
    int: Résultat du calcul du factoriel.
    """
    
    # Si le nombre est 1 ou 0, retourner 1 (0! = 1)
    if nb== 1 or nb == 0 :
        return 1
    
    # Sinon, retourner le produit du nombre et du factoriel du nombre précédent
    else:
        return nb * factoriel(nb-1)
        
# Appel de la fonction factoriel pour calculer le factoriell de  5
print("Le factorielle de 5 est ",factoriel(5))
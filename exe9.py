import math

print("Choisissez une forme géométrique:")
print("1. Sphère")
print("2. Parallélépipède rectangle")
print("3. Cylindre")

choix = int(input("Entrez votre choix (1, 2 ou 3): "))

if choix == 1:
    r = float(input("Entrez le rayon de la sphère: "))
    volume = (4/3) * math.pi * r**3
    print("Le volume de la sphère est:", volume)
elif choix == 2:
    lan = float(input("Entrez la langueur du parallélépipède rectangle: "))
    lar = float(input("Entrez la largeur du parallélépipède rectangle: "))
    h = float(input("Entrez la hauteur du parallélépipède rectangle: "))
    volume = lan * lar * h
    print("Le volume du parallélépipède rectangle est:", volume)
elif choix == 3:
    r = float(input("Entrez le rayon du cylindre: "))
    h = float(input("Entrez la hauteur du cylindre: "))
    volume = math.pi * r**2 * h
    print("Le volume du cylindre est:", volume)
else:
    print("Choix invalide. Veuillez entrer 1, 2 ou 3.")

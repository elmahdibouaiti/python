class Point:
    def __init__(self, nom, abscisse):
        self.nom = nom
        self.abscisse = abscisse

    def affiche(self):
        print(f"Nom du point: {self.nom}, Abscisse: {self.abscisse}")

    def translate(self, valeur):
        self.abscisse += valeur

point1 = Point("A", 5)

point1.affiche()
point1.translate(10)

point1.affiche()
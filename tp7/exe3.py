class Vecteur2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vecteur2D(self.x + other.x, self.y + other.y)

    def affiche(self):
        print(f"Vecteur2D (x: {self.x}, y: {self.y})")

v1 = Vecteur2D()
v2 = Vecteur2D(3, 4)

v1.affiche()
v2.affiche()

resultant_vector = v1 + v2
resultant_vector.affiche()

class RectangleSimple:
    def __init__(self, long=1, lar=1):
        self.long = long
        self.lar = lar

    def surface(self):
        return self.long * self.lar

    def affiche(self):
        print(f"Rectangle (long: {self.long}, lar: {self.lar}, surface: {self.surface()})")

class CarreSimple:
    def __init__(self, cote=1):
        self.cote = cote

    def surface(self):
        return self.cote * self.cote

    def affiche(self):
        print(f"Carré (côté: {self.cote}, surface: {self.surface()})")


rectangle_simple = RectangleSimple(4, 5)
carre_simple = CarreSimple(3)

rectangle_simple.affiche()
carre_simple.affiche()

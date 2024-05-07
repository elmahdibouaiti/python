class MaClasseSimple:
    def __init__(self):
        self.x = 23
        self.y = self.x + 5

    def affiche(self):
        z = 42
        print(f"y: {self.y}, z: {z}")

obj1_simple = MaClasseSimple()
obj1_simple.affiche()
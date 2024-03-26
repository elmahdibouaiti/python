class Point:
    def __init__(self, x, y):
        self.px, self.py = x, y

class Segment:
    def __init__(self, x1, y1, x2, y2):
        self.orig = Point(x1, y1)
        self.extren = Point(x2, y2)

    def __str__(self):
        return "Segment : [({:.1f}, {:.1f}), ({:.1f}, {:.1f})]".format(self.orig.px, self.orig.py, self.extren.px, self.extren.py)
    

s=Segment(0, 0, 5, 4)
print(s)


class Rectangle:
    def __init__(self, longueur=30, largeur=15):
    self.L, self.l= longueur, largeur
    self.nom= "rectangle

    def __str__(self):
    return "non: {}".format(self.nom)

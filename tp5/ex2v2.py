class Livre:
    def __init__(self, titre, auteur,nbpages):
        self.titre=titre
        self.auteur=auteur
        self.nbpages=nbpages
    def get_info(self):
        return f"{self.titre} écrit par {self.auteur} contient {self.nbpages} pages"
    
mon_livre1 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 83)
mon_livre2 = Livre("Antigone", "Jean Anouilh", 120)

print(mon_livre1.get_info())
print(mon_livre2.get_info())

mon_livre1.nbpages = 100
print(mon_livre1.get_info())

mon_livre2.nbpages = 100
print(mon_livre2.get_info())
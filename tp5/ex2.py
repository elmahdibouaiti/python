class Livre:
    def __init__(self, titre, auteur,nbpages):
        self.titre=titre
        self.auteur=auteur
        self.nbpages=nbpages
    def getTitre(self):
        return self.titre
    def getAuteur(self):
        return self.auteur
    def getNbPages(self):
        return self.nbpages
    def setNbpages(self, nbpages):
        nbpages=nbpages


mon_livre1 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 83)
mon_livre2 = Livre("Antigone", "Jean Anouilh", 120)
# Livre 1
titre = mon_livre1.getTitre()
print(f"Le titre du livre est {titre}")
auteur = mon_livre1.getAuteur()
print(f"L'auteur du livre est {auteur}")

nb_pages = mon_livre1.getNbPages()
print(f"Le livre a {nb_pages} pages")

mon_livre1.setNbpages(100)
nb_pages = mon_livre1.getNbPages()
print(f"Le livre a maintenant {nb_pages} pages")

# Livre 2
titre = mon_livre2.getTitre()
print(f"Le titre du livre est {titre}")
auteur = mon_livre2.getAuteur()
print(f"L'auteur du livre est {auteur}")

nb_pages = mon_livre2.getNbPages()
print(f"Le livre a {nb_pages} pages")

mon_livre2.setNbpages(100)
nb_pages = mon_livre2.getNbPages()
print(f"Le livre a maintenant {nb_pages} pages")
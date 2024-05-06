class Livre:
    def __init__(self, titre, auteur,nbpages):
        self.titre=titre
        self.auteur=auteur
        self.nbpages=nbpages
    def get_info(self):
        return f"{self.titre} écrit par {self.auteur} contient {self.nbpages} pages"
    
def lire_depuis_fichier(nom_fichier):
    livres = []
    with open(nom_fichier, 'r') as fichier:
        for ligne in fichier:
            titre, auteur, nbpages = ligne.strip().split(',')
            livres.append(Livre(titre, auteur, int(nbpages)))
    return livres

livres_stockes = lire_depuis_fichier("C:/Users/elmah/Downloads/python-main/python-main/tp5/data_livres.txt")
for livre in livres_stockes:
    print(livre.get_info())
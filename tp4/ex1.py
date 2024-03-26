def scanner(objet_fichier, gestionnaire_ligne):
    for ligne in objet_fichier:
        gestionnaire_ligne(ligne)

if __name__ == '__main__':
    def premierMot(ligne):
        print(ligne.split()[0])

    fic = open("data.dat")
    scanner(fic, premierMot)

    import io
    chaine = io.StringIO("un\deux xxx\ntois\n")
    scanner(chaine, premierMot)
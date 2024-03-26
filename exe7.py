nombre = int(input("Entrez un nombre entre 1 et 12 : "))

if nombre == 1:
    mois = "Janvier"
elif nombre == 2:
    mois = "Février"
elif nombre == 3:
    mois = "Mars"
elif nombre == 4:
    mois = "Avril"
elif nombre == 5:
    mois = "Mai"
elif nombre == 6:
    mois = "Juin"
elif nombre == 7:
    mois = "Juillet"
elif nombre == 8:
    mois = "Août"
elif nombre == 9:
    mois = "Septembre"
elif nombre == 10:
    mois = "Octobre"
elif nombre == 11:
    mois = "Novembre"
elif nombre == 12:
    mois = "Décembre"
else:
    mois = "Nombre invalide ! Veuillez entrer un nombre entre 1 et 12."

print("Le mois correspondant au nombre", nombre, "est", mois)

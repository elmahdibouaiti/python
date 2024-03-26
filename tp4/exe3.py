def Horaire(vitesse):
    # Calcul du temps de trajet en heures
    temps_en_heures = 170 / vitesse
    # Calcul de l'heure d'arrivée (9h étant l'heure de départ)
    heure_arrivee = 9 + temps_en_heures
    # Convertir en heures et minutes, arrondi à la minute inférieure
    heures = int(heure_arrivee)
    minutes = int((heure_arrivee - heures) * 60)
    # Afficher l'heure d'arrivée
    print(f"Vitesse: {vitesse} km/h - Arrivée: {heures}h{minutes:02d}")

print("Tableau des heures d'arrivée à Arras pour des vitesses de 100 à 300 km/h par pas de 10 km/h:")
# Boucle sur les vitesses de 100 à 300 km/h par pas de 10
for vitesse in range(100, 301, 10):
    Horaire(vitesse)

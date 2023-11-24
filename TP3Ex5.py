def calcul_cout_location(heure_debut, heure_fin):
    # Vérifier si les heures sont valides
    if heure_debut < 0 or heure_fin > 24:
        print("Les heures doivent être comprises entre 0 et 24 !\n")
        return

    # Vérifier si l'heure de début est après l'heure de fin
    if heure_debut >= heure_fin:
        print("Attention ! L'heure de début est après l'heure de fin.\n")
        return

    # Calculer le coût de la location en fonction des tarifs
    if 0 <= heure_debut < 7 or 17 <= heure_debut <= 24:
        tarif = 1
    else:
        tarif = 2

    duree_location = heure_fin - heure_debut
    cout_total = tarif * duree_location

    # Afficher le coût de la location
    print(f"Le coût de la location de {heure_debut}h à {heure_fin}h est de {cout_total} euros.")

# Demander à l'utilisateur de saisir les heures de début et de fin de location
try:
    heure_debut = int(input("Entrez l'heure de début de location : "))
    heure_fin = int(input("Entrez l'heure de fin de location : "))

    # Vérifier si l'heure de début est identique à l'heure de fin
    if heure_debut == heure_fin:
        print("Attention ! L'heure de fin est identique à l'heure de début.\n")
    else:
        calcul_cout_location(heure_debut, heure_fin)
except ValueError:
    print("Veuillez entrer des entiers pour les heures de début et de fin de location.\n")
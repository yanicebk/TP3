import random

# Prendre un nombre aléatoire entre 0 et 100
nombre_mystere = random.randint(0, 100)

# Initialisation du compteur
compteur_tours = 0

print("Devinez le nombre mystère entre 0 et 100.")

while True:
    try:
        # Demander à l'utilisateur de deviner le nombre
        tentative = int(input("Votre proposition : "))

        # Incrémenter le compteur de tours
        compteur_tours += 1

        # Comparer la tentative avec le nombre mystère
        if tentative < nombre_mystere:
            print("Le nombre mystère est plus grand. Essayez encore.")
        elif tentative > nombre_mystere:
            print("Le nombre mystère est plus petit. Essayez encore.")
        else:
            print(f"Félicitations ! Vous avez trouvé le nombre mystère en {compteur_tours} tours.")
            break
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")

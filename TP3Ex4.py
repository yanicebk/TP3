def calcul_factorielle_for(n):
    factorielle = 1
    print(f"Calcul de la factorielle de {n} avec la boucle for:")
    for i in range(1, n + 1):
        factorielle *= i
        print(f"Iteration {i}: {factorielle}")
    return factorielle

def calcul_factorielle_while(n):
    factorielle = 1
    i = 1
    print(f"Calcul de la factorielle de {n} avec la boucle while:")
    while i <= n:
        factorielle *= i
        print(f"Iteration {i}: {factorielle}")
        i += 1
    return factorielle

# Demander à l'utilisateur de saisir un entier n
n = int(input("Entrez un entier positif n : "))

# Demander à l'utilisateur de choisir la boucle à utiliser
choix_boucle = input("Choisissez la boucle (for/while) : ").lower()

# Vérifier le choix de l'utilisateur et effectuer le calcul
if choix_boucle == "for":
    resultat = calcul_factorielle_for(n)
elif choix_boucle == "while":
    resultat = calcul_factorielle_while(n)
else:
    print("Choix de boucle invalide. Veuillez choisir 'for' ou 'while'.")
    resultat = None

if resultat is not None:
    print(f"La factorielle de {n} est : {resultat}")
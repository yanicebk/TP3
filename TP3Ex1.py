#Exercice1 a)
N = int(input("Entrez la valeur de N : "))
somme = 0

for i in range(N + 1):
    somme += i

print("La somme des N entiers naturels de 0 à", N, "est :", somme)

#Exercice1 b)
valeur_utilisateur = 0

while valeur_utilisateur != 100:
    valeur_utilisateur = int(input("Entrez une valeur (entrez 100 pour terminer) : "))

print("Vous avez entré la valeur 100. La boucle d'attente se termine.")

#Exercice1 c)
valeurs_inf_10 = 0
valeurs_10_a_15 = 0
valeurs_sup_15 = 0

for _ in range(10):
    valeur = float(input("Entrez une valeur réelle entre 0 et 20 : "))

    while valeur < 0 or valeur > 20:
        valeur = float(input("Veuillez entrer une valeur entre 0 et 20 : "))

    if valeur < 10:
        valeurs_inf_10 += 1
    elif valeur < 15:
        valeurs_10_a_15 += 1
    else:
        valeurs_sup_15 += 1

print("Nombre de valeurs inférieures à 10 :", valeurs_inf_10)
print("Nombre de valeurs entre 10 et 15 inclus :", valeurs_10_a_15)
print("Nombre de valeurs supérieures ou égales à 15 :", valeurs_sup_15)

#Exercice1 d)
X = float(input("Entrez la valeur de X (supérieure à 1) : "))
somme = 0
N = 0

while somme <= X:
    N += 1
    somme += N

print("Le plus grand nombre N tel que la somme des entiers de 0 à N est inférieure ou égale à", X, "est :", N - 1)


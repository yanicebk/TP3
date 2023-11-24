import time

n = int(input("Entrez un nombre entier positif n : "))

print("Compte à rebours :")
for i in range(n, -1, -1):
    print(i)
    time.sleep(1)

import time

n = int(input("Entrez un nombre entier positif n : "))

print("Compte à rebours :")
while n >= 0:
    print(n)
    n -= 1
    time.sleep(1)

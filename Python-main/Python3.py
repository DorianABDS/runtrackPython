# job 1
valeur1 = 1
valeur2 = 2
while valeur1 != valeur2:
    input(str("Choissisez une valeur : "))
    if valeur1 <= valeur2:
        print("les deux valeurs ne sont pas égale")
        break
    elif valeur1 == valeur2:
        valeur1 + 1
        print(valeur1, "est égal à ", valeur2)

# job 5
def est_premier(n):
    """Retourne True si n est un nombre premier, sinon False."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for nombre in range(1000):
    if est_premier(nombre):
        print(nombre)
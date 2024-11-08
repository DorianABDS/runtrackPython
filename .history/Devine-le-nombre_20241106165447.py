# Indiquer un nombre en console, en fonction du nombre à trouver (entre 1 et 100), afficher en console "plus grand" ou "plus petit".

# Il faut:
# faire une boucle qui se fini une fois le "j'ai gagné"
# faire une condition qui compare le nombre choisi par le nombre à trouver

import random

print("Bienvenue dans le juste biscuit ! Trouve le nombre secret entre 1 et 100 et tente de gagner un croc-scooby !")

reponse = 0
while reponse != nombre_secret:
    reponse = int(input("Choisir un nombre : "))

    if reponse < nombre_secret:
        print("Trop petit")
    elif reponse > nombre_secret:
        print("Trop grand")
    else:
        print("Bravo scooby ! Tu as trouvé le nombre secret", nombre_secret)
        print("+ 1 croc-scooby")
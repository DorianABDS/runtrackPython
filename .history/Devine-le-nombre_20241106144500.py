# Indiquer un nombre en console, en fonction du nombre à trouver (entre 1 et 100), afficher en console "plus grand" ou "plus petit".

# Il faut:
# faire une boucle qui se fini une fois le "j'ai gagné"
# faire une condition qui compare le nombre choisi par le nombre à trouver

# boucle variable condition
import random

print("Bienvenue dans le juste prix ! Trouve le nombre secret entre 1 et 100 !")

reponse = int(input("Choisir un nombre : "))
nombre_secret = random.randint(1, 100)

print(reponse)
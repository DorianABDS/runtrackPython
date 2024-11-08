# Indiquer un nombre en console, en fonction du nombre à trouver (entre 1 et 100), afficher en console "plus grand" ou "plus petit".

# Il faut:
# faire une boucle qui se fini une fois le "j'ai gagné"
# faire une condition qui compare le nombre choisi par le nombre à trouver

# boucle variable condition
import random

print("Bienvenue dans le juste prix ! Trouve le nombre secret entre 1 et 100 !")

reponse = int(input("Choisir un nombre : "))
nombre_secret = random.randint(1, 100)
nbr_essais_max = 5
nbr_essais = 1
borne_sup = 30
ton_nombre = 0 

while ton_nombre == nombre_secret and nbr_essais <= nbr_essais_max:
    print("essaie n°", nbr_essais)
    ton_nombre = int(input("Choisi ton numéro :"))

     if ton_nombre < nombre_secret:
        print("Trop petit")

    elif ton_nombre > nombre_secret:
        print("Trop grand")
    
    else:
        print("Bravo scooby !",mon_nombre,"en",nbr_essais,"essai(s)")
        nbr_essais += 1


if nbr_essais>nbr_essais_max and ton_nombre == nombre_secret :
 print("Il te reste",nbr_essais_max,"essais")
 print("Le nombre secret est",mon_nombre,".")

import random

print("Bienvenue dans le juste biscuit ! Trouve le nombre secret entre 1 et 100 et tente de gagner un croc-scooby !")
nombre_secret = random.randint(1, 100)

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
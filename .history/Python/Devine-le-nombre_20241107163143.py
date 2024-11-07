import random

print("Bienvenue dans le juste biscuit ! Trouve le nombre secret entre 1 et 100 et tente de gagner un croc-scooby !")
nombre_secret = random.randint(1, 100)
nbr_essaie_max = 10


reponse = 0
while reponse != nombre_secret:
    reponse = int(input("Choisi un nombre : " + "boop"))

    if reponse < nombre_secret:
        print("Plus haut")
    elif reponse > nombre_secret:
        print("Plus bas")
    else:
        print("Bravo scooby ! Tu as trouvé le nombre secret qui est", nombre_secret)
        print("+ 1 croc-scooby")
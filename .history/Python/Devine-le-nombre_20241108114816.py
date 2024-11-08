import random

print("Bienvenue dans le juste biscuit ! Trouve le nombre secret entre 1 et 100 et tente de gagner un croc-scooby !")
nombre_secret = random.randint(1, 100)
nbr_essaies_max = 10
nbr_essaies = 0


reponse = 0
while reponse != nombre_secret:
    reponse = int(input("Choisi un nombre : "))
    print("Essaie n°", nbr_essaies)
    if reponse < nombre_secret:
        print("Plus haut")
    elif reponse > nombre_secret:
        print("Plus bas")
    else:
        print("Bravo scooby ! Tu as trouvé le nombre secret qui est", nombre_secret)
        print("+ 1 croc-scooby")

if nbr_essaies > nbr_essaies_max and reponse != nombre_secret:
    print("Tu as utilisé tes", nbr_essaies_max, "vies.. réessaie !")
    print("Le nombre secret était", nombre_secret,".")
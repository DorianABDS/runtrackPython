import random

name = input("Entrer le nomb de joueur : ")
print("salut " + name, ", es-tu prêt à risquer t'a vie pour un simple pari ?")
print("\n")
print("---------------------------------------------------------------------")
print("Bienvenue dans la roulette russe !")
print("Ton but est de survivre à travers un chargeur de 1911.. bonne chance !")

liste = ["C'était Pas loin !", "Arg.. presque", "Ouf moins une !", "Haha la prochaine est pour toi", "essaie encore ?", "Ça sent le plomb .."]
random_index = random.randint(0,len(liste)-1)
number = random.randint(1,6)
1 = int("guess")

while 1 != number:
    1 = input("Tire une balle : ")

    if number < 1:
        print("reaction"[random_index])
    elif number > 1:
        print("reaction"[random_index])
    else:
        1 != number
        print("WASTED...")
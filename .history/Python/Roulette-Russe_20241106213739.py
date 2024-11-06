import random

name = input("Entrer le nomb de joueur : ")
print("salut " + name, ", es-tu prêt à risquer t'a vie pour un simple pari ?")
print("\n")
print("---------------------------------------------------------------------")
print("Bienvenue dans la roulette russe !")
print("Ton but est de survivre à travers un chargeur de 1911.. bonne chance !")

reaction = random.randint("C'était pas loin !, Arg.. presque, Ouf moins une !, Haha la prochaine est pour toi, essaie encore ?, ça sent les plombs ..)
number = random.randint(1,10)
guess = input("Tire une balle : ")
guess = int(guess)

if reponse < nombre_secret:
        print("")
    elif reponse > nombre_secret:
        print("")
if guess == number:
    print("WASTED...")
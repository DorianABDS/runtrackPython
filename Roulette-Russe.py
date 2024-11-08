import random

name = input("Entrer le nom de joueur : ")
print("salut " + name, ", es-tu prêt à risquer t'a vie pour un simple pari ?")
print("\n")
print("---------------------------------------------------------------------")
print("Bienvenue dans la roulette russe !")
print("Ton but est de survivre à 6 balles de révolver bonne chance !")

liste = ["C'était Pas loin !", "Arg.. presque", "Ouf moins une !", "Haha la prochaine est pour toi", "essaie encore ?", "Ça sent le plomb .."]
random_index = random.choice(liste)

number = random.randint(1,6)
lop = {0}
guess = ""


while guess != number:
    guess = int(input("Tire une balle : "))
    lop.add(guess)
    print(lop)
    if number < guess:
        print("Cow-boy : ",random_index)
    elif number > guess:
        print("Cow-boy : ",random_index)
    else:
        guess != number
        print("WASTED...")
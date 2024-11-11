import random

# name = input("Entrer le nom de joueur : ")
# print("salut " + name, ", es-tu prêt à risquer t'a vie pour un simple pari ?")
# print("\n")
print("---------------------------------------------------------------------")
print("Bienvenue dans la roulette russe !")
print("Ton but est de survivre à 6 balles de révolver bonne chance !") 

# liste = ["BAAAM ! le revolver a rugi .."]
# random_index = random.choice(liste)

number = random.randint(1,6)
lop = {0}
guess = ""


while guess != number:
    guess = int(input("Tire une balle : "))
    lop.add(guess)
    print(lop)
    if 0 < guess > 6:
        print("c'est pas bon")
        break
    if number < guess:
        print("BAAAM ! le revolver a rugi ..")
    elif number > guess:
        print("BAAAM ! le revolver a rugi ..")
    else:
        guess != number
        print("WASTED...")
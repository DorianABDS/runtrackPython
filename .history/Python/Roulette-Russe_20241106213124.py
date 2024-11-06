import random

name = input("Entrer le nomb de joueur : ")
print("salut " + name, ", es-tu prêt à risquer t'a vie pour un simple pari ?")
print("⭣")
print("\n")
print("Bienvenue dans la roulette russe !")
print("Ton but est de survivre à travers un chargeur de 1911.. bonne chance !")

number = random.randint(1,10)
guess = input("Tire une balle : ")
guess = int(guess)

if guess == number:
    print("WASTED...")
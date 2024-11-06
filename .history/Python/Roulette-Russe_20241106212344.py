import random

print("Bienvenue dans la roulette russe !")
print("Ton but est de survivre à travers un chargeur de 1911.. bonne chance !")

number = random.randint(1,10)
guess = input("Tire une balle : ")
guess = int(guess)

if guess == number:
    print("WASTED...")
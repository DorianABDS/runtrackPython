import string

# job 1
10 + 3
10 - 3
10 * 3
10 / 3
10 // 3
10 % 3

# job 2
print(10+3)

# job 4
alphabet = string.ascii_lowercase
print(alphabet)

# job 5
alphabet = string.ascii_lowercase
alphabet_inverse = alphabet[::-1]
print(alphabet_inverse)

# job 6
ma_string = "Je suis une String"
print(ma_string)

# job 7
num1 = 40
num2 = 2
print(num1 + num2)

# job 8
num1 = 3
num2 = 14

produit = num1 * num2

print(produit)

# job 9
nom_produit = "T-shirt"
prix_unitaire = 20.0
quantite_stock = 50

def afficher_informations():
    print("\n--- Informations sur le produit ---")
    print(f"Nom du produit : {nom_produit}")
    print(f"Prix unitaire : {prix_unitaire:.2f} €")
    print(f"Quantité en stock : {quantite_stock}")
    print("------------------------------------")


afficher_informations()

quantite_achat = int(input("Combien de T-shirts souhaitez-vous acheter ? "))

if quantite_achat <= quantite_stock:

    quantite_stock -= quantite_achat
    print(f"\nVous avez acheté {quantite_achat} T-shirt(s).")
else:
    print("\nDésolé, il n'y a pas assez de T-shirts en stock.")

prix_unitaire = 1.10

afficher_informations()

# job 10
montant_investissement = 10000.0
taux_rendement = 5.0


def calculer_gain_annuel(montant, taux):
    return montant (taux / 100)


gain_annuel_initial = calculer_gain_annuel(montant_investissement, taux_rendement)
print(f"Gain annuel initial : {gain_annuel_initial:.2f} €")


montant_investissement += 5000

taux_rendement += 2

gain_annuel_avec_augmentation = calculer_gain_annuel(montant_investissement, taux_rendement)
print(f"Gain annuel après augmentation de capital : {gain_annuel_avec_augmentation:.2f} €")

retrait = montant_investissement * 0.10
montant_investissement -= retrait

taux_rendement -= 1

gain_annuel_apres_retrait = calculer_gain_annuel(montant_investissement, taux_rendement)
print(f"Montant après retrait : {montant_investissement:.2f} €")
print(f"Nouveau gain annuel après retrait : {gain_annuel_apres_retrait:.2f} euros")

# job11
chaine = input("Veuillez entrer une chaîne de caractères : ")

if 'e' in chaine:
    print("La chaîne contient le caractère 'e'.")
else:
    print("La chaîne ne contient pas le caractère 'e'.")
def main():
    # recolter une valeur porte monnaie
  wallet = int(input("75"))
  print("Vous avez actuellement", wallet, "euros")
 
  # creer un produit qui aura pour valeur 50
  produit = 50
  print("Le Produit vaut ", produit, "euros")
 
  # enleve au "wallet" le prix du produit
  wallet = wallet - produit
  # ou wallet -= produit
 
  # afficher la nouvelle valeur
  print("Produit acheté !")
  print("Il ne vous reste plus que", wallet, "euros")


if __name__ == "__main__":
    main()

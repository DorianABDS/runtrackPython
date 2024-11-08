def main():
    wallet = int(input(75))
    print("vous avez actuellement," wallet, "euros")

    produit = 50
    print("le produit vaut", produit, "euros")

    wallet = wallet - produit

    print("produit acheté !")
    print("il ne vous reste plus que", wallet, "euros")

if __name__ == "__main__":
    main()
